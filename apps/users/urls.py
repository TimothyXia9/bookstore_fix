from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("settings", views.SettingsView.as_view(), name="settings-get"),
    path("settings/<str:option>", views.SettingsView.as_view(), name="settings-post"),
    path("order", views.OrderView.as_view(), name="order"),
    path("confirm/<int:order_id>", views.confirm_order, name="confirm"),
    path("cancel/<int:order_id>", views.cancel_order, name="cancel"),
    path(
        "delete-address/<int:address_id>",
        views.delete_address,
        name="delete_address",
    ),
]
