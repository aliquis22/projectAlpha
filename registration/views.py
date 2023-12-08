from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm
from .forms import UserRegisterForm, OrganisationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from .models import  Organisation
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

@login_required
def register_organisation(request):
    if request.method == 'POST':
        form = OrganisationForm(request.POST)
        if form.is_valid():
            organisation = form.save(commit=False)
            organisation.owner = request.user
            organisation.save()
            return redirect('index')  # Замените 'success_url' на URL, куда перенаправлять после успешной регистрации
    else:
        form = OrganisationForm()

    return render(request, 'registration/reg_org.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )

        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)

