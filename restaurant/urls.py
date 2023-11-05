from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register('menu', MenuViewSet, basename='menu')
router.register('booking', BookingViewSet, basename='booking')

urlpatterns = router.urls
