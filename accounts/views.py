from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as auth_login
from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })


def login(request):
    provider_list = []
    # ...
    return auth_login(request,
        template_name='accounts/login.html',
        authentication_form=LoginForm,
        extra_context={
            'provider_list': provider_list,
        })

