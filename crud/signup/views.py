
# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from .models import Signup
from django.utils import timezone

# Create your views here.
def home(request):
    signups = Signup.objects.all()
    return render(request, 'home.html', {'signups':signups})

def detail(request, id):
    signup = get_object_or_404(Signup, pk=id)
    return render(request, 'detail.html', {'signup':signup})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_signup = Signup()
    new_signup.name = request.POST['name']
    new_signup.age = request.POST['age']
    new_signup.pub_date = timezone.now()
    new_signup.email = request.POST['email']
    new_signup.introduce = request.POST['introduce']
    new_signup.save()
    return redirect('detail', str(new_signup.id))

def edit(request, id):
    edit_Signup = Signup.object.get(pk=id)
    return render(request, 'edit.html', {'Signup':edit_Signup})

def update(request, id):
    update_Signup = Signup.objects.get(id=id)
    update_Signup.name = request.POST['name']
    update_Signup.age = request.POST['age']
    update_Signup.email = request.POST['email']
    update_Signup.pub_date = timezone.now()
    update_Signup.introduce = request.POST['introduce']
    update_Signup.save()
    return redirect('detail', str(update_Signup.id))

def delete(request, id):
    delete_Signup = Signup.objects.get(id=id)
    delete_Signup.delete()
    return redirect('home')