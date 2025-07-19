from django.urls import path
from . import views

app_name = 'providers'

urlpatterns = [
    path('', views.search_page, name='search'),
    path('provider/<str:npi>/', views.provider_detail, name='detail'),
]