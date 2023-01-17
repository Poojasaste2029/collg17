from django.db import models

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

# Create your models here.
class student_register(models.Model):
    fname=models.CharField(max_length=20,blank=True,verbose_name="First name",help_text="First name")
    lname=models.CharField(max_length=20,verbose_name="Last_name",help_text="Last_name")
    email=models.EmailField(help_text="Email Address")
    password1=models.CharField(max_length=6)
    password2=models.CharField(max_length=6)
    gender=models.CharField(max_length=10,choices=GENDER)
    color=models.CharField(max_length=10,choices=COLOURS)

