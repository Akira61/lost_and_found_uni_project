from django.urls import path, include
from .views import ResetPasswordConfirmView, UsernameResetConfirmView, EmailActivationConfirmView

urlpatterns = [
    path('password/reset/confirm/<str:uid>/<str:token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path(
        "username/reset/confirm/<str:uid>/<str:token>/",
        UsernameResetConfirmView.as_view(),
        name="username_reset_confirm_page",
    ),
    path(
            "activate/<str:uid>/<str:token>/",
            EmailActivationConfirmView.as_view(),
            name="activation_confirm_page",
    ),
]
