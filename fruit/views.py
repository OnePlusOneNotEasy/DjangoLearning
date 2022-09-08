from django.shortcuts import render, get_object_or_404, redirect
from .models import Fruit
from .forms import FruitForm, RawFruitForm
from django.http import Http404

# Create your views here.
def fruit_detail_view(request, my_id):
    # obj = Fruit.objects.get(id=my_id)
    # obj = get_object_or_404(Fruit, id=my_id)
    try:
        obj = Fruit.objects.get(id=my_id)
    except Fruit.DoesNotExist:
        raise Http404
    # context = {
    #     'title':obj.title,
    #     'description':obj.description
    # }
    context = {
        "obj":obj
    }
    return render(request, "fruits/detail.html", context)

def fruit_create_view(request):
    # obj = Fruit.objects.get(id=1)
    initial = {
        'title':'apple',
        'description':'delicious'
    }
    form = FruitForm(request.POST or None, initial=initial)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, 'fruits/create.html', context)

def fruit_delete_view(request, my_id):
    obj = get_object_or_404(Fruit, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../../")
    context = {
        "object":obj
    }
    return render(request, 'fruits/delete.html', context)

def fruit_list_view(request):
    queryset = Fruit.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, 'fruits/list.html', context)
# def fruit_create_view(request):
#     # print(request.GET['title'])
#     # print(request.POST)
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Fruit.objects.create(title=my_new_title)
#     context = {}
#     return render(request, 'fruits/create.html', context)

# def fruit_create_view(request):
#     my_form = RawFruitForm()
#     if request.method == 'POST':
#         my_form = RawFruitForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#     return render(request, 'fruits/create.html', context)
