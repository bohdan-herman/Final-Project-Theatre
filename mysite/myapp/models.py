from django.db import models
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

# Create your models here.

STATUS_RESERVATION = (
    (1, _("Reserved")),
    (2, _("Bought")),
)

STATUS_PLAY = (
    (1, _("Распроданы")),
    (2, _("Свободно")),
)
class Carousel(models.Model):
    image = models.ImageField()

class Play(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    image = models.ImageField()
    text = models.TextField()
    tickets = models.PositiveIntegerField()
    status = models.IntegerField(choices=STATUS_PLAY, default=2)
    date = models.DateTimeField(default=timezone.now)
    def save(self, *args, **kwargs):
        if self.tickets == 0:
            self.status = 1
        elif self.tickets > 0:
            self.status = 2
        super().save(*args, **kwargs)


class Reservation(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    email = models.EmailField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS_RESERVATION, default=1)

    def save(self, *args, **kwargs):
        self.play.tickets -= self.amount
        self.play.save()
        send_mail(
            subject=f'Бронирование на спектакль {self.play.name}',
            message=f'Вы забронировали {self.amount} билетов на спектакль {self.play.name}.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.email],
            fail_silently=False,
            )
        return super().save(*args, **kwargs)
        
class Feedback(models.Model):
    email = models.EmailField(null=False, blank=False)
    text = models.TextField()

        

