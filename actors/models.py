from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BR', 'Brasil'),
    ('UK', 'Reino Unido'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField(blank=True, null=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
