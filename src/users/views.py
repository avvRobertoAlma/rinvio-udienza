from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponse

def logout_view(request):
    logout(request)
    res = HttpResponse()
    res.delete_cookie('sessionid')
    return redirect('home')
    