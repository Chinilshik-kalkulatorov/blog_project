import pytest
from blog.models import MenuItem

@pytest.mark.django_db
def test_create_root_menu_item():
    root = MenuItem.objects.create(title="Root Menu", description="<p>Root Description</p>")
    assert root.id is not None
    assert root.title == "Root Menu"
    assert root.description == "<p>Root Description</p>"
    # У корня нет parent
    assert root.parent is None

@pytest.mark.django_db
def test_create_child_menu_item():
    root = MenuItem.objects.create(title="Root")
    child = MenuItem.objects.create(title="Child", parent=root, description="<p>Child Desc</p>")

    assert child.id is not None
    assert child.parent == root
    assert root.children.count() == 1
    assert root.children.first() == child
    assert child.description == "<p>Child Desc</p>"