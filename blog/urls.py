from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact_us/', views.ContactPage.as_view(), name='contact_us'),
    path('edit_comment/', views.EditComment.as_view(), name='edit_comment'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        "delete/<int:id>",
        views.delete_own_comment,
        name='delete_comment'),
]
