from django.shortcuts import render


def home_page(resquest):
    return render(resquest, 'home.html')
