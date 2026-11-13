from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    website = models.URLField()
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Photo(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name="photos"
    )
    image = models.ImageField(upload_to="hotels/")
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption

class Phone(models.Model):
    LABELS = [
        ("reception", "Reception"),
        ("reservation", "Reservation"),
    ]

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name="phones"
    )
    label = models.CharField(max_length=30, choices=LABELS)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.numbers
