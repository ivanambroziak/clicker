from django.db import models

class ClickerImage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва")
    image = models.ImageField(upload_to='clicker_images/', verbose_name="Фотографія")
    click_count = models.IntegerField(default=0, verbose_name="Кількість кліків")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Картинка для клікера"
        verbose_name_plural = "Картинки для клікера"

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    text = models.TextField(verbose_name="Коментар")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name}: {self.text[:50]}"