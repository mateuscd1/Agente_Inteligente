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
    # apenas técnicos aprovados
    if not request.user.groups.filter(name='Uploader').exists():
        return HttpResponseForbidden("Apenas técnicos PPG podem enviar documentos.")

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        arquivo = request.FILES.get("arquivo")

        if not titulo or not arquivo:
            messages.error(request, "Preencha o título e selecione um arquivo.")
            return redirect("upload")

        Documento.objects.create(
            titulo=titulo,
            arquivo=arquivo,
            criado_por=request.user
        )

        messages.success(request, "Documento enviado com sucesso!")
        return redirect("upload")

    documentos = Documento.objects.filter(criado_por=request.user).order_by("-criado_em")

    return render(request, "core/upload.html", {
        "documentos": documentos
    })

@login_required
def editar_documento(request, doc_id):
    documento = get_object_or_404(Documento, id=doc_id, criado_por=request.user)

    if request.method == "POST":
        novo_titulo = request.POST.get("titulo")
        if novo_titulo:
            documento.titulo = novo_titulo
            documento.save()
            messages.success(request, "Título atualizado com sucesso.")
            return redirect("upload")

    return render(request, "core/editar_documento.html", {
        "documento": documento
    })


@login_required
def excluir_documento(request, doc_id):
    documento = get_object_or_404(Documento, id=doc_id, criado_por=request.user)

    if request.method == "POST":
        documento.arquivo.delete()  # remove o arquivo físico
        documento.delete()          # remove do banco
        messages.success(request, "Documento excluído com sucesso.")
        return redirect("upload")

    return render(request, "core/excluir_documento.html", {
        "documento": documento
    })

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
