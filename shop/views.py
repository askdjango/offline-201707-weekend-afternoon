from django.shortcuts import redirect, render
from .models import Item
from .forms import ItemForm


def item_list(request):
    return render(request, 'shop/item_list.html', {
        'item_list': Item.objects.all(),
    })


def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })


def item_new(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect(item)
    else:
        form = ItemForm()
    return render(request, 'shop/item_form.html', {
        'form': form,
    })


def item_edit(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(item)
    else:
        form = ItemForm(instance=item)
    return render(request, 'shop/item_form.html', {
        'form': form,
    })


def item_delete(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('shop:item_list')
    return render(request, 'shop/item_confirm_delete.html', {
        'item': item,
    })

