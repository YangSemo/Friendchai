from abc import ABC

from rest_framework import serializers, validators

from .models import (
    Population, Brand, AnalysisModel, Headquarter, StoreAddress,
    Account
)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class BrandSnapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand_name', 'sector', 'average_sales', 'startup_cost', 'num_of_franchise']


class HeadquarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headquarter
        fields = '__all__'
        # fields = ('mutual', 'representative', 'representative_number')


class AnalysisModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisModel
        # fields = ('brand_name', 'average_sales_ratio', 'startup_cost_ratio', 'rate_of_opening_ratio', 'label')
        fields = '__all__'


# class RegisterSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(
#         required=True,
#         validators=[validators.UniqueValidator(queryset=Account.objects.all())]
#     )
#
#     email = serializers.EmailField(
#         required=True,
#         validators=[validators.UniqueValidator(queryset=Account.objects.all())]
#     )
#
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = Account
#         fields = ('username', 'password', 'password2', 'email')
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "비밀번호가 일치하지 않습니다"})
#
#         return attrs
#
#     def create(self, validated_data):
#         account = Account.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#         )
#
#         account.set_password(validated_data['password'])
#         account.save()
#
#         return account
#
#
# class LoginSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(
#         required=True,
#     )
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#
#     class Meta:
#         model = Account
#         fields = ('username', 'email', 'password')


class StoreAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreAddress
        # fields = '__all__'
        fields = ['brand_name', 'sector', 'latitude', 'longitude']


class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Population
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        # fields = '__all__'
        fields = ['username']
