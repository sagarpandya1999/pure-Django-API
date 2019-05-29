"""restfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest import views
from rest.api import urls
from status.api import urls

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.list_view, name='list'),
    path('<int:id>/', views.detail_view, name='detail'),

    path('json/cbv/', views.JsonCBV.as_view(), name='cbv'),
    path('json/cbv2/', views.JsonCBV2.as_view(), name='cbv2'),

    path('json/serialize/list/', views.SerializedListView.as_view(), name='serialize_list'),
    path('json/serialize/detail/', views.SerializedDetailView.as_view(), name='serialize_detail'),

    path('rest/api/', include('rest.api.urls')),
    path('status/api/', include('status.api.urls')),

]
