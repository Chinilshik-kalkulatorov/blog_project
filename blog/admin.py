from django.contrib import admin
from .models import Article, MenuItem

admin.site.register(Article)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'sort_order')
    list_editable = ('sort_order',)
    # При желании — настройки для дерева (но может потребоваться Django MPTT и т.д.)