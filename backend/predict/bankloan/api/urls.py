from django.urls import path, include 
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', views.ApprovalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('status/', views.approvereject),

    # path('form/', views.myform, name='myform'),
]