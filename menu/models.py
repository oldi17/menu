from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Все меню'
    
    def __str__(self):
        return self.title


class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', verbose_name='Меню')
    title = models.CharField(max_length=255, verbose_name='Название')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children', verbose_name='Родитель', )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.menu.title + " " + self.title
    
    def limit_parent_choises(self):
        pass