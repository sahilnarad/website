from django.shortcuts import render
from django.http import HttpResponse
def admin(request):
   
   #return render(request,'hello.html')
   return HttpResponse("Hello World...!");
