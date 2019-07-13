from django import forms
class addressform(forms.Form):
    name=forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'your name',
                'class':'form-control',

            }
        )
    )
    mobileno=forms.IntegerField(
        label='Enter your mobile no',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'your no',
                'class':'form-control',
            }
        )
    )
    city=forms.CharField(
        label="Enter your city",
        widget=forms.TextInput(
            attrs={
                'placeholder':'your city',
                'class':'form-control',
            }
        )
    )
    address=forms.CharField(
        label="Enter your address",
        widget=forms.Textarea(
            attrs={
                'placeholder':'your address',
                'class':'form-control',

            }
        )
    )