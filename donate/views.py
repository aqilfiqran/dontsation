from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import DonateArticle
from .forms import BarcodeForm

# Create your views here.


class VerificationView(FormView):
    template_name = 'verification/verification.html'
    form_class = BarcodeForm
    success_url = '/valid/'

    def form_valid(self, form):
        return super().form_valid(form)


class ValidView(TemplateView):
    template_name = 'verification/valid.html'


class DonateListView(ListView):
    model = DonateArticle
    paginate_by = 5

    def get_queryset(self):
        if self.kwargs['category'] != 'all':
            self.queryset = self.model.objects.filter(
                category=self.kwargs['category'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = "Donate List"
        return context


class DonateDetailView(DetailView):

    model = DonateArticle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = "Donate Detail"
        return context


def Index(request):
    return render(request, "index.html", {"page": "aqil"})
