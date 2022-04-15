from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('contact_us/', views.ContactPage.as_view(), name='contact_us'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        "delete/<int:id>",
        views.delete_own_comment,
        name='delete_comment'),
]
