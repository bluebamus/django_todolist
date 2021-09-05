from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    # path("login/", views.login_view, name="login"),
    path("login/", views.login_view.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("sigup", views.sign_up.as_view(), name="signup"),
    path("<int:pk>/", views.user_profile.as_view(), name="userprofile"),
    path("profileupdate/", views.profile_update.as_view(), name="profileupdate"),
    path("passwordupdate/", views.password_update.as_view(), name="passwordupdate"),
]