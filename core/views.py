from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import login as auth_login
from .forms import RegisterForm
from .models import Documento
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
import re
from django.contrib.auth import logout
from django.shortcuts import redirect

def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        password = request.POST.get("password")

        # limpar CPF (aceita com ou sem pontuação)
        cpf_digits = re.sub(r'\D', '', cpf or '')

        # autenticar
        user = authenticate(request, username=cpf_digits, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect("home")
            else:
                messages.error(request, "Sua conta ainda não foi aprovada pelo administrador.")
                return redirect("login")

        # se user is None:
        messages.error(request, "CPF ou senha incorretos.")
        return redirect("login")

    return render(request, "core/login.html")

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if not form.is_valid():
                print("RegisterForm errors:", form.errors)   # <-- debug: ver erros no terminal

        if form.is_valid():
            user = form.save()
            # opcional: adicionar ao grupo Pending
            pending, _ = Group.objects.get_or_create(name='Pending')
            user.groups.add(pending)
            messages.success(request, "Cadastro realizado. Aguarde aprovação do administrador.")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def upload_view(request):
    # apenas Uploader
    if not request.user.groups.filter(name='Uploader').exists():
        return HttpResponseForbidden("Apenas técnicos aprovados podem enviar documentos.")

    if request.method == 'POST':
        titulo = request.POST.get('titulo') or request.POST.get('title') or ''
        arquivo = request.FILES.get('arquivo')
        if not titulo or not arquivo:
            messages.error(request, "Preencha título e selecione arquivo.")
            return redirect('upload')
        doc = Documento.objects.create(
            titulo=titulo,
            arquivo=arquivo,
            criado_por=request.user
        )
        # extrair texto (sincronamente aqui, ou criar tarefa async depois)
        try:
            from .utils import extract_text_from_pdf
            texto = extract_text_from_pdf(doc.arquivo.path)
            doc.texto_extraido = texto
            doc.save()
        except Exception as e:
            # logar erro
            print("Erro extração:", e)
        messages.success(request, "Documento enviado.")
        return redirect('upload')

    documentos = Documento.objects.filter(criado_por=request.user).order_by('-criado_em')
    return render(request, 'core/upload.html', {'documentos': documentos})

@login_required
def delete_document(request, pk):
    if request.method == 'POST':
        doc = get_object_or_404(Documento, pk=pk, criado_por=request.user)
        doc.arquivo.delete(save=False)
        doc.delete()
        messages.success(request, "Documento excluído.")
    return redirect('upload')

def document_detail(request, pk):
    return render(request, 'core/document_detail.html', {'pk': pk})

def search_view(request):
    return render(request, 'core/search.html')

def resumo_view(request, pk):
    return render(request, 'core/resumo.html', {'pk': pk})

def chat(request):
    return render(request, 'core/chat.html')

def logout_view(request):
    # Para protótipo: aceitaremos GET e POST e sempre deslogamos e redirecionamos
    logout(request)
    messages.info(request, "Você saiu do sistema.")
    return redirect('home')
