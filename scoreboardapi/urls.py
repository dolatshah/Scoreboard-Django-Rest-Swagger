from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)

# using automatic URL routing with login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('pointsUpdate/<str:pk>/', views.pointsUpdate, name="pointsUpdate"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
