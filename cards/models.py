from django.db import models

class Word(models.Model):

    num = models.PositiveIntegerField("№ пп")
    word = models.CharField("Слово", max_length=20)
    imagew = models.ImageField("Образ слова", upload_to='cards/')
    soundw = models.FilePathField("Озвучка Пр1", path="files/")
    transcr = models.CharField("Транскрипция", max_length=20)
    imaget = models.ImageField("Образ звучания", upload_to='cards/')
    association = models.CharField("Ассоциация", max_length=20)
    interpret = models.CharField("Перевод", max_length=20)
    example1 = models.CharField("Пример 1", max_length=200)
    sounde1 = models.FilePathField("Озвучка Пр1", path="files/")
    example2 = models.CharField("Пример 2", max_length=200)
    sounde2 = models.FilePathField("Озвучка Пр2", path="files/")
    explain = models.TextField("Пояснение")

    def __str__(self):
        return self.word
