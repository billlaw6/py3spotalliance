from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from accounts.models import User

# Create your views here.

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        """
        We make sure to call the parent's form_valid() method
        because it might do some processing (in the case of CreateView, it will
        call form.save() for example).
        """
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

#class IndexView(LoginRequiredMixin, View):
#class IndexView(AjaxableResponseMixin, View):
class IndexView(View):
    view_name = 'User Index View'
    def get(self, request, *args, **kwargs):
        return HttpResponse('This is user index view. %s' % self.view_name)

class UserCreate(AjaxableResponseMixin, CreateView):
    model = User
    fields = ['username',]

class UserUpdate(AjaxableResponseMixin, UpdateView):
    model = User
    fields = ['username',]

class UserDelete(AjaxableResponseMixin, DeleteView):
    model = User
    success_url = reverse_lazy('')
