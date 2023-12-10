from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group
from registration.models import Organisation
from .forms import ReservationForm

def home(request):
    all_organisations = Organisation.objects.all()
    return render(request, 'reservation/index.html', {'all_organisations': all_organisations})

def about(request):
    return render(request, 'reservation/about.html')

def reservation(request, pk):
    organisation = get_object_or_404(Organisation, pk=pk)
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST, organisation=organisation)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.organisation = organisation
            reservation.save()
            return redirect('index')
    else:
        reservation_form = ReservationForm(organisation=organisation)
    return render(request, 'reservation/reservation.html', {'organisation': organisation, 'reservation_form': reservation_form})

