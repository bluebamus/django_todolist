from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login

from . import forms


# @ function-based view

# def login_view(request):
#     if request.method == "GET":
#         form = forms.LoginForm()
#         return render(request, "users/login.html", {"form": form})

#     elif request.method == "POST":
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect(reverse("home:index"))
#         return render(request, "users/login.html", {"form": form})

# @ class-based view

# from django.views import View

# class login_view(View):
#     def get(self, request):
#         form = forms.LoginForm()
#         return render(request, "users/login.html", {"form": form})

#     def post(self, request):
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect(reverse("home:index"))
#         return render(request, "users/login.html", {"form": form})

# @ FormView를 사용한 login_view

# from django.views.generic import FormView
# from django.urls import reverse_lazy

# class login_view(FormView):
#     template_name = "users/login.html"
#     form_class = forms.LoginForm
#     success_url = reverse_lazy("home:index")

#     def form_valid(self, form):
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(self.request, username=username, password=password)
#         if user is not None:
#             login(self.request, user)
#         return super().form_valid(form)

# @ LoginView를 사용한 login_view

from django.contrib.auth.views import LoginView

class login_view(LoginView):
    template_name = "users/login.html"


from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout

def log_out(request):
    logout(request)
    return redirect(reverse("home:index"))

from django.views.generic import FormView
from django.urls import reverse_lazy

class sign_up(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("home:index")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


from django.views.generic import DetailView
from . import models as user_models

class user_profile(DetailView):

    model = user_models.User
    context_object_name = "user_obj"
    template_name = "users/profile.html"


from django.views.generic import UpdateView

class profile_update(UpdateView):
    model = user_models.User
    template_name = "users/update.html"
    fields = (
        "first_name",
        "last_name",
        "avatar",
        "gender",
        "bio",
        "birthday",
    )

    def get_object(self, queryset=None):
        return self.request.user


from django.contrib.auth.views import PasswordChangeView

class password_update(PasswordChangeView):

    template_name = "users/update_password.html"
    success_url = reverse_lazy('users:login')