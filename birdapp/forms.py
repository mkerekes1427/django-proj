from django.forms import ModelForm, DateField, ValidationError
from .models import Observation
from .my_validators import _valid_pic
from django.contrib import messages

class ObservationForm(ModelForm):

    class Meta:
        model = Observation
        exclude = ["person", "color"]


    def clean(self):

        cleaned_data = super(ObservationForm, self).clean()

        cleaned_data["name"] = cleaned_data["name"].title()
        
        try:
            pic = cleaned_data["picture"]
        except:
            raise ValidationError("")
        
        print(cleaned_data)
        
        return cleaned_data



