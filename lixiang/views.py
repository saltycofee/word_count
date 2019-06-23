from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request, 'lixiang/home.html')
    # return HttpResponse('hello world!')


def count(request):
    response_dic = {}
    text = request.GET['text']
    total_count = len(text)
    response_dic['count_num'] = total_count
    response_dic['txt'] = text
    txt_dic = {}
    for word in text:
        if word not in txt_dic:
            txt_dic[word] = 1
        else:
            txt_dic[word] += 1
    txt_list = sorted(txt_dic.items(),key=lambda w:w[1], reverse=True)
    response_dic['txt_dic'] = txt_list
    return render(request,'lixiang/count.html', response_dic)