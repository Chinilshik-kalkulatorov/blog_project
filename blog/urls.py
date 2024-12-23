from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import article_list, load_more_articles, article_detail
from .api import ArticleViewSet  # <-- наш ViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article') 
# Это создаст пути: /articles/, /articles/{pk}/ и т.д.

urlpatterns = [
    path('', article_list, name='article_list'),
    path('load-more/', load_more_articles, name='load_more_articles'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),

    # Все пути, сгенерированные router, будут по адресу /api/...
    path('api/', include(router.urls)),
]