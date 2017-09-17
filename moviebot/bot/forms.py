from django import forms

class TwitterUserForm(forms.Form):
    twitter_user = forms.ChoiceField(label='Choose a twitter user', choices=[('POTUS', 'Donald Trump (@POTUS)'), ('realdonaldtrump', 'Donald Trump (@realDonaldTrump)'), ('BarackObama', 'Barack Obama (@BarackObama)'), ('HillaryClinton', 'Hillary Clinton (@HillaryClinton)'), ('uiowa', 'University of Iowa (@uiowa)')])




