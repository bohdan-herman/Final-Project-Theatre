from django import forms
from .models import Play, Reservation, Carousel
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
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get["amount"]
        play_id = self.request.POST.get("play_id")

        try:
            play = Play.objects.get(id=play_id)

        except Play.DoesNotExist:
            raise ValidationError('Play does not exist')
        
        if play.tickets < amount:
            raise ValidationError("Not enough tickets")
        
        self.instance.play = play
        return cleaned_data
    
class CarouselForm(forms.Model):
    class Meta:
        model = Carousel
        fields = ["image"]       
