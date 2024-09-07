from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, UserListView, UserDetailView, UserUpdateView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('user_login/', LoginView.as_view(template_name="users/user_login.html"), name='user_login'),
    path("user_logout/", LogoutView.as_view(), name="user_logout"),
    path('user_register/', UserCreateView.as_view(), name='user_register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('<int:pk>/user_detail/', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/user_edit/', UserUpdateView.as_view(), name='user_edit'),
    path('<int:pk>/user_delete/', UserDeleteView.as_view(), name='user_delete'),
]
