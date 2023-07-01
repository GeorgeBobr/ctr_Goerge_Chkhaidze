from django.db import models
Status = [('active', 'Активно'), ('blocked', 'Заблокировано')]
class Book(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="Автор", default="Неизвестный")
    email = models.EmailField()
    text = models.TextField(max_length=2000, verbose_name="Контент")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=50, choices=Status, default='active', verbose_name='Статус')

    def __str__(self):
        return f"{self.id} {self.author}: {self.email}"

    class Meta:
        db_table = "Book"
        verbose_name = "Гостевая книга"
        verbose_name_plural = "Гостевые книги"