from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Bear, ProfileUser


# Create your views here.


class BearList(generic.ListView):
    model = Bear
    template_name = 'bear_list.html'
    context_object_name = 'bears'


class BearDetails(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Bear
    template_name = 'bear_detail.html'
    context_object_name = 'bear'


class UserBears(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Bear
    template_name = 'bear_list.html'
    context_object_name = 'bears'

    def get_queryset(self):
        user_id = int(self.request.user.id)
        try:
            author = ProfileUser.objects.all().filter(user__pk=user_id)[0]
            bears = Bear.objects.all().filter(author=author.pk)
            return bears
        except:
            return []
