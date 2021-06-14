from django.contrib.auth import authenticate, login, logout

from rest_framework import (
    viewsets, permissions, generics, filters,
    views
)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import (
    BrandSerializer, PopulationSerializer, BrandSnapSerializer,
    AnalysisModelSerializer, HeadquarterSerializer, StoreAddressSerializer,
    AccountSerializer
)
from .models import (
    Brand, Headquarter, Population, AnalysisModel, StoreAddress,
    Account,
)


class BrandListView(generics.ListAPIView):
    """
        브랜드 리스트 조회
    """
    search_fields = ['brand_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Brand.objects.all()
    serializer_class = BrandSnapSerializer

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('name'):
            queryset = self.get_queryset().filter(brand_name__contains=request.GET.get('name'))
        elif request.GET.get('id'):
            queryset = self.get_queryset().filter(id__iexact=request.GET.get('id'))
        else:
            queryset = self.get_queryset()

        serializer = BrandSnapSerializer(queryset, many=True)
        return Response(serializer.data)


class BrandDetailView(views.APIView):
    """
        브랜드 상세 정보
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('name'):
            queryset = self.get_queryset().filter(brand_name__iexact=request.GET.get('name'))
        else:
            queryset = self.get_queryset()

        serializer = BrandSerializer(queryset, many=True)
        if serializer.data:
            return Response(serializer.data, status=200)
        else:
            return Response(status=500)


class HeadquarterView(views.APIView):
    """
        본사 리스트 조회
    """
    queryset = Headquarter.objects.all()
    serializer_class = HeadquarterSerializer

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        print(request.GET)
        if request.GET.get('mutual'):
            queryset = self.get_queryset().filter(mutual__contains=request.GET.get('mutual'))
        else:
            queryset = self.get_queryset()
        serializer = HeadquarterSerializer(queryset, many=True)
        return Response(serializer.data)


class StoreAddressView(generics.ListAPIView):
    """
        가게 위치 정보 조회
    """
    queryset = StoreAddress.objects.all()
    serializer_class = StoreAddressSerializer

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        print(request)
        if request.GET.get('do') and request.GET.get('sigu') and request.GET.get('dong') and request.GET.get('sector'):
            queryset = self.get_queryset().filter(
                do__iexact=request.GET.get('do'),
                sigu__iexact=request.GET.get('sigu'),
                dong__iexact=request.GET.get('dong'),
                sector__iexact=request.GET.get('sector'),
            )
        else:
            queryset = self.get_queryset()
        serializer = StoreAddressSerializer(queryset, many=True)
        return Response(serializer.data)


class PopulationListView(generics.ListAPIView):
    """
        인구수 정보 조회
    """
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer

    def get_queryset(self):
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get('do') and request.GET.get('sigu') and request.GET.get('dong'):
            queryset = self.get_queryset().filter(
                do__iexact=request.GET.get('do'),
                sigu__iexact=request.GET.get('sigu'),
                dong__iexact=request.GET.get('dong'))
        else:
            queryset = self.get_queryset()
        serializer = PopulationSerializer(queryset, many=True)
        return Response(serializer.data)


class RegisterView(views.APIView):
    def post(self, request, *args, **kwargs):
        if request.data.get('email') and request.data.get('username') and request.data.get('password'):
            user = Account.objects.create_user(
                email=request.data.get('email'),
                username=request.data.get('username'),
                password=request.data.get('password')
            )
            user.save()
            if Account.objects.filter(email__iexact=request.data.get('email')):
                return Response(status=200)
            else:
                return Response(status=500)
        return Response(status=500)


class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user is not None:
            login(request, user=user)
            if user.is_authenticated:
                auth_user = Account.objects.all().filter(email__iexact=request.data.get('email'))
                serializer = AccountSerializer(auth_user, many=True)
                return Response(serializer.data, status=200)
        else:
            unauth_user = Account.objects.all().filter(id__iexact='_')
            serializer = AccountSerializer(unauth_user, many=True)
            return Response(serializer.data, status=200)


class LogoutView(views.APIView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(status=200)


class BaseThemeView(views.APIView):
    """
    사용자로부터 테마 선택 입력받고 (1~5 레이블) AnalysisRatioModel 레이블 별 상위 10개 브랜드 반환
    """
    queryset = AnalysisModel.objects.all()
    serializer_class = AnalysisModelSerializer

    def get_queryset(self):
        return self.queryset.order_by('average_sales_ratio', 'startup_cost_ratio',
                                      'rate_of_opening_ratio')

    def get(self, request, *args, **kwargs):
        if request.GET.get('label'):
            if request.GET.get('sector') and request.GET.get('label'):
                queryset = self.get_queryset().filter(sector__iexact=request.GET.get('sector')) \
                    .filter(label__iexact=request.GET.get('label'))
            else:
                queryset = self.get_queryset().filter(label__iexact=request.GET.get('label'))
            query_result = list(queryset)

            top_brands = []
            for row in query_result:
                top_brands.append(
                    [row.brand_name,
                     float(row.average_sales_ratio + (1 - row.startup_cost_ratio) + row.rate_of_opening_ratio)])
            top_brands.sort(key=lambda x: -x[1])
            brand_list = []
            for row in top_brands[:10]:
                brand_list.append(row[0])

            serializer = AnalysisModelSerializer(
                queryset.filter(brand_name__in=brand_list), many=True)
            return Response(serializer.data)


from .apps import FranchiseClassifier


class CustomThemeView(views.APIView):
    """
    사용자가 특성의 우선순위를 입력 받아 그에 맞게 상위 10개 브랜드 반환
    """
    queryset = AnalysisModel.objects.all()
    serializer_class = AnalysisModelSerializer

    # classifierModel test
    # print("result: ", FranchiseClasseifier.load_model.predict([[75, 38, 999025, 85020, 18, 10]]))

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        # get custom property
        if request.GET:
            p1 = request.GET.get('p1')
            p2 = request.GET.get('p2')
            p3 = request.GET.get('p3')
            p4 = request.GET.get('p4')
            p5 = request.GET.get('p5')
            p6 = request.GET.get('p6')

            # features ranking => [number_of_months,franchise_count,average_sales,cost,open_rate,close_rate]
            # rank = request.GET.get('features_ranking')
            rank = [p1, p2, p3, p4, p5, p6]
            # 5 4 0 1 2 3
            # features weight => [0.9, 0.7, 0.5, 0.3, 0.2, 0.1]
            # rank_weight = request.GET.get('features_weight')
            rank_weight = [0.9, 0.7, 0.5, 0.3, 0.2, 0.1]

            # features ranking score
            number_of_months = [309, 198, 84, 75, 74, 35]
            franchise_count = [1338, 107, 38, 31, 28, 16]
            average_sales = [999025, 361352, 297889, 268958, 237821, 228112]
            cost = [72716, 85020, 86420, 92785, 128907, 266781]
            open_rate = [78, 21, 18, 18, 8, 6]
            close_rate = [4, 6, 11, 13, 14, 20]

            # classifierModel result => label extraction
            classify_result = FranchiseClassifier.load_model.predict([[number_of_months[int(rank[0])],
                                                                       franchise_count[int(rank[1])],
                                                                       average_sales[int(rank[2])],
                                                                       cost[int(rank[3])],
                                                                       open_rate[int(rank[4])],
                                                                       close_rate[int(rank[5])]]])

            print(request.GET.get('sector'))
            # get that label
            if request.GET.get('sector'):
                query = self.get_queryset().filter(sector__iexact=request.GET.get('sector')) \
                                            .filter(label__iexact=classify_result[0])
            else:
                query = self.get_queryset().filter(label__iexact=classify_result[0])
            query_result = list(query)

            top_brands = []
            for row in query_result:
                # brand weight calculration
                top_brands.append(
                    [row.brand_name, float((row.franchise_months_ratio * rank_weight[int(rank[0])]) +
                                           (row.num_of_franchise_ratio * rank_weight[int(rank[1])]) +
                                           (row.average_sales_ratio * rank_weight[int(rank[2])]) +
                                           ((1 - row.startup_cost_ratio) * rank_weight[int(rank[3])]) +
                                           (row.rate_of_opening_ratio * rank_weight[int(rank[4])]) +
                                           ((1 - row.rate_of_closing_ratio) * rank_weight[int(rank[5])]))])

            # brand score sorting
            top_brands.sort(key=lambda x: -x[1])
            brand_list = []
            for row in top_brands[:10]:
                brand_list.append(row[0])
            print(brand_list)

            serializer = AnalysisModelSerializer(
                # AnalysisModel.objects.filter(brand_name__in=brand_list).filter(label__iexact=2), many=True)
                query.filter(brand_name__in=brand_list), many=True)
            return Response(serializer.data)
        else:
            return Response(status=400)
