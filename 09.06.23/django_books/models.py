from django.db import models

# Create your models here.
books_tab = """
create table Books
(
id int AUTOINCREMENT
username string (VARChar500)
author string (VARChar500)
book_name string (VARChar500)
category string (VARChar500)
description string (VARChar5000)
...
)
"""

user_tab = """
create table Users
(
id int AUTOINCREMENT
username string (VARChar500)
password string (VARChar500)
email string (VARChar500)
name string (VARChar500)
...
)
"""

class Books_tab(models.Model):
    username = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="Аноним",
        verbose_name="Пользователь",
        max_length=200
    )
    author=models.CharField("Автор книги", max_length=300)
    book_name=models.CharField("Название книги", max_length=300)
    category=models.CharField("Категория книги", max_length=300)
    description=models.CharField("Описание книги", max_length=1000)

    class Meta:
        app_label = "django_books"
        ordering = ("book_name", "author")
        verbose_name = "Таблица с книгами"

    def __str__(self):
        return f"{self.book_name} {self.author} {self.category} {self.username}"