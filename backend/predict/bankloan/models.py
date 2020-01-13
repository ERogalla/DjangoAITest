from django.db import models

class bankloan(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    MARRIED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    GRADUATED_CHOICES = (
        ('Graduated', 'Graduated'),
        ('Not Graduated', 'Not Graduated')
    )
    SELFEMPLOYMENT_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban'),
    )

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    dependents = models.IntegerField()
    applicantincome = models.IntegerField()
    coapplicantincome = models.IntegerField()
    coapplicantincome = models.IntegerField()
    loanamt = models.IntegerField()
    loanterm = models.IntegerField()
    credithistory = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    married = models.CharField(max_length=20, choices=MARRIED_CHOICES)
    graduated = models.CharField(max_length=20, choices=GRADUATED_CHOICES)
    selfemployment = models.CharField(max_length=20, choices=SELFEMPLOYMENT_CHOICES)
    area = models.CharField(max_length=20, choices=PROPERTY_CHOICES)

    def __str__(self):
        return self.firstname, self.lastname