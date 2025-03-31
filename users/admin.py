from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    model = User

    # 관리자 목록 페이지에서 보여줄 필드
    list_display = ('id', 'username', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username',)
    ordering = ('id',)

    # 관리자 상세 페이지에서 보여줄 필드 설정
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('권한 설정', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('중요 날짜', {'fields': ('last_login', 'date_joined')}),
    )

    # 새 사용자 추가 시 보여줄 필드 설정
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
