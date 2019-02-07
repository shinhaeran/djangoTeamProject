from django.db import models
from django.contrib.auth.models import AbstractUser
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields


class Post(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    # title = models.CharField(max_length=200)
    text = models.TextField()
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE )


class User(AbstractUser):
    class Meta:
        permissions = [
            ['can_view_post', 'Can view post'],
            ['hi', 'hi'],
        ]


class SummerNote(summer_model.Attachment):
    summer_field = summer_fields.SummernoteTextField(default='')
    



