from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.admin import User

TYPE_OF_FLIGHT = (
    ('Эконом', 'Эконом'),
    ('Бизнес', 'Бизнес'),
    ('Первый класс', 'Первый класс')
)

class Tickets(models.Model):
    name_origin = models.CharField("Город вылета", max_length=100)
    name_dest = models.CharField("Город прилета", max_length=100)
    name_origin_aero = models.CharField("Аэропорт вылета", max_length=100)
    name_dest_aero = models.CharField("Аэропорт прилета", max_length=100)
    time_origin = models.TimeField("Время и дата вылета")
    time_dest = models.TimeField("Время и дата прилета")
    date_origin = models.DateField("Время прилета")
    date_dest = models.DateField("Время прилета")
    ticket_price = models.IntegerField("Цена билета")
    type_of_flight = models.CharField("Тип перелета", choices=TYPE_OF_FLIGHT, max_length=100)

    def __str__(self):
        return self.name_origin

    def get_absolute_url(self):
        return reverse("product", kwargs={"pk": self.pk})

    def get_add_to_sales_url(self):
        return reverse("add_to_cart", kwargs={"pk": self.pk})

    def get_remove_from_sales_url(self):
        return reverse("remove_from_cart", kwargs={"pk": self.pk})


class UsersSales(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sale = models.ForeignKey(Tickets, on_delete=models.CASCADE)

