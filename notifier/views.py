from django.contrib.auth.models import User
from notifier.models import UserComment

from django.shortcuts import render
from django.views.generic.base import View

class NotifierBaseView(View):
    """
    Base view returning the system users and comments
    """

    def get(self, request, *args, **kwargs):
        context = {'users': User.objects.all(), 'comments': UserComment.objects.all()}
        return render(request, "user_list.html", context=context)
