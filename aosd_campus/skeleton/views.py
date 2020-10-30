from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from skeleton import models, forms

# Create your views here.

# View for Navbar
class BaseView(TemplateView):
    template_name = 'skeleton/base.html'

# Front Page/Home
class FrontView(ListView):
    template_name = 'skeleton/front.html'
    model = models.SpecialEvent
    context_object_name = 'special_list'

    def get_context_data(self,**kwargs):

        context  = super().get_context_data(**kwargs)
        context['connection_form'] = forms.ConnectionForm
        return context

    def post(self, request):
        connect_form = forms.ConnectionForm(request.POST)
        if connect_form.is_valid():
            instance = connect_form.save(commit=False)
            instance.save()

            # Sending Mail
            cf_name = connect_form.cleaned_data['name']
            cf_phone = connect_form.cleaned_data['phone']
            cf_email = connect_form.cleaned_data['email']
            cf_interest = connect_form.cleaned_data['interest']
            cf_date = timezone.now();
            subject = "LET'S CONNECT SUBMITTED on WEBSITE: {} at {}".format(cf_name, cf_date)
            message = "Connection form submitted from website at {}.\nName: {}\nPhone: {}\nEmail: {}\nInterest: {}\n".format(cf_date, cf_name, cf_phone, cf_email, cf_interest)
            recipient = ["aosdcampus@gmail.com", "timea1337@gmail.com"]
            sender = "aosd.helper@gmail.com"
            try:
                send_mail(subject, message, sender, recipient)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
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
            instance.save()

            # Sending Mail
            bf_name = biblestudy_form.cleaned_data['name']
            bf_phone = biblestudy_form.cleaned_data['phone']
            bf_email = biblestudy_form.cleaned_data['email']
            bf_date = timezone.now();
            subject = "BIBLE STUDY CONNECTION SUBMITTED on WEBSITE: {} at {}".format(bf_name, bf_date)
            message = "Bible Study form submitted from website at {}.\nName: {}\nPhone: {}\nEmail:{}".format(bf_date, bf_name, bf_phone, bf_email)
            recipient = ["aosdcampus@gmail.com", "timea1337@gmail.com"]
            sender = "aosd.helper@gmail.com"
            try:
                send_mail(subject, message, sender, recipient)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

        return HttpResponseRedirect(reverse('skeleton:connect'))

#Gallery Page
class GalleryView(TemplateView):
    template_name = 'skeleton/gallery.html'

#Events Page
class EventView(ListView):
    model = models.SpecialEvent
    context_object_name = 'special_list'
    template_name = 'skeleton/events.html'

#Resources page
class ResourceView(ListView):
    model = models.Resource
    context_object_name = 'resource_list'
    template_name = 'skeleton/resources.html'

#Rush week signup
class SignUpView(TemplateView):
    template_name = 'skeleton/signup.html'

#Rush week signup
class PicGameView(TemplateView):
    template_name = 'skeleton/picgame.html'
