# Generated by Django 3.0.2 on 2020-01-06 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankloan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('dependents', models.IntegerField()),
                ('applicantincome', models.IntegerField()),
                ('coapplicantincome', models.IntegerField()),
                ('loanamt', models.IntegerField()),
                ('loanterm', models.IntegerField()),
                ('credithistory', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('married', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('graduated', models.CharField(choices=[('Graduated', 'Graduated'), ('Not Graduated', 'Not Graduated')], max_length=20)),
                ('selfemployment', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('area', models.CharField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')], max_length=20)),
            ],
        ),
    ]
