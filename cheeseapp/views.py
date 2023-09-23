from .models import Cheese
from rest_framework import viewsets, permissions
from .serializers import CheeseSerializer

class CheeseViewset(viewsets.ModelViewSet):
    queryset = Cheese.objects.all()
    serializer_class = CheeseSerializer
    permission_classes = [permissions.AllowAny]