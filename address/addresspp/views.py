from django.shortcuts import render
from .models import addressdata
from .forms import addressform
from django.http.response import HttpResponse
def addressview(request):
    if request.method=='POST':
        cform=addressform(request.POST)
        if cform.is_valid():
            name=request.POST.get('name','')
            mobileno=request.POST.get('mobileno','')
            city=request.POST.get('city','')
            address=request.POST.get('address','')
            a=addressdata(name=name,mobileno=mobileno,city=city,address=address)
            a.save()
            cform=addressform()
            return render(request,'addressform.html',{'kalla':cform})

        else:
            return HttpResponse("Invalid User Data")
    else:
        cform=addressform()
        return render(request,'addressform.html',{'kalla':cform})
def fetchingdata(request):
    data=addressdata.objects.all()
    return render(request,'addressdata.html',{'Dhamodar':data})

