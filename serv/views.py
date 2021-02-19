from django.shortcuts import render

# Create your views here.
def services(request):
    cont={'ser':'active'}
    return render(request,'serv/services.html',cont)