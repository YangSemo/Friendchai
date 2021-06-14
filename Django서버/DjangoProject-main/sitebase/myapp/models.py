from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Brand(models.Model):
    # id | 업종 | 브랜드 | 상호 | 가맹사업 개시일 | 가맹사업 개월수
    id = models.CharField(max_length=8, primary_key=True)
    sector = models.CharField(max_length=16)
    brand_name = models.CharField(max_length=40)
    mutual = models.CharField(max_length=40)
    franchise_start_date = models.CharField(max_length=40)
    franchise_months = models.IntegerField()

    # 가맹점수 | 임직원수 | 신규개점 | 폐점수 | 종료수 | 명의변경
    num_of_franchise = models.IntegerField()
    num_of_employees = models.IntegerField()
    num_of_open = models.IntegerField()
    num_of_quit = models.IntegerField()
    num_of_cancel = models.IntegerField()
    num_of_name_changing = models.IntegerField()

    # 평균 매출액 | 면적 당 평균 매출액 | 가맹비 | 교육비 | 보증금 | 기타 비용
    average_sales = models.IntegerField()
    average_sales_per_area = models.IntegerField()
    franchise_fee = models.IntegerField()
    education_fee = models.IntegerField()
    deposit = models.IntegerField()
    other_cost = models.IntegerField()

    # 창업비용 | 면적당 비용 | 기준 면적 | 전체 비용
    startup_cost = models.IntegerField()
    cost_per_area = models.IntegerField()
    standard_area = models.IntegerField()
    total_cost = models.IntegerField()

    def get_absolute_url(self):
        return reverse('myapp:detail', kwargs={'pk': self.id})


class Headquarter(models.Model):
    # 5
    id = models.CharField(max_length=8, primary_key=True)
    mutual = models.CharField(max_length=40)
    representative = models.CharField(max_length=40)
    register_law_date = models.CharField(max_length=40)
    register_biz_date = models.CharField(max_length=40)

    # 6
    representative_number = models.CharField(max_length=40)
    fax_number = models.CharField(max_length=40)
    address = models.CharField(max_length=128)
    biz_type = models.CharField(max_length=40)
    law_number = models.CharField(max_length=40)
    biz_number = models.CharField(max_length=40)

    # 6
    assets_2020 = models.FloatField()
    liabilities_2020 = models.FloatField()
    equity_2020 = models.FloatField()
    sales_2020 = models.FloatField()
    income_2020 = models.FloatField()
    net_income_2020 = models.FloatField()

    # 6
    assets_2019 = models.FloatField()
    liabilities_2019 = models.FloatField()
    equity_2019 = models.FloatField()
    sales_2019 = models.FloatField()
    income_2019 = models.FloatField()
    net_income_2019 = models.FloatField()

    # 6
    assets_2018 = models.FloatField()
    liabilities_2018 = models.FloatField()
    equity_2018 = models.FloatField()
    sales_2018 = models.FloatField()
    income_2018 = models.FloatField()
    net_income_2018 = models.FloatField()

    # 6
    assets_2017 = models.FloatField()
    liabilities_2017 = models.FloatField()
    equity_2017 = models.FloatField()
    sales_2017 = models.FloatField()
    income_2017 = models.FloatField()
    net_income_2017 = models.FloatField()

    # 3
    opening_2020 = models.IntegerField()
    closing_2020 = models.IntegerField()
    name_change_2020 = models.IntegerField()

    # 3
    opening_2019 = models.IntegerField()
    closing_2019 = models.IntegerField()
    name_change_2019 = models.IntegerField()

    # 3
    opening_2018 = models.IntegerField()
    closing_2018 = models.IntegerField()
    name_change_2018 = models.IntegerField()

    # 3
    opening_2017 = models.IntegerField()
    closing_2017 = models.IntegerField()
    name_change_2017 = models.IntegerField()

    # 3
    num_of_correction = models.IntegerField()
    num_loss_of_law = models.IntegerField()
    num_of_sentences = models.IntegerField()


class StoreAddress(models.Model):
    id = models.CharField(max_length=8, primary_key=True, null=False)
    sector = models.CharField(max_length=16, null=False)
    brand_name = models.CharField(max_length=40)

    do = models.CharField(max_length=16, null=False)
    sigu = models.CharField(max_length=32, null=False)
    dong = models.CharField(max_length=16)

    longitude = models.CharField(max_length=16, null=False)
    latitude = models.CharField(max_length=16, null=False)


class Population(models.Model):
    id = models.CharField(max_length=8, primary_key=True, null=False)
    do = models.CharField(max_length=16, null=False)
    sigu = models.CharField(max_length=32, null=False)
    dong = models.CharField(max_length=16)
    population = models.IntegerField()


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email 주소가 있어야 합니다.")
        if not username:
            raise ValueError('사용자 이름이 있어야 합니다.')
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    id = models.SmallAutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(verbose_name='email', max_length=128, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['username']  # 필수입력 필드
    USERNAME_FIELD = 'email'  # 로그인 식별자

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    objects = UserAccountManager()


class AnalysisModel(models.Model):
    id = models.CharField(max_length=8, primary_key=True)

    # model
    sector = models.CharField(max_length=16)
    brand_name = models.CharField(max_length=40)
    franchise_months = models.IntegerField()

    num_of_franchise = models.IntegerField()
    average_sales = models.IntegerField()
    startup_cost = models.IntegerField()

    rate_of_opening = models.IntegerField()
    rate_of_closing = models.IntegerField()

    # ratio
    franchise_months_ratio = models.FloatField()
    num_of_franchise_ratio = models.FloatField()
    average_sales_ratio = models.FloatField()

    startup_cost_ratio = models.FloatField()
    rate_of_opening_ratio = models.FloatField()
    rate_of_closing_ratio = models.FloatField()

    label = models.IntegerField()

    def __str__(self):
        return 'id' + self.id + self.sector + self.brand_name
