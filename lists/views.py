from django.shortcuts import render, redirect
from lists.models import Item


# Create your views here.
def home_page(request):
    """Домашняя страница"""
    # TODO потдержка более чем одного списка
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/one-of-a-kind-list-in-the-world/')
    return render(request, 'home.html')


def view_list(request):
    """Представление списка"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
