import re
import pandas as pd

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from pyecharts import options as opts
from pyecharts.charts import Bar

import base64

import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Bar
from pyecharts import options as opts


# Create your views here.
def index(request):
    return render(request, 'index.html')


def calPage(request):
    return render(request, "cal.html")


def calucate(request):
    value_a = request.POST['valueA']
    value_b = request.POST['valueB']
    result = int(value_a) + int(value_b)
    print(int(value_a), int(value_b))
    return render(request, "result.html", context={'data': result})


def input_page(request):
    return render(request, "input_page.html")


def calculate_result(request):
    input_text = request.POST['input_text']
    print(input_text)
    return render(request, 'calculate_result.html', context={'input_text': input_text, 'out_result': 15})


def navigation(request):
    return render(request, 'navigation.html')


def summary(request):
    return JsonResponse({'namd': "kjkkkkgklgkl"})


import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


def table(request):
    # return render(request,'table.html')
    df = pd.read_excel("/Users/liujun/Downloads/2019级工程管理1班课表.xlsx")
    context = {
        'data_stream': df.to_html()
    }
    return render(request, 'table.html', context)
    # df = pd.read_excel("/Users/liujun/Downloads/2019级工程管理1班课表.xlsx")
    # excel_file=open("/Users/liujun/Downloads/2019级工程管理1班课表.xlsx","rb+")
    # input_stream=excel_file.read()
    # input_stream = read_into_buffer("/Users/liujun/Downloads/2019级工程管理1班课表.xlsx")
    # return render(request, 'table.html', context={"data_stream": input_stream})


def bar_chart(request):
    bar = Bar()
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
    bar.render("./firstWEB/templates/test12.html")
    return render(request, 'test12.html')
    # bar.render()


# def line_chart(request):


def chart(request):
    return render(request, 'chart.html')


def img_show(request):
    return render(request, "img_test.html")
