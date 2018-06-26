from django import forms
from django.contrib.auth.models import User
from timetable.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Set password', widget=forms.PasswordInput(attrs={
                'class': 'item-input-wrapper form-control',
                'name': 'password',
                'autofocus': 'autofocus',
            }))

    first_name = forms.CharField(label='Enter your first name', widget=forms.TextInput(attrs={
                'class': 'item-input-wrapper form-control',
                'name': 'first_name',
                'autofocus': 'autofocus',
            }))

    last_name = forms.CharField(label='Enter your last name', widget=forms.TextInput(attrs={
        'class': 'item-input-wrapper form-control',
        'name': 'last_name',
        'autofocus': 'autofocus',
    }))

    username = forms.CharField(label='Set username', widget=forms.TextInput(attrs={
        'class': 'item-input-wrapper form-control',
        'name': 'username',
        'autofocus': 'autofocus',
    }))

    email = forms.CharField(label='Enter your email address', widget=forms.EmailInput(attrs={
        'class': 'item-input-wrapper form-control',
        'name': 'email',
        'autofocus': 'autofocus',
    }))

    def __init__(self,*args, **kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})

        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label = ''

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    teacherSubject = forms.CharField(label='Enter the subjects you teach', widget=forms.TextInput(attrs={
        'class': 'item-input-wrapper form-control',
        'name': 'Subjects',
        'autofocus': 'autofocus',
    }))
    teacherClasses = forms.CharField(label='Enter the classes you teach', widget=forms.TextInput(attrs={
        'class': 'item-input-wrapper form-control',
        'name': 'Classes',
        'autofocus': 'autofocus',
    }))

    def __init__(self,*args, **kwargs):
        super(UserProfileForm,self).__init__(*args,**kwargs)
        self.fields['teacherSubject'].widget.attrs.update({'autofocus': 'autofocus'})

        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label = ''

    class Meta:
        model = UserProfile
        fields = ('teacherSubject', 'teacherClasses')
