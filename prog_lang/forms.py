from django import forms
from prog_lang.models import ProgLang

class ProgLangForm(forms.ModelForm):
    class Meta:
        model = ProgLang
        fields = "__all__"

        # если вдруг хотим вытащить по одному
        # fields = "перечисление чего хотим вытащить".split()
        # Тут нужно быть внимательным потому что если некоторые поля будут обязательными и мы их не отобразим - будет ошибка

