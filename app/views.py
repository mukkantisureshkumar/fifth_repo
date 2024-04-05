from django.shortcuts import render

# Create your views here.
def disney(request):
    return render(request,'disney.html')

def mikky(request):
    return render(request,'mikky.html')

def motu_patlu(request):
    return render(request,'motu_patlu.html')

def tom_jerry(request):
    return render(request,'tom_jerry.html')
