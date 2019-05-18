# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views import generic


def redirect_to_user(request):
    url = f"/accounts/profile/{request.user.id}/"
    return HttpResponseRedirect(redirect_to=url)


class UserProfileDetails(generic.DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'


class Signup(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
