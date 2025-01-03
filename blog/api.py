# blog/api.py
from rest_framework import viewsets
from .models import Article, MenuItem
from .serializers import ArticleSerializer, MenuItemChildSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ArticleViewSet(viewsets.ModelViewSet):
    """
    Полноценный CRUD для статей.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class MenuTreeAPIView(APIView):
    def get(self, request):
        # Ищем только корневые пункты (нет parent)
        roots = MenuItem.objects.filter(parent__isnull=True).order_by('sort_order')
        data = MenuItemChildSerializer(roots, many=True).data
        return Response(data)