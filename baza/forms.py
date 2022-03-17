from django import forms
from .models import Reader


class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ('fio', 'eticket', 'phone')

        def __init__(self, *args, **kwargs):
            super(ReaderForm, self).__init__(*args, **kwargs)
            self.fields[fields].widget.attrs.update({'class': 'form-control'})