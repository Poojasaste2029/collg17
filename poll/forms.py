from django import forms
from django.core import validators
from .models import student_register

GENDER=[
    ('Male','Male'),
    ('FeMale','FeMale'),
    ('other','other')
]
COLOURS=[
    ('',"--Select--"),
    ('RED','Red',),
    ('PINK','Pink'),
    ('ORANGE','Orange'),
    ('BLACK','Black'),
    ('WHITE','White'),

]

# class Registration(forms.Form):
#     fname=forms.CharField(label='First name')
#     # l_name=forms.CharField(name_starts_with(value='l_name'))
#     lname=forms.CharField()
#     email=forms.EmailField()
#     password1=forms.CharField(label='Set password')
#     password2=forms.CharField(label='Confirm password')
#     gender=forms.CharField(widget=forms.RadioSelect(choices=GENDER))
#     color=forms.CharField(widget=forms.SelectMultiple(choices=COLOURS))

# slide 35-3
# 2-validation of complete Django from  at once
    # def clean(self):
    #     valname=super().clean()
    #     nm =self.cleaned_data['fname']
    #     if len(nm)  <4:
    #         raise forms.ValidationError("Name should be grater than 4")

    #     lmn =self.cleaned_data['lname']
    #     if len(lmn) <5:
    #         raise forms.ValidationError("Name should be grater than 5")

    # def clean(self):
    #     val=super().clean()
    #     pwd1=self.cleaned_data['password1']
    #     pwd2=self.cleaned_data['password2']

    #     if pwd1 != pwd2:
    #         raise forms.ValidationError("password does not match try another")

# custom password
# def name_starts_with(value):
#     if value[0] !='r':
#         raise forms.ValidationError("name should not be start with r")

#3- using meta class

# class Registration(forms.ModelForm):
#     class Meta:
#         model=student_register
#         fields="__all__"



#  4- using built in validators

# class Registration(forms.Form):
#     f_name=forms.CharField(label='First name',
#                            validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(6)])
#     lname=forms.CharField(validators=[validators.MinLengthValidator(4)])
#     email=forms.EmailField()
#     password1=forms.CharField(label='Set password',validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(6)])
#     password2=forms.CharField(label='Confirm password')
#     gender=forms.CharField(widget=forms.RadioSelect(choices=GENDER))
#     colours=forms.CharField(widget=forms.SelectMultiple(choices=COLOURS))

  
  #3- using meta class

class Registration(forms.ModelForm):
    class Meta:
        model=student_register
        fields="__all__"

        # fields=['fname','lname']
        # exclude=['lname']
        labels={
            'fname':"user first name",
            'lname':"user last name",
            'email':'Email address',

        }
        error_messages={
            "fname":{"required":"user first name is requires"},
            "lname":{"required":"user last name is requires"},
            "email":{"required":"user email is requires"},
            "password1":{"required":"password is must"},
            "password2":{"required":"confirm password is must"},
            }
        
        help_texts={
            'fname':"user first name",
            'lname':"user last name",
            'email':'Email address',
            'password1':'Set password',
            'password2':'Confirm password',

        }

        widgets={
            "email":forms.EmailInput(),
            "password1":forms.PasswordInput(),
            "password2":forms.PasswordInput(),

        }

            

        

    