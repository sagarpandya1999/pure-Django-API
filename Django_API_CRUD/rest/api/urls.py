
from django.urls import path
from rest.api import views

urlpatterns = [

    path('', views.UpdateModelListAPIView.as_view(), name='api_list'),
    path('<int:id>/', views.UpdateModelDetailAPIView.as_view(), name='api_detail'),

]