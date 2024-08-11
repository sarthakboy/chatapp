from django.urls import path, include
from chating import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
 path("", LoginView.as_view(template_name="chating/LoginPage.html"), name="login-user"),

    # login-section
    path("auth/login/", LoginView.as_view
         (template_name="chating/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(next_page="login-user"), name="logout-user"),
    path("chat/", chat_views.chatPage, name="chat-page"),
]
