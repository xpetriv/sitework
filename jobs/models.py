from django.db import models
from django.utils import timezone


class Articles(models.Model):
    title = models.CharField('Посада', max_length=50)
    city = models.CharField('Місто', max_length=50)
    full_text = models.TextField('Коротке резюме')
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/jobs/{self.id}'

    class Meta:
        verbose_name = 'Оголошення'    
        verbose_name_plural = 'Оголошення'

