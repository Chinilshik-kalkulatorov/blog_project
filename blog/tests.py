from django.test import TestCase
from .models import Article
from django.urls import reverse

class ArticleModelTest(TestCase):
    def test_create_article(self):
        article = Article.objects.create(
            title="Тестовая статья",
            short_description="Краткое описание",
        )
        # Проверяем, что статья создалась
        self.assertEqual(article.title, "Тестовая статья")
        self.assertIsNotNone(article.id)

class ArticleListViewTest(TestCase):
    def test_article_list_view(self):
        # Создадим пару статей
        Article.objects.create(title="Статья 1", short_description="...")
        Article.objects.create(title="Статья 2", short_description="...")

        # Переходим на главную, где article_list
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        # Проверяем, что заголовок статьи появляется в контексте
        self.assertContains(response, "Статья 1")
        self.assertContains(response, "Статья 2")

class ArticleDetailViewTest(TestCase):
    def test_article_detail_view(self):
        # Создаём статью
        article = Article.objects.create(title="Статья 1", short_description="...")

        # Переходим на её детальную страницу
        response = self.client.get(reverse('article_detail', args=[article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Статья 1")