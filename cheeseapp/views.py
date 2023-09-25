from .models import cheeseAttr
from rest_framework import viewsets, permissions
from .serializers import cheeseSerializer

class CheeseViewset(viewsets.ModelViewSet):
    queryset = cheeseAttr.objects.all()
    serializer_class = cheeseSerializer
    permission_classes = [permissions.AllowAny]