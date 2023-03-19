from django.shortcuts import render, redirect
from django.contrib.auth import logout
from item.models import Category, Item
from .forms import SignupForm
from .models import AitverFullProjectTeamMember,ProjectFile
# Create your views here.

def index(request):
    items=Item.objects.filter(is_sold=False)[0:8]
    categories=Category.objects.all()
    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items
    })
    
def aitvet(request):
    members = AitverFullProjectTeamMember.objects.all()
    pfiles = ProjectFile.objects.all()
    return render(request, 'core/aitvet.html',{
        'members': members,
        'projectfiles': pfiles,
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login/')