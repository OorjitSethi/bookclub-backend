from django.urls import include, path
from rest_framework import routers
from .views import WebpageViewSet, SessionViewSet, ViewerViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'webpages', WebpageViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'viewers', ViewerViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
