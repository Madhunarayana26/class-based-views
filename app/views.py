from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.
#insertion of data using function based view
def insert_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
    return render(request,'insert_fbv.html',d)
#insertion of data using class based view

class insert_cbv(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'insert_cbv.html',d)
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data is valid')








