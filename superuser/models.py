from django.db import models


# Create your models here.
class lawyer(models.Model):
    lname = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    pdetail = models.CharField(max_length=700)
    experience = models.CharField(max_length=10)
    location = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.lname


class court(models.Model):
    courtname = models.CharField(max_length=50)

    def __str__(self):
        return self.courtname


class client(models.Model):
    cname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    dob = models.DateField()
    add = models.CharField(max_length=50)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    postalcode = models.IntegerField()
    court1=models.ForeignKey(court,on_delete=models.CASCADE)
    lawyername = models.ForeignKey(lawyer, on_delete=models.CASCADE)

    def __str__(self):
        return self.cname


class category(models.Model):
    catname = models.CharField(max_length=50)
    catdisc = models.TextField()

    def __str__(self):
        return self.catname


class case(models.Model):
    casename = models.CharField(max_length=30)
    casedate = models.DateField()
    catgname = models.ForeignKey(category, on_delete=models.CASCADE)
    clname = models.ForeignKey(client, on_delete=models.CASCADE)
    lawname = models.ForeignKey(lawyer, on_delete=models.CASCADE)
    court2 = models.ForeignKey(court, on_delete=models.CASCADE)

    def __str__(self):
        return self.casename


class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    address=models.TextField()
    password=models.CharField(max_length=100)
    profile_picture=models.ImageField(upload_to="profile_picture")


    def  __str__(self):
        return self.lname+" - "+self.lname