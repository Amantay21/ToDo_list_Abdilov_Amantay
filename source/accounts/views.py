from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from accounts.forms import MyUserCreationForm


class RegisterView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = "user_create.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if not next_page:
            next_page = self.request.POST.get('next')
        if not next_page:
            next_page = reverse('webapp:index')
        return next_page
