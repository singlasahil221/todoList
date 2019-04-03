from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime

class BaseModel(models.Model):
    """
    Provides default timestamp model
    All models to extend this base class
    """
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.id

    def __unicode__(self):
        return "%s" % self.id



class Todo(BaseModel):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    is_completed = models.BooleanField(default = False)
    scheduled_at = models.DateTimeField(default = datetime.now)
    description = models.CharField(max_length=1000)

    class Meta:
        ordering = ['scheduled_at']


    def __str__(self):
        return self.description