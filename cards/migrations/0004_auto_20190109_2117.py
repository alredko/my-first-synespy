# Generated by Django 2.1.4 on 2019-01-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20190102_1043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['num', 'word', 'interpret']},
        ),
        migrations.AlterField(
            model_name='word',
            name='example1',
            field=models.CharField(max_length=200, verbose_name='Пример 1'),
        ),
        migrations.AlterField(
            model_name='word',
            name='example2',
            field=models.CharField(max_length=200, verbose_name='Пример 2'),
        ),
        migrations.AlterField(
            model_name='word',
            name='num',
            field=models.PositiveIntegerField(verbose_name='№ пп'),
        ),
        migrations.AlterField(
            model_name='word',
            name='sounde1',
            field=models.FilePathField(path='files/', verbose_name='Озвучка Пр1'),
        ),
        migrations.AlterField(
            model_name='word',
            name='sounde2',
            field=models.FilePathField(path='files/', verbose_name='Озвучка Пр2'),
        ),
        migrations.AlterField(
            model_name='word',
            name='soundw',
            field=models.FilePathField(path='files/', verbose_name='Озвучка Пр1'),
        ),
    ]
