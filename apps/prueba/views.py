from django.shortcuts import render

from django.views.generic import FormView
from .forms import UserRegisterForm
from .models import User

# Create your views here.

class UserFormView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'


    def form_valid(self, form):
        
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
        )

        return super(UserFormView, self).form_valid(form)


def base(request):
    return render(request, 'users/base.html')