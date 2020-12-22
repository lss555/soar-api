from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  title = models.CharField(max_length=100)
  date = models.DateField()
  text = models.CharField(max_length=1000)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The '{self.title}' blog says, {self.text}. It's id: {self.id}. made on: {self.date}."

  def as_dict(self):
    """Returns dictionary version of Blog models"""
    return {
        'id': self.id,
        'title': self.title,
        'text': self.text,
        'date': self.date
    }
