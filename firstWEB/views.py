from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers

# Create your views here.
def index(request):
    return render(request,'index.html')
def calPage(request):
    return render(request,"cal.html")
def calucate(request):
    value_a=request.POST['valueA']
    value_b=request.POST['valueB']
    result=int(value_a)+int(value_b)
    print(int(value_a),int(value_b))
    return render(request,"result.html",context={'data':result})
def input_page(request):
    return render(request,"input_page.html")

def calculate_result(request):
    input_text=request.POST['input_text']
    print(input_text)
    return render(request,'calculate_result.html',context={'input_text':input_text,'out_result':15})
def navigation(request):
    return render(request,'navigation.html')
def summary(request):
    return JsonResponse({'namd':"kjkkkkgklgkl"})
