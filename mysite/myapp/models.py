from django.db import models
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

# Create your models here.

STATUS_CHOIСES = (
    (1, _("Reserved")),
    (2, _("Bought")),
)


class Carousel(models.Model):
    image = models.ImageField()

class Play(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    image = models.ImageField()
    text = models.TextField()
    tickets = models.PositiveIntegerField()
    date = models.DateTimeField(default=timezone.now)

class Reservation(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    email = models.EmailField()
    status = models.IntegerField(choices=STATUS_CHOIСES, default=1)

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
    email = models.EmailField()
    text = models.TextField()

        

