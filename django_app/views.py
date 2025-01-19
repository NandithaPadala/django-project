from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def result(request):
    num1 = int(request.POST['number1']) 
    num2 = int(request.POST['number2'])
    if request.POST.get('add') == "": 
        ans = num1 + num2
    elif request.POST.get('subtract') == "":
        ans = num1 - num2

    elif request.POST.get('multiply') == "":
        ans = num1 * num2

    else: 
        ans = num1 / num2

    return render(request, 'result.html', {'ans': ans})

def index(request):
    return render(request,'index.html', {'name' : 'Nanditha'})