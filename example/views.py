from django.http import *
from django.views.decorators.csrf import csrf_protect
from django.template import Context
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from django.contrib.auth.models import User, check_password

@csrf_protect
def login_user(request):
    logout(request)
    #template = get_template('login.html')
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')

    return render_to_response('login.html', RequestContext(request, {}))



@login_required(login_url='/login/')
def main(request):

    ## get user model
    user = User.objects.all()
    res = [n.username for n in user]

    return HttpResponse(res)