# Generated by Django 4.1.4 on 2023-01-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_register',
            name='color',
            field=models.CharField(choices=[('', '--Select--'), ('RED', 'Red'), ('PINK', 'Pink'), ('ORANGE', 'Orange'), ('BLACK', 'Black'), ('WHITE', 'White')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student_register',
            name='email',
            field=models.EmailField(help_text='Email Address', max_length=254),
        ),
        migrations.AlterField(
            model_name='student_register',
            name='fname',
            field=models.CharField(blank=True, help_text='First name', max_length=20, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='student_register',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('FeMale', 'FeMale'), ('other', 'other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student_register',
            name='lname',
            field=models.CharField(help_text='Last_name', max_length=20, verbose_name='Last_name'),
        ),
    ]