from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    website = models.URLField()
    email = models.EmailField()

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