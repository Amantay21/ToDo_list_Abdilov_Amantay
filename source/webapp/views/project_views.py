from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SimpleSearchForm, ProjectForms, EditUsersInProjectForms
from webapp.models import Project


class ProjectsView(ListView):
    model = Project
    template_name = 'projects/index.html'
    context_object_name = 'projects'
    paginate_by = 4

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) |
                                       Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/projects_detail_view.html'


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/projects_create.html'
    form_class = ProjectForms
    permission_required = 'webapp.add_project'

    def get_success_url(self):
        return reverse('webapp:projects_detail_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/projects_update.html'
    form_class = ProjectForms
    permission_required = 'webapp.change_project'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()

    def get_success_url(self):
        return reverse('webapp:projects_detail_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/projects_delete.html'
    success_url = reverse_lazy('webapp:index')

    permission_required = 'webapp.delete_project'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()


class EditUsersInProjectView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/projects_update.html'
    form_class = EditUsersInProjectForms

    permission_required = 'webapp.edit_users_in_project'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()

    def get_success_url(self):
        return reverse('webapp:projects_detail_view', kwargs={'pk': self.object.pk})
