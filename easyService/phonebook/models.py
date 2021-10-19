from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Department(models.Model):
    name = models.CharField(verbose_name=_("Название отдела"), max_length=40)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Название отдела'
        verbose_name_plural = 'Название отдела'


class MAN(models.Model):
    name = models.CharField(verbose_name=_("ФИО"), max_length=40)
    position = models.CharField(verbose_name=_("Должность"), max_length=40)
    department = models.ForeignKey(Department, verbose_name=_("Отдел"), on_delete=models.CASCADE, blank=True, null=True)
    tel = models.CharField(verbose_name=_("Вн. телефон"), max_length=40)
    mobtel = models.CharField(verbose_name=_("Моб. телефон"), max_length=40)
    cab = models.CharField(verbose_name=_("Кабинет"), max_length=40)
    email = models.CharField(verbose_name=_("Почтовый ящик"), max_length=40)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудник'