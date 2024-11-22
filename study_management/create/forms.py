from django import forms
from .models import createstudy

class createstudyform(forms.ModelForm):
    Sponsor_Name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'list': 'sponsor_list'})  # link to datalist
    )

    class Meta:
        model = createstudy
        fields = "__all__"
      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        sponsors = createstudy.objects.values_list('Sponsor_Name', flat=True).distinct()
        
        self.sponsors = sponsors
