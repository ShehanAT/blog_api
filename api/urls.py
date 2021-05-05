from django.contrib import admin
from django.urls import path, include 
from rest_framework import routers
from . import views 



# router = routers.DefaultRouter()
# router.register(r'api/posts', views.PostViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.home, name='home'),
    path('api/posts', views.posts_view),
    # path('api/posts/', include('rest_framework.urls',
    # namespace='rest_framework')),
    
    path('api/ping', views.ping_view)
]