from django.shortcuts import render,HttpResponse
from Hello_World import views

def Hello(request):
    return HttpResponse("<h1>Hello World</h1>\n Este é o meu primeiro projeto com django e python")

def Soma(request, num1, num2):
    soma = num1 + num2
    return HttpResponse(f'A soma dos números é {soma}')

def Divisao(request, num1, num2):
    divisao = num1/num2
    return HttpResponse('A divisão é '+format(divisao))
    
def Multi(request, num1, num2):
    multi = num1 * num2
    return HttpResponse(f'A multiplicação dos números é {multi}')
