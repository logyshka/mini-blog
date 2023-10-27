from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views import View

from .form import CommentForm
from .models import Publication, Like


class PublicationView(View):
    """Вывод публикаций"""

    def get(self, request: WSGIRequest):
        publications = Publication.objects.all()
        data = {
            'publications': publications
        }
        return render(request, 'blog/blog.html', data)


class PublicationDetail(View):
    """Вывод одной публикации"""
    def get(self, request: WSGIRequest, pk: int):
        publication = Publication.objects.get(id=pk)
        data = {
            'publication': publication
        }
        return render(request, 'blog/blog_detail.html', data)


class AddComment(View):
    """Добавление комментария"""

    def post(self, request: WSGIRequest, pk: int):
        form = CommentForm(request.POST)

        if form.is_valid():
            form = form.save(False)
            form.publication_id = pk
            form.save()

        return redirect(f'/{pk}')


class AddLike(View):
    """Поставить лайк"""

    def get(self, request: WSGIRequest, pk: int):
        ip_client = get_client_ip(request)

        try:
            like = Like.objects.get(ip=ip_client, publication_id=pk)
            like.delete()
        except:
            like = Like(
                ip=ip_client,
                publication_id=pk
            )
            like.save()
        return redirect(f'/{pk}')


def get_client_ip(request: WSGIRequest) -> str:
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
