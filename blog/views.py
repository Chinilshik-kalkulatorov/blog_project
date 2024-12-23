from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

def article_list(request):
    articles = Article.objects.order_by('-created_at')
    paginator = Paginator(articles, 6)  # По 6 статей на страницу
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/article_list.html', {
        'page_obj': page_obj,
    })

def load_more_articles(request):
    """Возвращает следующую страницу статей в виде HTML."""
    if request.method == 'GET':
        page = request.GET.get('page', 2)  # Начнём загрузку со 2-й страницы
        articles = Article.objects.order_by('-created_at')

        paginator = Paginator(articles, 6)
        page_obj = paginator.get_page(page)

        # Рендерим кусок HTML через отдельный «парциальный» шаблон
        articles_html = render_to_string(
            'blog/articles_list_partial.html',
            {'page_obj': page_obj}
        )

        return JsonResponse({
            'articles_html': articles_html,
            'has_next': page_obj.has_next()
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)

def article_detail(request, article_id):
    # Ищем статью по ID
    article = get_object_or_404(Article, pk=article_id)
    # Рендерим шаблон и передаём туда статью
    return render(request, 'blog/article_detail.html', {'article': article})