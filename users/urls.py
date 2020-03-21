from django.urls import path

from . import views

app_name='users'

urlpatterns = [
    path('register/', views.register),
    path('token/', views.token),
    path('token/refresh/', views.refresh_token),
    path('token/revoke/', views.revoke_token),

    path('login/', views.login_view, name='login'),
    path('registering/', views.register_view),
    path('logout/', views.logout_view, name='logout')
]