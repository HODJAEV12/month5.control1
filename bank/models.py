from django.db import models

class Checks(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    author = models.CharField(max_length=50, verbose_name="Автор")
    check_number = models.CharField(max_length=100, verbose_name="Номер счета")
    money = models.IntegerField(max_length=100, verbose_name="Баланс")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"