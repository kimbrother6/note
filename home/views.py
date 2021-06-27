from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home/home.html')

def m(request):
    return render(request, 'home/base.html')