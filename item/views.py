from django.shortcuts import render, get_object_or_404
from .models import Item, Category
from django.db.models import Q, Max

# Create your views here.

def items(request):
    shape_choices = Item.SHAPE_CHOICES
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    shape_id = request.GET.get('shape', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 0)

    if min_price:
        items = items.filter(price__gte=int(min_price))

    if max_price:
        items = items.filter(price__lte=int(max_price))

    if shape_id:
        items = items.filter(shape=shape_id)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))


    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'shape_id': shape_id,
        'shape_choices': shape_choices,
        'min_price': min_price,
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    similar = Item.objects.filter(is_sold=False, category=item.category).exclude(pk=pk)[0:4]
    # filter(category=item.category)

    return render(request, 'item/detail.html', {
        'item': item,
        'similar': similar,
    })