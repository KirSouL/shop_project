from django.shortcuts import render
from catalog.models import Product, Category


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Shop Market',
        'title_info': 'Shop Market - это магазин сервисов. Пользуйтесь и получайте наслаждение.'

    }
    return render(request, 'catalog/home.html', context)


def category(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Категории продуктов',
    }
    return render(request, 'catalog/category.html', context)


def product(request, pk):
    product_list = Product.objects.get(pk=pk)
    context = {
        'object_list': product_list,
        'title': 'Продукт',
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя пользователя: {name},\n"
              f"Почта пользователя: {email},\n"
              f"Телефон пользователя: {phone},\n"
              f"Сообщение от пользователя: {message}")
    return render(request, 'catalog/contacts.html', context)
