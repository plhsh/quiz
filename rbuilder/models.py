from django.db import models


class Cities(models.Model):
    city = models.CharField(max_length=128, verbose_name="City")
    country = models.CharField(max_length=64, blank=True, default='', verbose_name="Country")
    region = models.CharField(max_length=64, blank=True, default='', verbose_name="Region")

    def __str__(self):
        return self.city


class Locations(models.Model):
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='addresses_by_city', blank=True, verbose_name='city id')
    address = models.CharField(max_length=128, verbose_name="Address")


    # def save(self, *args, **kwargs):
    #     self.full_address = f"{self.country}.{self.city}.{self.addr}"
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.city_id.city}.{self.address}"


class Links(models.Model):
    loc_1 = models.ForeignKey(Locations, on_delete=models.PROTECT, related_name='links_loc_1')
    loc_2 = models.ForeignKey(Locations, on_delete=models.PROTECT, related_name='links_loc_2')
    bandwidth = models.PositiveIntegerField(default=0, verbose_name='Speed')
    price = models.PositiveIntegerField(default=0, verbose_name='Price')

    def __str__(self):
        return f"Private channel between {self.loc_1} & {self.loc_2} at the speed of {self.bandwidth} is available at {self.price} USD per month"

    def get_pair(self):
        return [self.loc_1, self.loc_2]


class Quotations(models.Model):
    loc_1 = models.ForeignKey(Locations, on_delete=models.PROTECT, related_name='quote_loc_1', verbose_name='Location A')
    loc_2 = models.ForeignKey(Locations, on_delete=models.PROTECT, related_name='quote_loc_2', verbose_name='Location B')
    bandwidth = models.PositiveIntegerField(default=0, verbose_name='Speed')
    email = models.EmailField(verbose_name='Email', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_time = self.time_create.strftime("%Y-%m-%d %H:%M")
        return f"{formatted_time} Private channel request between {self.loc_1} & {self.loc_2} at {self.bandwidth} speed from {self.email}"




