from django.urls import path

from .views import AddPostView, ArticleDetailView, HomeView, UpdatePostView

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),


]
