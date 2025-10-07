from django import forms
from .models import Play, Reservation, Carousel, Feedback
from django.core.exceptions import ValidationError

class PlayForm(forms.ModelForm):
    class Meta:
        model = Play
        fields = ['name', 'price', 'image', 'text', 'tickets']
    
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['email', 'amount']
    
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        super().__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get("amount") 

        try:
            play = Play.objects.get(id=self.pk)

        except Play.DoesNotExist:
            raise ValidationError('Play does not exist')
        
        if play.tickets < amount:
            raise ValidationError("Not enough tickets")
        
        if play.status == 1:
            raise ValidationError("Tickets are already bought")
        
        self.instance.play = play
        return cleaned_data
    
class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ["image"]       


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["email", "text"]