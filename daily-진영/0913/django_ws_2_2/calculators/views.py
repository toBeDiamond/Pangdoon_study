from django.shortcuts import render

# Create your views here.
def calculator(request, num1, num2):
    mult = num1 * num2
    minus = num1 - num2
    if num2 == 0:
        div = '계산할 수 없습니다.'
    else:
        div = num1 / num2

    context = {
        'num1': num1,
        'num2': num2,
        'mult': mult,
        'minus' : minus,
        'div' : div,
    }


    return render(request,'calculators/calculator.html', context)
