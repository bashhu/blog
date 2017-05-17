#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,Http404
from .form import TaskForm,CommandForm
from .models import Command,Command_log
from django.shortcuts import render
from utils.salt_api import  Salt_base_api
import json
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.decorators import permission_required

# Create your views here.
#

def index(request):
    return render(request,'task_index.html',{})

#@permission_required('task.add_command',login_url='/users/')
class Task_listView(generic.ListView):
    ''' looking one blog page 
        try:
        task_list = Command.objects.all()
    except Command.DoesNotExist:
        raise Http404
    print task_list
    return render(request, 'task_list.html', {'task_list': task_list})'''
    model = Command
    template_name = 'task_list.html'
    context_object_name = 'task_list'

@login_required(login_url='/users/')
def Task_cmd(request):
    return render(request, "task_cmd.html", {})


@login_required(login_url='/users/')
def Task(request):
    if request.method == 'POST':  # 当提交表单时
        form = TaskForm(request.POST)  # form 包含提交的数据
        if form.is_valid():  # 如果提交的数据合法
            host = form.cleaned_data['host']
            salt_mod = form.cleaned_data['salt_mod']
            salt_parm = form.cleaned_data['salt_parm']
            s = Salt_base_api()
            parm='{ "client":"local","tgt":"%s","fun":"%s","arg":"%s"}'% (host, salt_mod, salt_parm)

            res=s.salt_req(parm,'')['return'][0]
            print res
            return render(request,"task_result.html",{ 'result': res[host]})
    else:  # 当正常访问时
        form = TaskForm()
    return render(request, 'task_result.html', {'form': form})




@login_required(login_url='/users/')
def Task_log_list(request, id):
    ''' looking one blog page '''
    try:
        task_log_list =  Command_log.objects.filter(task_id__iexact = id)
    except Command_log.DoesNotExist:
        raise Http404
    return render(request, 'task_log_list.html', {'task_log_list': task_log_list})

@login_required(login_url='/users/')
def Task_log(request, id):
    ''' looking one blog page '''
    try:
        task_log =  Command_log.objects.get(id__iexact = id)
    except Command_log.DoesNotExist:
        raise Http404
    task_result = json.loads(task_log.salt_res)[task_log.salt_host]
    return render(request, 'task_log.html', {'task_log': task_log,'task_result': task_result})


def Task_save_log(task_id, salt_parm, reason, res):
    cmd = Command.objects.get(id=task_id)
    cmd_name = cmd.cmd_name
    cmd_cate = cmd.cmd_cate
    salt_host = cmd.salt_host
    salt_mod = cmd.salt_mod
    salt_reason = reason
    cmd_log = Command_log.objects.create(task_id=task_id, cmd_name=cmd_name, cmd_cate=cmd_cate, salt_host=salt_host, salt_mod=salt_mod, salt_parm=salt_parm, salt_reason=salt_reason, salt_res=res)
    cmd_log.save()


@permission_required('task.add_command',login_url='/users/')
def Task_exec(request,id):
    cmd = Command.objects.get(id=id)
    if request.method == 'POST':  # 当提交表单时
        form = CommandForm(request.POST)  # form 包含提交的数据
        print form
        if form.is_valid():  # 如果提交的数据合法
            host = cmd.salt_host
            salt_mod = cmd.salt_mod
            salt_parm = form.cleaned_data['salt_parm']
            reason =  form.cleaned_data['salt_reason']
            s = Salt_base_api()
            parm='{ "client":"local","tgt":"%s","fun":"%s","arg":"%s"}'% (host, salt_mod, salt_parm)
            res=s.salt_req(parm,'')['return'][0]
            Task_save_log(task_id=id, salt_parm=salt_parm, reason=reason, res=json.dumps(res))
            return render(request,"task_result.html",{ 'result': res[host]})
    else:  # 当正常访问时
        return render(request, "task_result.html", {'result': 'parm is err'})
    return render(request, 'task_result.html', {'form': form})


@permission_required('task.add_command',login_url='/users/')
def Cmd_online(request):
    if request.method == 'POST':  # 当提交表单时
        form = TaskForm(request.POST)  # form 包含提交的数据
        print request
        if form.is_valid():  # 如果提交的数据合法
            host = form.cleaned_data['host']
            salt_mod = form.cleaned_data['salt_mod']
            salt_parm = form.cleaned_data['salt_parm']
            s = Salt_base_api()
            parm='{ "client":"local","tgt":"%s","fun":"%s","arg":"%s"}'% (host, salt_mod, salt_parm)
            res=s.salt_req(parm,'')['return'][0]
            reason = 'cmd run with admin'
            id=1
            print id,salt_parm,reason,res
            Task_save_log(task_id=id, salt_parm=salt_parm, reason=reason, res=json.dumps(res))
            #return HttpResponse(json.dumps(res))
            return render(request,"task_result.html",{ 'result': res[host]})
    else:  # 当正常访问时
        return render(request, "task_result.html", {'result': 'parm is err'})
    return render(request, 'task_result.html', {'form': form})