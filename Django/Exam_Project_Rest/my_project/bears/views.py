from rest_framework import exceptions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Bear
from .serializers import BearSerializer, BearCreateSerializer


# Create your views here.


# class BearList(generic.ListView):
#     model = Bear
#     template_name = 'bear_list.html'
#     context_object_name = 'bears'

class MethodSerializerView(object):
    '''
    Utility class for get different serializer class by method.
    For example:
    method_serializer_classes = {
        ('GET', ): MyModelListViewSerializer,
        ('PUT', 'PATCH'): MyModelCreateUpdateSerializer
    }
    '''
    method_serializer_classes = None

    def get_serializer_class(self):
        assert self.method_serializer_classes is not None, (
                'Expected view %s should contain method_serializer_classes '
                'to get right serializer class.' %
                (self.__class__.__name__,)
        )
        for methods, serializer_cls in self.method_serializer_classes.items():
            if self.request.method in methods:
                return serializer_cls

        raise exceptions.MethodNotAllowed(self.request.method)


class Bears(MethodSerializerView, generics.ListCreateAPIView):
    queryset = Bear.objects.all()
    serializer_class = BearSerializer
    method_serializer_classes = {
        ('GET'): BearSerializer,
        ('POST'): BearCreateSerializer,

    }
    permission_classes = [IsAuthenticated]


class BearDetail(MethodSerializerView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Bear.objects.all()
    # serializer_class = BearSerializer
    method_serializer_classes = {
        ('GET'): BearSerializer,
        ('PUT', 'PATCH'): BearCreateSerializer,
    }

    permission_classes = [IsAuthenticated]

# class BearDetails(LoginRequiredMixin, generic.DetailView):
#     login_url = '/accounts/login/'
#     model = Bear
#     template_name = 'bear_detail.html'
#     context_object_name = 'bear'


# class UserBears(LoginRequiredMixin, generic.ListView):
#     login_url = '/accounts/login/'
#     model = Bear
#     template_name = 'bear_list.html'
#     context_object_name = 'bears'
#
#     def get_queryset(self):
#         user_id = int(self.request.user.id)
#         try:
#             author = ProfileUser.objects.all().filter(user__pk=user_id)[0]
#             bears = Bear.objects.all().filter(author=author.pk)
#             return bears
#         except:
#             return []
