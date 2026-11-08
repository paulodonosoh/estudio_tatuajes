from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Reserva
from .serializers import ReservaSerializer


class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.select_related('artista').all()
    serializer_class = ReservaSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]
