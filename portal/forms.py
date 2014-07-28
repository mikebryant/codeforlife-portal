from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class TeacherSignupForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(label='Email address', widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    school = forms.CharField(label='School / Club', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'School / Club'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    def clean_email(self):
        email = self.cleaned_data.get('email', None)

        if email:
            users = User.objects.filter(email=email)
            if len(users) != 0:
                raise forms.ValidationError('That email address is already in use')

        return email

    def clean(self):
        password = self.cleaned_data.get('password', None)
        confirm_password = self.cleaned_data.get('confirm_password', None)

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Your passwords do not match')

        return self.cleaned_data

class TeacherEditAccountForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(label='Email address', widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(label='New password (optional)', required=False, widget=forms.PasswordInput(attrs={'placeholder': 'New password (optional)'}))
    confirm_password = forms.CharField(label='Confirm new password', required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'}))
    current_password = forms.CharField(label='Current password', widget=forms.PasswordInput(attrs={'placeholder': 'Current password'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(TeacherEditAccountForm, self).__init__(*args, **kwargs)


    def clean_email(self):
        email = self.cleaned_data.get('email', None)

        if email:
            users = User.objects.filter(email=email)
            if not (len(users) == 0 or (len(users) == 1 and users[0].email == self.user.email)):
                raise forms.ValidationError('That email address is already in use')

        return email

    def clean(self):
        password = self.cleaned_data.get('password', None)
        confirm_password = self.cleaned_data.get('confirm_password', None)
        current_password = self.cleaned_data.get('current_password', None)

        if (password or confirm_password) and password != confirm_password:
            raise forms.ValidationError('Your new passwords do not match')

        if not self.user.check_password(current_password):
            raise forms.ValidationError('Your current password was incorrect')

        return self.cleaned_data


class TeacherLoginForm(forms.Form):
    email = forms.EmailField(label='Email address', widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        email = self.cleaned_data.get('email', None)
        password = self.cleaned_data.get('password', None)

        if email and password:
            users = User.objects.filter(email=email)
            if len(users) != 1:
                raise forms.ValidationError('Incorrect email address or password')

            user = authenticate(username=users[0].username, password=password)

            if user is None:
                raise forms.ValidationError('Incorrect email address or password')
            if not user.is_active:
                raise forms.ValidationError('User account has been deactivated')

            self.user = user

        return self.cleaned_data

class ClassCreationForm(forms.Form):
    name = forms.CharField(label='Group Name', widget=forms.TextInput(attrs={'placeholder': 'Group Name'}))

class StudentCreationForm(forms.Form):
    names = forms.CharField(label='names', widget=forms.Textarea)