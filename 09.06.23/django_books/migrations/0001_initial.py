# Generated by Django 4.2.2 on 2023-06-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books_tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='Аноним', max_length=200, verbose_name='Пользователь')),
                ('author', models.CharField(max_length=300, verbose_name='Автор книги')),
                ('book_name', models.CharField(max_length=300, verbose_name='Название книги')),
                ('category', models.CharField(max_length=300, verbose_name='Категория книги')),
                ('description', models.CharField(max_length=1000, verbose_name='Описание книги')),
            ],
            options={
                'verbose_name': 'Таблица с книгами',
                'ordering': ('book_name', 'author'),
            },
        ),
    ]
