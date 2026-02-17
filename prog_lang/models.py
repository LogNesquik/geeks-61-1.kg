from django.db import models

class ProgLang(models.Model):
    # charfield - поле которое отвечает за кол-во символов в форме
    # verbose_name - название поля в панели
    title = models.CharField(max_length=30, verbose_name='Укажите язык программирования')
    # TextField - поле для ввода большого текста
    description = models.TextField(verbose_name='Укажите описание языка программирования')
    # ImageField - поле для загрузки media картинок - принимает любые виды картинок
    image = models.ImageField(upload_to='proglang/', verbose_name='Загрузите изображение языка программирования')
    # PositiveBigIntegerField - поле для ввода больших чисел (только положительные)
    # blank=True - поле не обязательное для заполнения
    create_date_lang = models.PositiveBigIntegerField(blank=True, verbose_name='Укажите год создания языка программирования')
    # DateTimeField - поле для ввода даты и времени
    # auto_now_add=True - при создании записи автоматически заполняет текущее время и дату
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи')

    views = models.PositiveIntegerField(default=0, null=True)

    # TODO - изучать поля самостоятельно FileField, URLField, EmailField.
    # FileFied - поле для загрузки любых файлов, например .pdf, .docx и т.д.
    # URLField - поле для ввода ссылок, например https://www.example.com
    # EmailField - поле для ввода email адресов, например admin@example.com
    # TODO - изучить атрибут null=True
    # null - это атрибут который позволяет сохранять пустые значения в базе данных
    # TODO - почитать документацию джанго



    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'