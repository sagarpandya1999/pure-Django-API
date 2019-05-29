from django.urls import path
from .views import StatusListAPIView

urlpatterns = [

    path('', StatusListAPIView, name='list'),

]
