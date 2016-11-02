from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html', {})

def report(request):
    return render(request, 'report.html', {})

def setting(request):
    return render(request, 'setting.html', {})
