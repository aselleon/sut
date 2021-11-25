from django.shortcuts import render

# Create your views here.

def course_info(request):
    return render(request, 'shop/course_info.html', {})

def dev_contacts(request):
    address = 'улица Манаса 8, Алматы 050000'
    dev_list = ({'name': 'Assel Orynbassar', 'phone': '+7 (777) 777-77-77', 'email': '28308@iitu.edu.kz', 'hours': '08:00 AM - 6:00 PM'},
                {'name': 'Muratbekuly Beket', 'phone': '+7 (777) 777-77-88', 'email': '27214@iitu.edu.kz', 'hours': '08:00 AM - 6:00 PM'})
    return render(request, 'shop/dev_contacts.html', context={'devs': dev_list, 'address': address})
    #return render(request, 'shop/dev_contacts.html', {})

def team_members(request):
    return render(request, 'shop/team_members.html', {})

def catalogue(request):
    catalogue_item = ({'id': 'curtnirimshik' , 'p': 'Курт & Иримшик' , 'src': '/static/images/Group 6892.svg'})
    return render(request, 'shop/indexcat.html', {})

def main_page(request):
    catalogue_item = ({'id': 'curtnirimshik' , 'p': 'Курт & Иримшик' , 'src': '/static/images/Group 6892.svg'})
    return render(request, 'shop/index.html', context={'items': catalogue_item})

def login_page(request):
    return render(request, 'shop/login.html', {})

def indexcat(request):
    return render(request, 'shop/indexcat.html', {})


from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all() #получить только доступные продукты
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/indexcat.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/catalogue.html',
                  {'product': product})