from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator
from . import models as book_models
from django.shortcuts import render, redirect


class DetailView(View):
    def get(self, request, book_id, page):
        book = get_object_or_404(book_models.Book, pk=book_id)
        pagination = Paginator(book.comments.order_by("-published_time").all(), 7).page(
            page
        )
        comments = pagination.object_list
        return render(
            request,
            "detail.html",
            {
                "book": book,
                "comments": comments,
                "pagination": pagination,
            },
        )


class CategoryView(View):
    def get(self, request, category_id, page):
        # 类别
        categories = book_models.CategoryFirst.get_category_first()
        current_category = book_models.CategorySecond.get_category_second(category_id)
        # 分页
        pagination = Paginator(current_category.books.all(), 16).page(page)
        category_books = pagination.object_list
        # 新书热卖榜
        new_hot_books = book_models.Book.get_new_hot_books(current_category)
        # 图书畅销榜
        hot_books = book_models.Book.get_hot_books(current_category)
        return render(
            request,
            "category.html",
            {
                "categories": categories,
                "category_books": category_books,
                "current_category": current_category,
                "new_hot_books": new_hot_books,
                "hot_books": hot_books,
                "pagination": pagination,
            },
        )


class CommentSubmitView(View):
    def post(self, request, book_id, page):
        book = book_models.Book.objects.get(id=book_id)
        comment_text = request.POST["comment"]
        user_now = request.user
        # 根据需要进行评论的处理，例如创建评论对象并保存到数据库
        comment = book_models.Comment(book=book, content=comment_text, user=user_now)
        comment.save()
        print("saved")
        return redirect("/book/detail/" + str(book_id) + "/" + str(page) + "#comment")


def delete_comment(request, book_id, page, comment_id):
    comment = get_object_or_404(book_models.Comment, id=comment_id)
    # 进行删除评论的操作
    if comment.user == request.user:
        comment.delete()
    return redirect("book:detail", book_id=book_id, page=page)
