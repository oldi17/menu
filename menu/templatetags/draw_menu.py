from django import template

from menu.models import Item
from django.template.context import RequestContext

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context: RequestContext, menu: str):
    result = {'title': menu,}

    if context.request.GET.get('menu', None) == menu:
        items = list(Item.objects.filter(menu__title=menu).values())
        selected_id = int(context.request.GET.get('item_id', -1))
        result['items'] = getTreeStructure(items, selected_id)
    return result

def getTreeStructure(items: [Item], selected_id: int):
    if selected_id == -1:
        return getItemsByParentID(items)
    
    selected_item = next(iter(getItemsByParentID(items, selected_id)), None) \
        or getItemByID(items, selected_id)
    
    if selected_item:
        return getParentsAndNeighbors(items, selected_item)
    return getItemsByParentID(items)

def getParentsAndNeighbors(items: [Item], selected_item: Item) -> [int]:
    selected_item_neighbors = getItemsByParentID(items, selected_item['parent_id'])
    if selected_item['parent_id'] == None:
        return selected_item_neighbors
    parent = getItemByID(items, selected_item['parent_id'])
    parent['children'] = selected_item_neighbors
    return getParentsAndNeighbors(items, parent)

def getNeighbors(items: [Item], selected_item: Item):
    return [item for item in items if item['parent_id'] == selected_item['parent_id']]

def getItemByID(items: [Item], id: int):
    return next((item for item in items if item['id'] == id), None)

def getItemsByParentID(items: [Item], parent_id: int = None):
    return [item for item in items if item['parent_id'] == parent_id]