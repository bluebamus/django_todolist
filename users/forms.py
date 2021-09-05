from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))

# class SignupForm(forms.Form):

#     first_name = forms.CharField(max_length=80)
#     last_name = forms.CharField(max_length=80)
#     email = forms.EmailField()
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     check_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         try:
#             models.User.objects.get(username=username)
#             raise forms.ValidationError("User already exists with that username")
#         except models.User.DoesNotExist:
#             return username

#     def clean_check_password(self):
#         password = self.cleaned_data.get("password")
#         check_password = self.cleaned_data.get("check_password")
#         if password != check_password:
#             raise forms.ValidationError("Password confirmation does not match")
#         else:
#             return password

#     def save(self):
#         first_name = self.cleaned_data.get("first_name")
#         last_name = self.cleaned_data.get("last_name")
#         email = self.cleaned_data.get("email")
#         password = self.cleaned_data.get("password")
#         username = self.cleaned_data.get("username")
#         user = models.User.objects.create_user(username, email, password)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()

class SignupForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    check_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username")

    def clean_check_password(self):
        password = self.cleaned_data.get("password")
        check_password = self.cleaned_data.get("check_password")
        if password != check_password:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.set_password(password)
        user.save()