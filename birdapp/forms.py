from django.forms import ModelForm, ValidationError
from .models import Observation
import string


class ObservationForm(ModelForm):

    class Meta:
        model = Observation
        exclude = ["person", "color"]


    def clean(self):

        cleaned_data = super(ObservationForm, self).clean()

        cleaned_data["name"] = string.capwords(cleaned_data["name"])
        
        try:
            pic = cleaned_data["picture"]
        except:
            raise ValidationError("")
        
        return cleaned_data



