from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    return render(request, 'core/login.html')

def register_view(request):
    return render(request, 'core/register.html')

def upload_view(request):
    return render(request, 'core/upload.html')

def document_detail(request, pk):
    return render(request, 'core/document_detail.html', {'pk': pk})

def search_view(request):
    return render(request, 'core/search.html')

def resumo_view(request, pk):
    return render(request, 'core/resumo.html', {'pk': pk})
