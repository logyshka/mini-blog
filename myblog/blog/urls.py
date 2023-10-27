from django.urls import path

from . import views

urlpatterns = [
    path('', views.PublicationView.as_view()),
    path('<int:pk>/', views.PublicationDetail.as_view()),
    path('review/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
    path('<int:pk>/add_like/', views.AddLike.as_view(), name='add_like'),
]
