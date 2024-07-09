from django.db import models

# Create your models here.
class home(models.Model):
  Title= models.CharField(max_length=300,default="")
  sub_title = models.CharField(max_length=300,default="")
  button1= models.CharField(default="", max_length=50)
  button2= models.CharField(default="", max_length=50)
  button3= models.CharField(default="", max_length=50)
  image=models.ImageField(upload_to='static/index', default='')

class container(models.Model):
   name=models.CharField(max_length=50)
   title=models.CharField(max_length=50)
   date=models.DateField( auto_now=False, auto_now_add=False)
   detail=models.TextField()
   image=models.ImageField(upload_to='static/title',default="")

   

class about(models.Model):
  title = models.CharField(max_length=300,default="")
  subtitle = models.CharField(max_length=300,default="")
  description = models.TextField()
  image=models.ImageField(upload_to='static/about', default='')


class Contact(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    subject = models.TextField()
    def __str__(self):
         return self.fname + self.lname
    


