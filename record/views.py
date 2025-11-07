from django.shortcuts import render

def record_main_page(request):
    return render(request, 'record/index.html')
