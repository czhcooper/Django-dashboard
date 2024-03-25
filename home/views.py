from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.contrib import messages
from .models import rnaseq
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html') 


# Dashboard
@login_required
def dashboard(request):
  context = {
    'segment': 'dashboard'
  }
  return render(request, 'pages/dashboard/dashboard.html', context)

# Pipeline
def pipeline_16S(request):
  context = {
    'parent': 'pipeline',
    'segment': 'pipeline_16S',
  }
  return render(request, 'pages/pipeline/pipeline_16S.html', context)


from .forms import UpModelForm

@login_required
def pipeline_rnaseq(request):
    

    if request.method == 'POST':
        file = request.FILES.get('file')  # 与Dropzone的paramName相匹配
        
        if file:
            # 构建文件的完整路径
            file_full_path = os.path.join(settings.MEDIA_ROOT, f"rnaseq/{request.user.username}/{file.name}")
            
            # 检查文件是否存在，如果存在，则删除
            if default_storage.exists(file_full_path):
                default_storage.delete(file_full_path)
                    
        if file:
            # 保存文件
            file_path = default_storage.save(f"rnaseq/{request.user.username}/{file.name}", file)
            # 创建rnaseq实例并保存到数据库
            #print(request.user.username)
            #print(request.FILES)
            rnaseq_instance = rnaseq(user=request.user, user_name=request.user.username,file_path=file_path)
            rnaseq_instance.save()

  
    context = {
        'parent': 'pipeline',
        'segment': 'pipeline_rnaseq',
        'username': request.user.username,
    }

    return render(request, 'pages/pipeline/pipeline_rnaseq.html', context)

# run ranseq
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
@csrf_exempt
def run_analysis_rnaseq(request):
    if request.method == 'POST':
        # 进行数据校验...
        data_valid = True  # 假设校验结果

        if data_valid:
            try:
                # 指定 Conda 环境名称
                conda_env_name = "rasflow"
                # Python 脚本的文件名
                script_name = "main.py"
                # 指定脚本运行的目录
                script_dir = "/Users/cooper/Documents/django/biopanel/workflow/RASflow"

                # 使用 conda run 命令在指定的环境中运行脚本，注意 cwd 参数的使用
                command = f"conda run -n {conda_env_name} python {script_name}"
                
                # 使用 subprocess.run 执行命令，并指定 cwd 参数
                result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=script_dir)

                if result.returncode == 0:
                    return JsonResponse({'status': 'success', 'message': '数据分析任务启动成功'}, status=200)
                else:
                    # 如果有错误，包括 stderr 在内的错误信息
                    error_message = result.stderr
                    return JsonResponse({'status': 'error', 'message': f'数据分析任务启动失败: {error_message}'}, status=500)
            except subprocess.CalledProcessError as e:
                # 包括 stderr 在内的错误信息
                error_message = e.stderr
                return JsonResponse({'status': 'error', 'message': f'数据分析任务执行错误: {error_message}'}, status=500)
        else:
            return JsonResponse({'status': 'error', 'message': '数据校验失败'}, status=400)





#测试
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.contrib import messages
from .models import rnaseq
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os

@login_required
def test(request):
    if request.method == 'POST':
        file = request.FILES.get('file')  # 与Dropzone的paramName相匹配
        
        if file:
            # 构建文件的完整路径
            file_full_path = os.path.join(settings.MEDIA_ROOT, f"rnaseq/{request.user.username}/{file.name}")
            
            # 检查文件是否存在，如果存在，则删除
            if default_storage.exists(file_full_path):
                default_storage.delete(file_full_path)
                    
        if file:
            # 保存文件
            file_path = default_storage.save(f"rnaseq/{request.user.username}/{file.name}", file)
            # 创建rnaseq实例并保存到数据库
            print(request.user.username)
            #print(request.FILES)
            rnaseq_instance = rnaseq(user=request.user, user_name=request.user.username,file_path=file_path)
            rnaseq_instance.save()


    # 重定向回上传页面，或者返回到相应的页面
    return render(request,'pages/pipeline/test.html')  


