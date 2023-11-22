from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Все меню'
    
    def __str__(self):
        return self.title


class Item(models.Model):
    menu = models.ForeignKey(Menu, blank=True, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=255, verbose_name='Название')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.title