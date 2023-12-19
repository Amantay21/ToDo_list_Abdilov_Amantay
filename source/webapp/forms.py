from django import forms

from webapp.models import Status, Type, Task


class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'types')
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
            if bad_words in title:
                raise forms.ValidationError('Нельзя использовать запещенные слова')
            return title
# class TaskForms(forms.Form):
#     title = forms.CharField(max_length=200, required=True, label='Заголовок')
#     description = forms.CharField(max_length=400, required=True, label='Описание')
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), label='status')
#     types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Типы')




