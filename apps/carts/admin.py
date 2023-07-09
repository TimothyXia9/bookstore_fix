from django.contrib import admin
from . import models

# @admin.register(models.Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ('user',)  # 显示的字段
#     ordering = ('user',)  # 排序的字段
#     search_fields = ('user',)  # 搜索的字段


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    actions = None

    list_display = (
        "cart",
        "book",
        "order",
        "quantity",
    )

    ordering = (
        "cart",
        "id",
    )

    search_fields = (
        "book",
        "cart",
    )

    readonly_fields = (
        "cart",
        "book",
        "order",
        "quantity",
    )  # 设置只读字段

    # 取消添加修改删除权限
    def has_add_permission(self, request):
        return False

    # Allow viewing objects but not actually changing them
    def has_change_permission(self, request, obj=None):
        if request.method not in ("GET", "HEAD"):
            return False
        return super(CartItemAdmin, self).has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False
