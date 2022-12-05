from django.db import models


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class MeetUp(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    # date = models.DateField()
    # image = models.ImageField(upload_to='images/%Y/%m/%d/', null=True)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # participants = models.ManyToManyField(Participant, blank=True)  # из-за связи с бд каждый учстник принимат участие в каждом сорвеновании
    organizer_email = models.EmailField()

    def __str__(self):
        return f'{self.slug} - {self.title}'

