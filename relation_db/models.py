from django.db import models


# Модель many:many / ManyToMany
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class NumberCar(models.Model):
    nameCar = models.CharField(max_length=100, default='Lexus GX 570')
    number_car = models.CharField(max_length=15, default='..KG....')
    tags = models.ManyToManyField(Tag, null=True)


    def __str__(self):
        return f"{self.nameCar}------{', '.join(i.name for i in self.tags.all())}"

# модель отношение 1:1 / OneToOne
class DocumetsCar(models.Model):
    choice_car = models.OneToOneField(NumberCar, on_delete=models.CASCADE, related_name='car')
    document = models.CharField(max_length=100)

    def __str__(self):
        return self.document
    

# Модель 1:many / OneToMany
class Review(models.Model):
    # MARKS - это наше соотношение оценок, почему 2? потому что одно значение идет в бд другое на отображение
    MARKS = {
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    }
    # Создаем отношение один к многим
    """
    1. первым параметром принимаем класс
    2. on_delete параметри нужен для того чтобы если удалилась машина, то и оценки удалятся
    3. realited_name параметр нужен для
    """
    choice_car = models.ForeignKey(NumberCar, on_delete=models.CASCADE, related_name='review')
    marks = models.CharField(max_length=100, choices=MARKS, default='5')
    text = models.CharField(max_length=100, default='отличная машина')
    created_at = models.DateTimeField(auto_now_add=True)

    """
    напомню что charfield нужен для хранения данных в небольшом количестве
    datetimefield с параметром auto_now_add=True, нужен для того чтобы принимать автоматически дату
    """

    def __str__(self):
        return f"Марка автомобиля {self.choice_car} Оценка: {self.marks} Комментарий к оценки {self.text}"
    