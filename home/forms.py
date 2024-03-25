from django.forms import ModelForm
from .models import rnaseq 

class UpModelForm(ModelForm):
   

    class Meta:
        model = rnaseq
        fields = "__all__"

