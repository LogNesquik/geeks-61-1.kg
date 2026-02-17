from django.urls import path
from . import views

app_name = 'yaziki'

urlpatterns = [
    path('prog_lang/', views.ProgLangList.as_view(), name='yaziki_programmirovanie'),
    path('prog_lang/<int:id>/', views.ProgLangDetail.as_view()),
    path('prog_lang/<int:id>/delete', views.DeleteProgLangView.as_view()),
    path('prog_lang/<int:id>/edit', views.UpdateProgLangView.as_view()),

    path('create_prog_lang/', views.CreateProgLang.as_view(), name='sozdat_blog'),
    path('search/', views.Search_view.as_view()),
]