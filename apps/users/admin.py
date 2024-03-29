from django.contrib import admin
from . import models


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "avatar",
        "date_joined",
        "last_login",
    )

    ordering = ("email",)

    search_fields = (
        "username",
        "email",
    )

    list_filter = ("last_login",)


@admin.register(models.Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "phone_number",
        "region",
        "address",
        "zip_code",
        "default",
    )

    ordering = ("user",)

    search_fields = (
        "user",
        "name",
        "phone_number",
    )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "recipient",
        "payment_method",
        "payment_amount",
        "paid",
        "created_time",
        "finished_time",
        "state",
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = self.readonly_fields
        # 设置部分字段只读
        if obj:  # 编辑现有对象时，设置只读字段
            readonly_fields += (
                "user",
                "payment_method",
                "payment_amount",
                "paid",
                "created_time",
                "finished_time",
            )
        return readonly_fields

    ordering = (
        "user",
        "recipient",
    )

    list_filter = ("created_time",)
