from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, OrganisationRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}')
            return redirect('index')
    else:
        form = UserRegisterForm()
        return render(request, 'registration/register.html', {'form':form})

# def register_org(request):
#     if request.method == 'POST':
#         form = OrganisationRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Создан аккаунт {username}')
#             return redirect('index')
#     else:
#         form = OrganisationRegisterForm
#         return render(request, 'registration/register.html', {'form':form})

