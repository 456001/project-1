from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sanchi(request):
    return render(request,'sanchi.html')

def dairymilk(request):
    return HttpResponse('dairymilk create happiness among us')
