from .models import Article
from django.urls import reverse_lazy  # new
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView  # new
)
from django.views.generic import ListView, DetailView  # new
from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin  # esto es para que solo el usuario logeado
    # pueda editar lo suyo y no lo de otro
)


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(LoginRequiredMixin, DetailView):  # new
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
):  # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView
):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    # esto es para que solo los usuarios logeados puedan
    # editar o eliminar lo suyo, si es falso tira un
    # 403 permission denied error

    def test_func(self):  # new
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    #fields = ('title', 'body', 'author',)
    # Para que el usuario se asigne automaticamente en funcion
    # de quien esta registrado
    fields = ('title', 'body')

    # esto permite setearlo automaticamente al usuario
    # de la sesion
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
