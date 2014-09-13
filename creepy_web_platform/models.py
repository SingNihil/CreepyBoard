# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"Название категории")
    description = models.TextField(verbose_name=u"Описание категории")

    class Meta:
        verbose_name=u"Категория"
        verbose_name_plural=u"Категории"

    def __unicode__(self):
        return  self.title

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name=u"Название тега")

    class Meta:
        verbose_name=u"Тег"
        verbose_name_plural=u"Теги"

    def __unicode__(self):
        return  self.title

class Post(models.Model):
    user = models.ForeignKey(User, verbose_name=u"Автор записи")
    date = models.DateTimeField(auto_now_add=True, verbose_name=u"Время создания записи")
    category = models.ForeignKey(Category, verbose_name=u"Категория записи")
    title = models.CharField(max_length=100, verbose_name=u"Заголовок записи")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u"Теги записи")
    reply_for = models.ForeignKey('self' ,blank=True, verbose_name=u"Ответ на")
    content = models.TextField(verbose_name=u"Содержание записи")
    views = models.IntegerField(verbose_name=u"Колличество просмотров")
    rating = models.IntegerField(default=0,verbose_name=u"Рейтинг записи")
    image = models.ImageField(upload_to=u"images",blank=True, verbose_name=u"Прикрепленное изображение")

    class Meta:
        verbose_name=u"Запись"
        verbose_name_plural=u"Записи"

    def __unicode__(self):
        return  u"[%s](%s) %s" %(self.date, self.user, self.title)

