from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time', 'name', 'phone']

    def __init__(self, *args, **kwargs):
        organisation = kwargs.pop('organisation', None)
        super(ReservationForm, self).__init__(*args, **kwargs)

        # Ограничиваем список доступных столов теми, которые есть у выбранной организации
        if organisation:
            self.fields['table'].widget = forms.Select(choices=[(i, i) for i in range(1, organisation.tables + 1)])