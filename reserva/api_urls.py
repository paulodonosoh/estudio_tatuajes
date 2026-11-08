from rest_framework.routers import DefaultRouter

from .api_views import ReservaViewSet

router = DefaultRouter()
router.register('reservas', ReservaViewSet, basename='reserva')

urlpatterns = router.urls
