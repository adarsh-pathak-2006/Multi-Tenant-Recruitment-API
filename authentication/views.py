from django.shortcuts import render, redirect
from core.models import User
from django.views import View
from authentication.forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        form=RegisterForm
        return render(request, 'register.html', { 'form':form })
    
    def post(self, request):
        form_data=RegisterForm(request.POST)
        if form_data.is_valid():
            username=form_data.cleaned_data['username']
            pass1=form_data.cleaned_data['password']
            pass2=form_data.cleaned_data['rep_password']

            if pass1==pass2:
                if User.objects.filter(username=username).exists():
                    return render(request, 'register.html', { 'form':form_data, 'user_err':'user alreadyt exists' })
                else:
                    User.objects.create_user(username=username, password=pass1)
                    return redirect('register')
                
            else:
                return render(request, 'register.html', { 'form':form_data, 'pass_err':'enter same passwords in both fields' })

        else:
            return render(request, 'register.html', { 'form':form_data, 'invalid':'invalid inputs' })