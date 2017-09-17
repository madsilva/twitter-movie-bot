from django import forms

class TwitterUserForm(forms.Form):
    twitter_user = forms.ChoiceField(choices=[('POTUS', 'Donald Trump (@POTUS)'), ])




