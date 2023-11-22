from django.contrib import admin
from .models import Menu, Item

@admin.register(Item)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent',)
    list_filter = ('menu',)
    fieldsets = (
        ('Добавить новый пункт', {
            'description': "Выберите меню. В качестве родителя может выступать ---(корневой пункт) либо другой пункт этого меню.",
            'fields': (
                ('menu', 'parent'), 
                'title',)
            }),
            )


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', )