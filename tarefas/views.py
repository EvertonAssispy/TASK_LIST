from django.shortcuts import render, get_object_or_404, redirect
from .models import task
from .forms import Taskform
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

import datetime








@login_required
def tasks(request):
    '''pesquisa'''
    search = request.GET.get('search')
    
    filter = request.GET.get('filter')
    
    usuario = User.objects.all()
    
    taskdonerecently = task.objects.filter(done='done', 
        updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30),user=request.user).count()
    
    tasksdone = task.objects.filter(done='done',user=request.user).count()
    
    tasksdoing = task.objects.filter(done='doing',user=request.user).count()
    if search:
        '''usando o filter para literalmente filtrar os objetos do banco de acordo
        com os argumentos passados, usando USER igual ao user request que é o usuario ja autenticado.'''
        tasks = task.objects.filter(titulo__icontains=search, user=request.user)
        
        return render(request, 'tarefas.html', {'tasks': tasks})
    
    elif filter:
        
        tasks = task.objects.filter(done=filter, user=request.user)
    
        return render(request, 'tarefas.html', {'tasks': tasks, 'user':usuario})
        
        
    else:
        tasks_list = task.objects.all().order_by('-created_at').filter(user=request.user)
        
        '''VARIAVEL QUE RECEBE A CLASSE'''
        paginator = Paginator(tasks_list, 7)
        
        '''TEMOS QUE RECEBER O ARGUMENTO PAGE, ENTAO PEGAMOS COM GET
        E ASSOCIAMOS A UMA VARIAVEL, SO PRECISAMOS RESGATAR MESMO'''
        page = request.GET.get('page')
        
        '''PEGANDO A PAGINA ORIGINAL'''
        tasks = paginator.get_page(page)
        
        
        return render(request, 'tarefas.html', {'tasks': tasks, 'tasksrecently':taskdonerecently,'tasksdone':tasksdone,'tasksdoing':tasksdoing})

@login_required
def taskviews(request, id):
    tarefa = get_object_or_404(task, pk=id)
    return render(request, 'task.html', {'task': tarefa})
    
    
# adcionando dados ao banco de dados com front-end
@login_required
def nova_task(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        
        if form.is_valid():
            '''AQUI COLOCAREMOS A TASK EM DOING PARA FICAR PRE MARCADO COMO NAO FEITO, PARA O SERVIDOR 
            RODAR SEM ESSA CONFIGURACAO QUANDO O USUARIO FOR MODIFICAR UMA TAREFA'''
            task = form.save(commit=False)
            task.done = 'doing'
            
            '''usando USER igual ao user request que é o usuario ja autenticado.'''
            task.user = request.user
            
            
            task.save()
            return redirect('/')
        
        
    else:
        form = Taskform()
        return render (request, 'nova_task.html', {'form': form})
    
    
@login_required
def edittask(request, id):
    
    """TAREFA EM TODAS AS VIEWS É A VARIAVEL QUE PUXA OS DADOS DO BANCO, SENDO ASSIM
    "GET_OBJECT_OR_404" DIZ QUE SE O OBJETO INSTANCIADO NO PRIMARE KEY = ID
    NAO FOR ENCONTRADO ELE RETORNARÁ UMA MENSAGEM 404"""
    
    tarefa =get_object_or_404(task, pk=id)
    form = Taskform(instance=tarefa)
    
    if(request.method == 'POST'):
        form = Taskform(request.POST, instance=tarefa)
        
        if(form.is_valid()):
           tarefa.save()
           return redirect('/')
        else:
            return render(request, 'edittask.html', {'form': form, 'task': tarefa})
            
        
    else:
        
        return render(request, 'edittask.html', {'form': form, 'task': tarefa})
    
    
@login_required    
def deletetask(request, id):
    tarefa =get_object_or_404(task, pk=id)
    tarefa.delete()
    
    messages.info(request, 'tarefa deletada com sucesso!')
    
    return redirect('/')
  
  
@login_required
def changestatus(request, id):
    tarefa = get_object_or_404(task, pk=id)
    
    
    if(tarefa.done == 'doing'):
        tarefa.done = 'done'
    else:
        tarefa.done = 'doing'
    
    tarefa.save()
    
    return redirect('/')