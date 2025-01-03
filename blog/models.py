from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    full_text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)

    class Meta:
        ordering = ['-created_at']  # <-- убывающая сортировка по дате
    
    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children'
    )
    # текст, который редактируется в CKEditor
    description = RichTextField(blank=True, null=True)

    # можно добавить поле для сортировки
    sort_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title