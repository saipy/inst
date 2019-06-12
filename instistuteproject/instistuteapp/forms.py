from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your Name'



            }
        )
    )

    rating=forms.IntegerField(
        label="Enter your rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'rating'



            }
        )
    )

    feedback=forms.CharField(
        label="Enter your feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'your feedback'



            }
        )
    )
