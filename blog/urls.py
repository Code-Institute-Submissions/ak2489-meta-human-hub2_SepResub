from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('success/', views.Success.as_view(), name='success'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('create/', views.AddPost.as_view(), name='create_post'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path(
        '<slug:slug>/delete/', views.DeletePost.as_view(), name='delete_post'),
]

handler404 = "meta_human.views.page_not_found_view"
