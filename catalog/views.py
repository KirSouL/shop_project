from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя пользователя: {name},\n"
              f"Почта пользователя: {email},\n"
              f"Телефон пользователя: {phone},\n"
              f"Сообщение от пользователя: {message}")
    return render(request, 'catalog/contacts.html')
