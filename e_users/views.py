from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from e_users.forms import UserAuthForm
from e_users.models import UserDetail

def index(request):
    form = UserAuthForm()
    template_name = 'index.html'
    if request.method == 'POST':
        form = UserAuthForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            print username,password
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/userdetail')
            else:
                return HttpResponse('<h1>wrong credentials!!</h1>')
        else:
            return HttpResponse('<h1>retry</h1>')
    else:
        return  render(request,template_name,{'form':form,})

@login_required(login_url='/')
def UserDetailView(request):
    template_name = 'detailview.html'
    context = {'userdetails' : request.user.userdetail_set.all(),}
    return render(request,template_name,context)
