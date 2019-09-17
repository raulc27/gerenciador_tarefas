from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('listar_tarefas')
    return render(request, 'usuarios/form_usuario.html')

