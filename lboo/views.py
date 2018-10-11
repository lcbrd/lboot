from django.shortcuts import render

# Create your views here.
def lboo(request):
    return render(request,"lb.html")