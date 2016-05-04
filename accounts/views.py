from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
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
    # 不能直接将函数装饰器用在方法上，必须使用method_decorator转为方法装饰器
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse('This is user index view. %s' % self.view_name)


class UserList(ListView):
    model = User
    # default context_object_name is object_list
    context_object_name = 'object_list'
    queryset = User.objects.all()

    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(UserList, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = 'User List View Page Title'
        return context

    def get_queryset(self):
        #self.user = get_object_or_404(User, username=self.args[0])
        return User.objects.filter(is_active=True)

    def head(self, *args, **kwargs):
        last_user = self.get_queryset().latest('data_joined')
        response = HttpResponse('')
        # RFC 1123 date formate
        response['Last-Modified'] = last_user.data_joined.strftime('%a, %d %b %Y &H:%M:%S GMT')
        return response

class UserDetail(DetailView):
    queryset = User.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(UserDetailView, self).get_object()
        # 自定义处理
        return object


class UserCreate(AjaxableResponseMixin, CreateView):
    model = User
    fields = ['username',]
    success_url = reverse_lazy('')


class UserUpdate(AjaxableResponseMixin, UpdateView):
    model = User
    fields = ['username',]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserUpdate, self).dispatch(*args, **kwargs)


class UserDelete(AjaxableResponseMixin, DeleteView):
    model = User
    success_url = reverse_lazy('')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserDelete, self).dispatch(*args, **kwargs)



