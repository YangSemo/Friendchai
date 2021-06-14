from django.contrib import admin

from .models import (
    Brand, Headquarter, StoreAddress, Population, Account
)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'sector', 'mutual')
    list_filter = ['brand_name']
    search_fields = ['brand_name']


class HeadquarterAdmin(admin.ModelAdmin):
    list_display = ('mutual', 'address')
    list_filter = ['mutual']
    search_fields = ['mutual']


class StoreAddressAdmin(admin.ModelAdmin):
    list_display = ('sector', 'brand_name', 'do', 'sigu', 'dong', 'longitude', 'latitude')
    list_filter = ['brand_name']
    search_fields = ['brand_name']


class PopulationAdmin(admin.ModelAdmin):
    list_display = ('do', 'sigu', 'dong', 'population')
    list_filter = ['sigu']
    search_fields = ['do']


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'joined_at', 'last_login_at')
    list_display_links = ('email', 'username')
    search_fields = ('username', 'email')
    readonly_fields = ('id', 'date_joined', 'last_login')
    exclude = ('password',)  # 사용자 상세 정보에서 비밀번호 필드를 노출하지 않음

    def joined_at(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d")

    def last_login_at(self, obj):
        if not obj.last_login:
            return ''
        return obj.last_login.strftime("%Y-%m-%d %H:%M")

    joined_at.admin_order_field = '-date_joined'  # 가장 최근에 가입한 사람부터 리스팅
    joined_at.short_description = '가입일'
    last_login_at.admin_order_field = 'last_login_at'
    last_login_at.short_description = '최근로그인'


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username')
    list_display_links = ('email', 'username')
    search_fields = ('username', 'email')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Headquarter, HeadquarterAdmin)
admin.site.register(StoreAddress, StoreAddressAdmin)
admin.site.register(Population, PopulationAdmin)
admin.site.register(Account, UserAdmin)
