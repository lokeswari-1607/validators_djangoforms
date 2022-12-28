from django.core import validators
from django import forms
#  Normal vadilators function
def check_for_s(value):
    if value[0].lower()=='s':
        raise forms.ValidationError('not started with s')

def check_for_len(v):
     if len(v)<=3:
         raise forms.ValidationError('len is < than 3')

class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_s])
    fathername=forms.CharField(max_length=100,validators=[check_for_len])
    email=forms.EmailField()
    reemail=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    # By using Built-in-validators
    mobile=forms.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    # By using form class object method with clean method
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reemail']
        if e!=re:
            raise forms.ValidationError('email not matched')


    # By using form class object method with clean_element
    def botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>=0:
            raise forms.ValidationError('botcatched')

    