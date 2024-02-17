from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login as django_login
from django.views.decorators.csrf import csrf_exempt
from .models import User
# from .model import analyze_text
from django.contrib import messages
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\
import torch
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
import torch.nn.functional as F
from transformers import BertTokenizer, BertConfig,AdamW, BertForSequenceClassification,get_linear_schedule_with_warmup
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.metrics import accuracy_score,matthews_corrcoef
from tqdm import tqdm, trange,tnrange,tqdm_notebook
from sklearn.preprocessing import LabelEncoder
from ctransformers import AutoModelForCausalLM
from django.apps import apps     



def render_home_window(request):
    return render(request, "main/index.html")

def render_about_window(request):
    return render(request, "main/about.html")

def render_service_window(request):
    return render(request, "main/service.html")

def render_team_window(request):
    return render(request, "main/team.html")

def render_why_window(request):
    return render(request, "main/why.html")    

def render_main_window(request):
    return render(request, "main/main.html")    

def render_signin_window(request):
    return render(request, "main/signin.html")   

def render_signup_window(request):
    return render(request, "main/signup.html")

def register(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            c_password = request.POST['c_password']
            if password == c_password:
                user = User.objects.create(email=email, password=password)
                user.save()
                return render(request, 'main/signin.html')  # Перенаправление на страницу входа после регистрации
            else:
                messages.error(request, 'Passwords must be similar')
                return render(request, 'main/signup.html')  
        except:
            messages.error(request, 'Passwords must be similar')
            return render(request, 'main/signup.html')          
    else:
        return render(request, 'main/signup.html')

def login(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.get(email=email, password=password)
            print(user)
            if user is not None:
                django_login(request, user)
                return render(request, 'main/main.html')  # Перенаправление на главную страницу после входа
            else:
                messages.error(request, 'Incorrect email or password')
                return render(request, 'main/signin.html')
        except:
            messages.error(request, 'Incorrect email or password')
            return render(request, 'main/signin.html')    
    else:
        return render(request, 'main/signin.html')

@csrf_exempt
def recognize_person(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        print(f"inputted: {input_text}")
        try:
            llm = apps.get_app_config('main').llm
            system_prompt = "### System:\You are StableBeluga model and you are trying to help as much as you can to make user understand whether text is wrote by the predator or not.\n\n"
            message = f"Analyze this text and make an assumption whether this text look like message from child predator or not '{input_text}'. \
            \nThe answer should be like: I have analyzed this text. My assumptions: '<there you put your arguments>'"
            prompt = f"{system_prompt}### User: {message}\n\n### Assistant:\n"
            response = llm(prompt)
            return HttpResponse(response)
        except Exception as e:
            print(e)
            return "failed to process data"
    else:
        failed_response = f"failed response"
        return HttpResponse(failed_response)
 

