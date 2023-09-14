from django.shortcuts import render


def first(request):
    message = request.GET.get('message')
    # if not message:
    #     message = '아무것도 받지 못함'
    context = {
        'message' : message
    }
    return render(request,'throw_catch/first.html', context)

from django.shortcuts import render

def second(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request,'throw_catch/second.html', context)

