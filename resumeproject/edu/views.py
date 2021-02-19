from django.shortcuts import render

# Create your views here.
def skil(request):
    cont={'skil':'active'}
    return render(request,'edu/skil.html',cont)