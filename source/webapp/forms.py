from django import forms

from webapp.models import Status, Type, Task, Project


class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'types')
        # exclude = ()
        widgets = {'types': forms.CheckboxSelectMultiple}
        error_messages = {
            'title': {
                'required': 'Please enter',
                'min_length': 'Заголовок слишком короткий'
            }
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 4:
            raise forms.ValidationError('Заголовок слишком короткий')
        return title

    def bad_words(self):
        bad_words = ['дурак', 'дебил', 'чушпан']
        title = self.cleaned_data['title']
        description = self.cleaned_data['description']
        if bad_words in title or bad_words in description:
            raise forms.ValidationError('Нельзя использовать запещенные слова')
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        if title == description:
            raise forms.ValidationError('Заголовок и Контент не могут быть одинаковые')
        return cleaned_data


class ProjectForms(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'start_date', 'end_date')


# class TaskForms(forms.Form):
#     title = forms.CharField(max_length=200, required=True, label='Заголовок')
#     description = forms.CharField(max_length=400, required=True, label='Описание')
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), label='status')
#     types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Типы')

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
