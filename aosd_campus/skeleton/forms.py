from django import forms
from .models import ConnectionLink

# Form for Let's Connect
class ConnectionForm(forms.ModelForm):
    class Meta:
        model = ConnectionLink
        fields = ('name','email', 'phone','interest')
        widgets = {
          'interest': forms.Textarea(attrs={'rows':1, 'cols':27}),

        }
        labels = {
            'phone': "Phone (Optional)",
            'email': "E-mail",
            'interest': "What are you interested in?"
        }

class BibleStudyForm(forms.ModelForm):
    class Meta:
        model = ConnectionLink
        fields = ('name','email','phone')
        exclude = ('interest',)
        labels = {
            'phone': "Phone (Optional)",
            'email': "E-mail",
        }
