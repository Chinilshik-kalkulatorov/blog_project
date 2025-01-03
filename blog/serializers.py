from rest_framework import serializers
from .models import Article, MenuItem

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class MenuItemChildSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'description', 'children']

    def get_children(self, obj):
        qs = obj.children.order_by('sort_order')
        return MenuItemChildSerializer(qs, many=True).data