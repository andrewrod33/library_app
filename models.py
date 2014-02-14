from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=255, unique=True)


    def __unicode__(self):
        return "%s by %s, %s" %(self.title, self.author, self.isbn)


