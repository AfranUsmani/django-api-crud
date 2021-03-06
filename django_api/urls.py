"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from cuboid.api.views import *
#from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import views
from cuboid.api.views import RegisterAPI, LoginAPI
from knox import views as knox_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('auth/login/', obtain_jwt_token, name='login'),
    #path('cuboid/', include('cuboid.api.urls', namespace='cuboid-api')),
    #path('api-token-auth/', views.obtain_auth_token , name='api_token_auth'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('', CuboidListAPIView.as_view(), name='cuboid-listcreate'),
    path('new/', CuboidCreateAPIView.as_view(), name='cuboid-create'),
    path('<int:pk>', CuboidRudView.as_view(), name='cuboid-rud'),
    path('user/', CuboidUserListAPIView.as_view(), name='cuboid-retrieve'),
]
