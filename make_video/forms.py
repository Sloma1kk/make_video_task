from django import forms


class TextInputForm(forms.Form):
    user_text = forms.CharField(
        label='',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'input-field'})
    )
