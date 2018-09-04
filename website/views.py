from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'website/index.html')

def about_aipn(request):
    return render(request,'website/about_aipn.html')

def mission(request):
    return render(request,'website/mission.html')  

'''
def about_us(request):
    return render(request,'website/about_us.html')

def board(request):
    return render(request,'website/board.html')

def committees(request):
    return render(request,'website/committees.html')

def why_cfa(request):
    return render(request,'website/why_cfa.html')

def about_cfa(request):
    return render(request,'website/about_cfa.html')


def about_cipm(request):
    return render(request,'website/about_cipm.html')

def invetment_foundation(request):
    return render(request,'website/invetment_foundation.html') 

def exam_fees(request):
    return render(request,'website/exam_fees.html') 

'''    