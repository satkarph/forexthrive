from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView
from .forms import SignUpForm, UserForm, ProfileForm, SessionForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from apps.userprofile.models import Profile

from apps.userprofile.models import Session
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView

class HomeView(TemplateView):
    template_name = 'common/home.html'

# class DashboardView(LoginRequiredMixin, TemplateView):
#     template_name = 'common/dashboard.html'
#     login_url = reverse_lazy('home')
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         print(self.request.user.id)
#         context['book_list'] = self.request.user
#         return context

class DashboardView(SuccessMessageMixin, CreateView, ListView):
    model = Session
    form_class = SessionForm
    template_name_suffix = '_create_form'
    success_url = "/dashboard/"
    success_message = "Session was added successfully"

    def form_valid(self, form):
        print(self.request.user)
        obj = form.save(commit=False)
        obj.user = User.objects.get(username=self.request.user)
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class SessionDeleteView(SuccessMessageMixin, DeleteView):
    model = Session
    success_url = "/dashboard/"
    success_message = "Session was deleted successfully"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SimulatorView(TemplateView):
    template_name = 'common/forexthrive.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from apps.userprofile.models import Profile

from django.contrib import messages

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'common/profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'common/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


