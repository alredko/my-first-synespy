from django.db import models

STATUS_CHOICES = (
    ('NEW', 'New'),
    ('TOURIST', 'Tourist'),
    ('IMMIGRANT', 'Immigrant'),
    ('ABORIGINE', 'Aborigine'),
)

class User(models.Model):

    name = models.CharField("Имя", max_length=50)
    email = models.EmailField("E-Mail", max_length=50)
    status = models.CharField("Статус", max_length=10)
    progress = models.CharField("Порядок карточек", max_length=10)
    created_date = models.DateTimeField('Время регистрации')

    def __str__(self):
        return self.name
