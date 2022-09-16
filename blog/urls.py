from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('success/', views.Success.as_view(), name='success'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('create/', views.AddPost.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

handler404 = "meta_human.views.page_not_found_view"
