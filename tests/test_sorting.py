import pytest
from django.utils import timezone
from django.urls import reverse
from blog.models import Article
import datetime

@pytest.mark.django_db
def test_sorting_by_date(client):
    """
    Создаём 2 статьи с разными датами, 
    проверяем, что более свежая идёт первой в HTML (при Meta: ordering = ['-created_at']).
    """

    # Статья постарше (created_at: вчера)
    older_article = Article.objects.create(
        title="Older Article",
        short_description="Old desc",
        created_at=timezone.now() - datetime.timedelta(days=1)
    )

    # Статья поновее (created_at: сейчас)
    newer_article = Article.objects.create(
        title="Newer Article",
        short_description="New desc",
        created_at=timezone.now()
    )

    # Допустим, у вас есть URL с именем 'article_list'
    url = reverse('article_list')
    response = client.get(url)
    assert response.status_code == 200

    # Преобразуем содержимое ответа в текст
    content = response.content.decode()

    # Проверяем, что "Newer Article" встречается в тексте раньше, чем "Older Article"
    index_newer = content.index("Newer Article")
    index_older = content.index("Older Article")
    assert index_newer < index_older