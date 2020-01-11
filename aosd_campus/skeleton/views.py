from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from skeleton import models, forms

# Create your views here.

# View for Navbar
class BaseView(TemplateView):
    template_name = 'skeleton/base.html'

# Front Page/Home
class FrontView(TemplateView):
    template_name = 'skeleton/front.html'

    def get_context_data(self,**kwargs):

        context  = super().get_context_data(**kwargs)
        context['connection_form'] = forms.ConnectionForm
        return context

    def post(self, request):
        connect_form = forms.ConnectionForm(request.POST)
        if connect_form.is_valid():
            instance = connect_form.save(commit=False)
            instance.save()
        return HttpResponseRedirect(reverse('skeleton:front'))

# About Page
class AboutView(ListView):
    model = models.Leader
    context_object_name = 'leader_list'
    template_name = 'skeleton/about.html'

# Connect Page
class ConnectView(ListView):
    model = models.BibleTalk
    context_object_name = 'bt_list'
    template_name = 'skeleton/connect.html'

    def get_context_data(self,**kwargs):

        context  = super().get_context_data(**kwargs)
        context['bstudy_form'] = forms.BibleStudyForm
        return context

    def post(self, request):
        biblestudy_form = forms.BibleStudyForm(request.POST)
        if biblestudy_form.is_valid():
            instance = biblestudy_form.save(commit=False)
            instance.interest = 'Bible Study'
            instance.save()
        return HttpResponseRedirect(reverse('skeleton:connect'))

class GalleryView(TemplateView):
    template_name = 'skeleton/gallery.html'
