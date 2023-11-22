from django.contrib import admin
from .models import Menu, Item

class MenuItemInline(admin.TabularInline):
    model = Item

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    list_display = ('title', )