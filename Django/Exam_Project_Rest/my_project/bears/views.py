from django.views import generic

from .models import Bear


# Create your views here.


class BearList(generic.ListView):
    model = Bear
    template_name = 'bear_list.html'
    context_object_name = 'bears'


class BearDetails(generic.DetailView):
    model = Bear
    template_name = 'bear_detail.html'
    context_object_name = 'bear'
