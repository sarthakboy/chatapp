
from django.shortcuts import render, redirect


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chating/chatPage.html", context)



def login_view(request):
    return render(request, 'chating/LoginPage.html')
