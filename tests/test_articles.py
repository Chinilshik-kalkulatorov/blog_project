import pytest
from django.urls import reverse
from blog.models import Article

@pytest.mark.django_db
def test_article_creation():
    """Проверяем, что можем создать статью и она сохраняется в БД."""
    article = Article.objects.create(
        title="Тестовая статья",
        short_description="Описание",
    )
    assert article.id is not None
    assert article.title == "Тестовая статья"

@pytest.mark.django_db
def test_article_list_view(client):
    """Проверяем, что на странице списка отображаются статьи."""
    Article.objects.create(title="Статья 1", short_description="...")
    Article.objects.create(title="Статья 2", short_description="...")

    url = reverse('article_list')  # предполагаем, что у вас name='article_list'
    response = client.get(url)
    assert response.status_code == 200

    # Проверяем, что в выводе есть строки "Статья 1" и "Статья 2"
    content = response.content.decode('utf-8')
    assert "Статья 1" in content
    assert "Статья 2" in content