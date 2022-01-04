from django.shortcuts import render, get_object_or_404
from .models import Motorcycle
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def motorcycle(request):
    motorcycle = Motorcycle.objects.order_by('-created_date')
    paginator = Paginator(motorcycle,4)
    page = request.GET.get('page')
    paged_motorcycle = paginator.get_page(page)
    manufacture_search = Motorcycle.objects.values_list('manufacture', flat=True).distinct()
    model_search = Motorcycle.objects.values_list('model', flat=True).distinct()
    year_search = Motorcycle.objects.values_list('year', flat=True).distinct()
    data = {
        'motorcycle': paged_motorcycle,
        'manufacture_search' : manufacture_search,
        'model_search' : model_search,
        'year_search' : year_search,
    }
    return render(request, 'motorcycle/motorcycle.html', data)

def motorcycle_detail(request, id):
    single_motorcycle = get_object_or_404(Motorcycle, pk=id)

    data={
        'single_motorcycle': single_motorcycle,
    }
    return render(request, 'motorcycle/motorcycle_detail.html', data)

def search(request):
    motorcycle = Motorcycle.objects.order_by('-created_date')

    manufacture_search = Motorcycle.objects.values_list('manufacture', flat=True).distinct()
    model_search = Motorcycle.objects.values_list('model', flat=True).distinct()
    year_search = Motorcycle.objects.values_list('year', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            motorcycle = motorcycle.filter(motorcycle_title__icontains=keyword)
    if 'manufacture' in request.GET:
        manufacture = request.GET['manufacture']
        if manufacture:
            motorcycle = motorcycle.filter(manufacture__iexact=manufacture)
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            motorcycle = motorcycle.filter(model__iexact=model)
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            motorcycle = motorcycle.filter(year__iexact=year)
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            motorcycle = motorcycle.filter(price__gte=min_price, price__lte=max_price)
    data = {
        'motorcycle': motorcycle,
        'manufacture_search' : manufacture_search,
        'model_search' : model_search,
        'year_search' : year_search,
    }
    return render(request, 'motorcycle/search.html', data)
