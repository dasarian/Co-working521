from django.shortcuts import render

def show_main_page(request):
    apartments_list = [
        {'address': 'ул. Ленина, д. 10', 'price': '25 000 руб./мес.'},
        {'address': 'пр. Мира, д. 45', 'price': '32 000 руб./мес.'},
        {'address': 'ул. Садовая, д. 8', 'price': '28 500 руб./мес.'},
        {'address': 'пер. Строителей, д. 3', 'price': '22 000 руб./мес.'},
        {'address': 'ул. Цветочная, д. 15', 'price': '35 000 руб./мес.'},
    ]

    context = {
        'apartments': apartments_list
    }

    return render(request, 'main/index.html', context)