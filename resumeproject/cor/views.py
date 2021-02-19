from django.shortcuts import render

# Create your views here.
def home(request):
    cont={'home':'active'}
    return render(request,'cor/home.html',cont)
def contect(request):
    cont={'contect':'active'}

    return render(request,'cor/context.html',cont)
