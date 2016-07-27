from __future__ import unicode_literals
from django.db import models


class contact(models.Model):
    name=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    gender=models.CharField(max_length=1,choices=(('m','male'),('f','female')))
    typecontact=models.CharField(max_length=1,choices=(('p','person'),('f','business')))
    def __unicode__(self):
        return "%s %s" % (self.name,self.family)



class contact_phone(models.Model):
    phone=models.CharField(max_length=12)
    contact=models.ForeignKey(contact)
    
    def __unicode__(self):
        return self.phone

