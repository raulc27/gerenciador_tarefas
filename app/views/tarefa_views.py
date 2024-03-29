# Create your views here.
from django.shortcuts import render, redirect
from ..forms import TarefaForm
from ..entidades.tarefa import Tarefa
from ..services import tarefa_service


def listar_tarefas(request):
    tarefas=tarefa_service.listar_tarefas()
    return render(request, 'tarefas/listar_tarefas.html', {"tarefas": tarefas})

    nome_tarefa = "Assistir a Semana Python e Django da TreinaWeb"
    return render(request,'tarefas/listar_tarefas.html',{"nome_tarefa":nome_tarefa})

def cadastrar_tarefa(request):
    if request.method=="POST":
        form_tarefa=TarefaForm(request.POST)
        if form_tarefa.is_valid():
            titulo=form_tarefa.cleaned_data["titulo"]
            descricao = form_tarefa.cleaned_data["descricao"]
            data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
            prioridade = form_tarefa.cleaned_data["prioridade"]

            tarefa_nova = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, prioridade=prioridade)

            tarefa_service.cadastrar_tarefa(tarefa_nova)

            return redirect('listar_tarefas')
    else:
        form_tarefa=TarefaForm()

    return render(request,'tarefas/form_tarefa.html',{"form_tarefa":form_tarefa})



def editar_tarefa(request, id):
    tarefa_bd=tarefa_service.listar_tarefa_id(id)
    form_tarefa=TarefaForm(request.POST or None, instance=tarefa_bd)
    if form.tarefa.is_valid():
        titulo = form_tarefa.cleaned_data["titulo"]
        descricao = form_tarefa.cleaned_data["descricao"]
        data_expiracao = form_tarefa.cleaned_data["data_expiracao"]
        prioridade = form_tarefa.cleaned_data["prioridade"]

        tarefa_nova = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, prioridade=prioridade)

        tarefa_service.editar_tarefa(tarefa_bd, tarefa_nova)

        return redirect('listar_tarefas')

    return render(request, 'tarefas/form_tarefa.html', {"form_tarefa": form_tarefa})


def remover_tarefa(request, id):
    tarefa_bd=tarefa_service.listar_tarefa_id(id)
    if request_method == "POST":
        tarefa_service.remover_tarefa(tarefa_bd)
        return redirect ('listar_tarefas')
    return render(request, 'tarefas/confirma_exclusao.html', {'tarefa': tarefa_bd})
