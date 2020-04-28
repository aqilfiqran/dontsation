from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView, View
from .models import DonateArticle, Donate
from .forms import BarcodeForm, DonateForm
from .generators import generateCode, sendVerification, isCheck

# Create your views here.


class DonateCreateView(CreateView):
    form_class = DonateForm
    template_name = 'donate/create.html'
    extra_context = {
        'page': 'Dontsation : Donasi'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        donateArticle = DonateArticle.objects.only(
            'id').get(id=self.kwargs['pk'])
        barcode = generateCode(200)

        form.instance.confirmation = 0
        form.instance.donateArticle = donateArticle
        form.instance.barcode = barcode

        sendVerification(form.instance.email, barcode)
        return super().form_valid(form)


class VerificationView(FormView):
    template_name = 'verification/verification.html'
    form_class = BarcodeForm
    success_url = '/valid/'
    extra_context = {
        'page': 'Dontsation : Verifikasi'
    }

    def get_context_data(self, **kwargs):
        kwargs.update(self.extra_context)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if isCheck(form.cleaned_data['code']) == False:
            return redirect('donate:verify')
        return super().form_valid(form)


class ValidView(TemplateView):
    template_name = 'verification/valid.html'


class DonateListView(ListView):
    model = DonateArticle
    paginate_by = 5

    def get_queryset(self):

        try:
            self.queryset = self.model.objects.filter(
                title__icontains=self.kwargs['search'])
        except KeyError:
            pass

        if self.kwargs['category'] != 'all':
            self.queryset = self.model.objects.filter(
                categoryslug=self.kwargs['category'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('page'):
            context['current'] = int(self.request.GET.get('page'))
        else:
            context['current'] = 1
        context['page'] = "Dontsation : List"
        return context


class DonateDetailView(DetailView):

    model = DonateArticle

    def get_context_data(self, **kwargs):
        receive = 0

        donateArticle = DonateArticle.objects.only(
            'id').get(slug=self.kwargs['slug'])
        donators = Donate.objects.filter(donateArticle=donateArticle)
        print(donators)
        context = super().get_context_data(**kwargs)
        context['page'] = "Dontsation : Detail"

        for donator in donators:
            receive += donator.donation

        context['donators'] = donators
        context['receive'] = receive

        return context


class Index(View):
    extra_context = {
        'page': 'Dontsation : Beranda',
    }

    def get(self, request):
        return render(request, 'index.html', self.extra_context)

    def post(self, request):
        return redirect('donate:list', category='all', search=request.POST['search'])
