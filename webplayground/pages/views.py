from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy, reverse
from .models import Page
from pages.forms import PageForm

# Create your views here.
class PageList(ListView):
    model = Page
    
class PageDetail(DetailView):
    model = Page

@method_decorator(staff_member_required, name="dispatch")
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy("pages:pages")

@method_decorator(staff_member_required, name="dispatch")
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"

    def get_success_url(self, ) -> str:
        return reverse_lazy("pages:update", args=[self.object.id]) + "?ok"

@method_decorator(staff_member_required, name="dispatch")
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")
