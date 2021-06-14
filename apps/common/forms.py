from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.userprofile.models import Profile, Session

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'phone_number',
            'birth_date',
            'profile_image'
        ]



ACCOUNT_TYPE = (('', 'Select Account Type...'),
                ('Standart/Netted', 'Standart/Netted'),
                ('Standart/Netted', 'Standart/Netted'))

SELECT_PAIRS = (('', 'Select Pairs...'),
                ('AUD/USD', 'AUD/USD'),
                ('EUR/USD', 'EUR/USD'))

# SELECT_PAIRS = (
#                 ('2', 'AUD/USD'),
#                 ('2', 'AUD/USD'),
#                 ('2', 'AUD/USD'),
#                 ('2', 'AUD/USD'),
#                 ('3', 'EUR/USD'))

class SessionForm(forms.ModelForm):
    # strategy_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Strategy'}), required=True)
    strategy_name = forms.CharField(required=True)
    equity = forms.IntegerField(required=True)
    leverage = forms.IntegerField(required=True)
    most_recent_data = forms.BooleanField(required=False)
    tick_volume = forms.BooleanField(required=False)
    min_timeframe = forms.BooleanField(required=False)
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE, required=True)
    select_pairs = forms.ChoiceField(choices=SELECT_PAIRS, required=True)
    # select_pairs = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.SelectMultiple,
    #     choices=SELECT_PAIRS,
    # )
    simulation_start_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ), required=True
    )
    class Meta:
        model = Session
        fields = ["strategy_name",
                  "user",
                  "equity",
                  "leverage",
                  "account_type",
                  "select_pairs",
                  "simulation_start_date",
                  "most_recent_data",
                  "tick_volume",
                  "min_timeframe"
                  ]
        # widgets = {
        #     'strategy_name': forms.TextInput(attrs={
        #         'id': 'post-text',
        #         'required': True,
        #         'placeholder': 'Strategy'
        #     }),
        # }