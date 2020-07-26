from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')

def firstyear(request):
    return render(request,'firstyear.html')

def secondyear(request):
    return render(request,'secondyear.html')

def civil(request):
    return render(request,'civil.html')

def Chemical(request):
    return render(request,'Chemical.html')

def Biotech(request):
    return render(request,'Biotech.html')

def CS(request):
    return render(request,'CS.html')

def Eandcomm(request):
    return render(request,'Eandcomm.html')

def Eandcomp(request):
    return render(request,'Eandcomp.html')

def EandIn(request):
    return render(request,'EandIn.html')

def electrical(request):
    return render(request,'electrical.html')

def Mechanical(request):
    return render(request,'Mechanical.html')

def Mechatronics(request):
    return render(request,'Mechatronics.html')

def Production(request):
    return render(request,'Production.html')

def cpp(request):
    return render(request,'c++.html')

def c(request):
    return render(request,'c.html')

def chem(request):
    return render(request,'chem.html')

def ed(request):
    return render(request,'ed.html')

def electrical1(request):
    return render(request,'electrical1.html')

def mechanics(request):
    return render(request,'mechanics.html')

def physics(request):
    return render(request,'physics.html')

def proffComm(request):
    return render(request,'proffComm.html')

def maths(request):
    return render(request,'maths.html')

def maths2(request):
    return render(request,'maths2.html')

def electronics(request):
    return render(request,'electronics.html')

def engDesign1(request):
    return render(request,'engDesign1.html')

def environment(request):
    return render(request,'environment.html')                                                    
