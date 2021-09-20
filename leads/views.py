from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Leads, Agent
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

# class LoginView(TemplateView):


class SignupView(LoginRequiredMixin, CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(LoginRequiredMixin, TemplateView):
    template_name = "landing.html"


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/leads_list.html"
    queryset = Leads.objects.all()
    # tochange name passed to html
    context_object_name = "leads"


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/leads_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")

    def form_valid(self, form):
        send_mail(
            subject="A lead Has Been Created",
            message="Go to the site to see details",
            from_email="ahmedmostafa12211@gmail.com",
            recipient_list=["ahmedmostafa12211@gmail.com"]
        )

        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Leads.objects.all()
    form_class = LeadModelForm

    def get_success(self):
        return reverse("leads:lead_update")


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/leads_detail.html"
    queryset = Leads.objects.all()

    context_object_name = "lead"


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Leads.objects.all()

    def get_success(self):
        return reverse("leads:lead_list")


def landing_page(request):
    return render(request, "landing.html")


def lead_list(request):
    leads = Leads.objects.all()
    context = {"leads": leads}
    return render(request, "leads/leads_list.html", context)


def lead_detail(request, pk):
    lead = Leads.objects.get(id=pk)
    context = {"lead": lead}
    return render(request, "leads/leads_detail.html", context)


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            # ||
            # first_name = form.cleaned_data["first_name"]
            # last_name = form.cleaned_data["last_name"]
            # age = form.cleaned_data["age"]
            # agent = form.cleaned_data["agent"]
            # Leads.objects.create(first_name=first_name,
            #                      last_name=last_name, age=age, agent=agent)
            return redirect('/leads')
    context = {"form": form}
    return render(request, "leads/leads_create.html", context)


def lead_update(request, id):

    return render(request, "leads/lead_update.html")


def lead_delete(request, id):
    pass
