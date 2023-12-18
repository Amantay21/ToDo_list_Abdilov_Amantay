from django import forms

from webapp.models import Status, Type


class TaskForms(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Заголовок')
    description = forms.CharField(max_length=400, required=True, label='Описание')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='status')
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Типы')

