from django.db import models


class City(models.Model):
    name = models.CharField(max_length=60)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    def slugify(self):
        return self.name.replace(' ', '-').lower()

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(City, self).save(*args, **kwargs)


BRIEF_DESCRIPTION_CHOICES = [
    ('Ensolarado', 'Ensolarado'),
    ('Nublado', 'Nublado'),
    ('Chuvoso', 'Chuvoso'),
    ('Parcialmente nublado', 'Parcialmente nublado'),
    ('Neve', 'Neve'),
    ('Granizo', 'Granizo'),
]


class DailyWeather(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="weathers",
        unique_for_date="date"
    )
    date = models.DateField()
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    brief_description = models.CharField(
        max_length=20,
        choices=BRIEF_DESCRIPTION_CHOICES
    )

    def __str__(self):
        return f'{self.date.strftime("%d/%m/%Y")} - {self.brief_description}'
