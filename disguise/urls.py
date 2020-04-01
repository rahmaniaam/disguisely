from django.urls import path

from . import views

app_name='disguise'

urlpatterns = [
    path(r'', views.upload_form_view, name='upload'),
    path('progress/<uuid:key>/', views.progress_view, name='progress'),
    path('zip/', views.zip_worker, name='zip')
]