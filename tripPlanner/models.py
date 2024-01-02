from django.db import models
import datetime
import os

def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('images/',filename)

# Create your models here.
class Place(models.Model):
    locationId = models.IntegerField(primary_key=True)
    parentId = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_categories')
    name = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to=filepath,null=True,blank=True)

class Feedback(models.Model):
    feedbackId = models.IntegerField(primary_key=True)
    locationId = models.ForeignKey(Place, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
