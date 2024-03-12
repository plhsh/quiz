from django.db import models


class Cities(models.Model):
    city = models.CharField(max_length=128, verbose_name="Город")

    def __str__(self):
        return self.city


class Locations(models.Model):
    region = models.CharField(max_length=20, verbose_name="Регион")
    country = models.CharField(max_length=3, verbose_name="Страна")
    city = models.CharField(max_length=3, verbose_name="Город")
    addr = models.CharField(max_length=4, verbose_name="Адрес")
    full_address = models.CharField(max_length=12, blank=True)
    ct = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='city_by_address', blank=True, verbose_name='city id')


    # def save(self, *args, **kwargs):
    #     self.full_address = f"{self.country}.{self.city}.{self.addr}"
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.full_address


class Links(models.Model):
    loc_1 = models.ForeignKey(Locations, on_delete=models.PROTECT, related_name='links_loc_1')
    loc_2 = models.ForeignKey(Locations, on_delete=models.PROTECT, related_name='links_loc_2')
    bandwidth = models.PositiveIntegerField(default=0, verbose_name='Скорость')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')

    def __str__(self):
        return f"Канал между {self.loc_1} и {self.loc_2} на скорости {self.bandwidth} доступен по цене {self.price} USD в месяц"

    def get_pair(self):
        return [self.loc_1, self.loc_2]


class Quotations(models.Model):
    loc_1 = models.ForeignKey(Locations, on_delete=models.PROTECT, related_name='quote_loc_1', verbose_name='Локация 1')
    loc_2 = models.ForeignKey(Locations, on_delete=models.PROTECT, related_name='quote_loc_2', verbose_name='Локация 2')
    bandwidth = models.PositiveIntegerField(default=0, verbose_name='Скорость')
    email = models.EmailField(verbose_name='Email', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.time_create.strftime("%Y-%m-%d %H:%M")
        return f"{formatted_time} Запрос на канал между {self.loc_1} и {self.loc_2} на скорости {self.bandwidth} от {self.email}"




