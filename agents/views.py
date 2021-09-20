from django.http import request
from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from leads.models import Agent
from .forms import AgentModelForm
# Create your views here.


class AgentListView(LoginRequiredMixin, ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        return Agent.objects.all()


class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = "agents/agents_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent_list")

    def form_valid(self, form):

        agent = form.save(commit=False)
        print(self.request.user)
        agent.organization = self.request.user.userprofile
        agent.save()

        return super(AgentCreateView, self).form_valid(form)


class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "agents/agent_update.html"
    queryset = Agent.objects.all()
    form_class = AgentModelForm

    def get_success(self):
        return reverse("leads:lead_update")


class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = "agents/agent_detail.html"
    queryset = Agent.objects.all()

    context_object_name = "agent"


class AgentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "agents/agent_delete.html"
    queryset = Agent.objects.all()

    def get_success(self):
        return reverse("agents:agent_list")
