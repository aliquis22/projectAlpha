from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm
from .forms import UserRegisterForm, OrganisationRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            customer_group = Group.objects.get(name='Guests')
            user.groups.add(customer_group)

            messages.success(request, f'Создан аккаунт {username}')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})

def register_org(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            customer_group = Group.objects.get(name='Organisations')
            user.groups.add(customer_group)

            messages.success(request, f'Создан аккаунт {username}')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/reg_org.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        # Вызываем authenticate с указанием модели
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )

        if user is not None:
            login(self.request, user)
            # Вход выполнен успешно, выполните необходимые действия
            return redirect(self.get_success_url())
        else:
            # Неверные учетные данные, обработайте ошибку или покажите сообщение
            return self.form_invalid(form)

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

