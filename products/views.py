from django.shortcuts import render


def index(request, page=1, category="Allgemein"):
    return render(request, 'products/index.html')