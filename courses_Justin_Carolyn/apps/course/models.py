from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CommentManager(models.Manager):
    def addComment(self, postData):
        try:
            if len(postData["comment"]) == 0:
                return (False, "Comment cannot be empty!")
        except KeyError:
            return (False, "Comment cannot be empty!")
        try:
            if len(postData["name"]) == 0:
                postData["name"] = "Anonymous"
                print "postData['name']", postData["name"]
        except KeyError:
            print "KeyError"
        # return (True, Comment.objects.create())
        return (False, "work in progress!")
    def removeComment(self, postData):
        pass;


class Comment(models.Model):
    name = models.CharField(max_length=45)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course)
    objects = CommentManager()
