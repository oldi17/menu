from django.contrib import admin
from django.forms import ModelForm
from .models import Menu, Item

# @admin.register(Item)
# class MenuItemAdmin(admin.ModelAdmin):
#     list_display = ('title', 'parent',)
#     list_filter = ('menu__title',)
#     # fieldsets = [
#     #     ( None, 
#     #         {
#     #             'fields': (
#     #                 'menu', 
#     #                 'parent', 
#     #                 'title',
#     #                 )
#     #         }
#     #     ),
#     # ]

#     def get_form(self, request, obj=None, **kwargs):
#         if obj: # obj is not None, so this is a change page
#             kwargs['exclude'] = ['menu', ]
#         return super(MenuItemAdmin, self).get_form(request, obj, **kwargs)

class MenuItemInline(admin.TabularInline):
    model = Item

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    list_display = ('title', )