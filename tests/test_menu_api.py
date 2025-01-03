import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from blog.models import MenuItem

@pytest.mark.django_db
def test_menu_tree_api():
    # Создаём 2 корневых и 1 ребёнка у первого
    root1 = MenuItem.objects.create(title="Root 1", sort_order=1)
    root2 = MenuItem.objects.create(title="Root 2", sort_order=2)
    child1 = MenuItem.objects.create(title="Child 1.1", parent=root1)

    url = reverse('menu_tree_api')  # path('api/menu/', MenuTreeAPIView.as_view(), name='menu_tree_api')
    client = APIClient()
    response = client.get(url)

    assert response.status_code == 200
    json_data = response.json()
    # Ожидаем массив корневых пунктов
    assert len(json_data) == 2

    # Проверим порядок (sort_order)
    assert json_data[0]['title'] == "Root 1"
    assert json_data[1]['title'] == "Root 2"

    # У первого корневого должен быть 1 child
    assert len(json_data[0]['children']) == 1
    assert json_data[0]['children'][0]['title'] == "Child 1.1"
    # У второго корневого нет детей
    assert len(json_data[1]['children']) == 0