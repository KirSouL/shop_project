from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Blog, Version
from pytils.translit import slugify


class ProductFormValidMixin:
    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductCreateView(ProductFormValidMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data


class ProductUpdateView(ProductFormValidMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data["object_list"]:
            current_version = Version.objects.filter(product=product, is_version=True)
            product.current_version = current_version
        return context_data

    def form_valid(self, form):
        forms = self.get_context_data()['current_version']
        self.object = form.save()
        if forms.is_valid():
            forms.instance = self.object
            forms.save()

        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class BlogFormValidMixin:
    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)


class BlogCreateView(BlogFormValidMixin, CreateView):
    model = Blog
    fields = ('title', 'information', 'preview', 'is_published',)
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(BlogFormValidMixin, UpdateView):
    model = Blog
    fields = ('title', 'information', 'preview', 'is_published',)

    # success_url = reverse_lazy('catalog:blog_list')
    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


def category(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Категории продуктов',
    }
    return render(request, 'catalog/category.html', context)


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"
