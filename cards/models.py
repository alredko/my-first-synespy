from django.db import models

class Word(models.Model):

    num = models.PositiveIntegerField("№ пп")
    word = models.CharField("Слово", max_length=20)
    imagew = models.ImageField("Образ слова", upload_to='cards/')
    soundw = models.FileField("Звучание слова", upload_to='files/')
    transcr = models.CharField("Транскрипция", max_length=20)
    imaget = models.ImageField("Образ звучания", upload_to='cards/')
    association = models.CharField("Ассоциация", max_length=20)
    interpret = models.CharField("Перевод", max_length=20)
    example1 = models.CharField("Пример 1", max_length=200)
    sounde1 = models.FileField("Озвучка Пр1", upload_to='files/')
    example2 = models.CharField("Пример 2", max_length=200)
    sounde2 = models.FileField("Озвучка Пр2", upload_to='files/')
    explain = models.TextField("Пояснение")

    def __str__(self):
        return self.word
