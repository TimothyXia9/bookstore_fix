from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("detail/<int:book_id>/<int:page>", views.DetailView.as_view(), name="detail"),
    path(
        "category/<int:category_id>/<int:page>",
        views.CategoryView.as_view(),
        name="category",
    ),
    path(
        "detail/<int:book_id>/<int:page>/submit_comment",
        views.CommentSubmitView.as_view(),
        name="comment_submit",
    ),
    path(
        "detail/<int:book_id>/<int:page>/delete_comment/<int:comment_id>/",
        views.delete_comment,
        name="delete_comment",
    ),
]
