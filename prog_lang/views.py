from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.core.paginator import Paginator
from django.views import generic
from django.db.models import F
"""

GET - получает данные
POST - отправляет данные

"""

class Search_view(generic.ListView):
    template_name = 'prog_languages.html'
    context_object_name = 'prog_lang'
    model = models.ProgLang

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context

class UpdateProgLangView(generic.UpdateView):
    template_name = 'update_prog_lang.html'
    form_class = forms.ProgLangForm
    model = models.ProgLang
    success_url = '/prog_lang/'

    def get_object(self, **kwargs):
        prog_lang_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=prog_lang_id)

    def form_valid(self, form):
        print(form.changed_data)
        return super(UpdateProgLangView, self).form_valid(form=form)

class DeleteProgLangView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/prog_lang/'
    model = models.ProgLang
    context_object_name = 'ProgLang'


    def get_object(self, **kwargs):
        prog_lang_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=prog_lang_id)

class CreateProgLang(generic.CreateView):
    template_name = 'create_prog_lang.html'
    success_url = '/prog_lang/'
    form_class = forms.ProgLangForm


    def form_valid(self, form):
        print(form.changed_data)
        return super(CreateProgLang, self).form_valid(form=form)

class ProgLangDetail(generic.DetailView):
    template_name = 'prog_lang_detail.html'
    context_object_name = 'prog_id'
    pk_url_kwarg = 'id'
    model = models.ProgLang


    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request

        views_lang = request.session.get('viewed_lang', [])
        if obj.pk not in views_lang:
            models.ProgLang.objects.filter(pk=obj.pk).update(
                views = F("views")+1

            )
            views_lang.append(obj.pk)
            request.session['viewed_lang'] = views_lang

            obj.refresh_from_db()
        return obj

class ProgLangList(generic.ListView):
    template_name = 'prog_languages.html'
    model = models.ProgLang
    context_object_name = 'prog_lang'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prog_lang'] = context['prog_obj']
        return context
# def prog_lang_list_view(request):
#     if request.method == 'GET':
#          prog_lang = models.ProgLang.objects.all()
#          paginator = Paginator(prog_lang, 2)
#          page = request.GET.get('page')
#          page_obj = paginator.get_page(page)
#          return render(
#               request,
#               'prog_languages.html',
#               {
#                    "prog_lang": page_obj
#               }
#          )