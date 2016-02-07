from captcha.fields import ReCaptchaField
from django import forms
from django.utils.translation import ugettext_lazy as _


class EmailForm(forms.Form):
    firstname = forms.CharField(label=_("Vorname"), max_length=255)
    lastname = forms.CharField(label=_("Nachname"), max_length=255)
    email = forms.EmailField(label=_("E-Mail"))
    subject = forms.CharField(label=_("Betreff"), max_length=255)
    captcha = ReCaptchaField()
    message = forms.CharField(label=_("Deine Nachricht"), widget=forms.Textarea)
