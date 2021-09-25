from django.db import models

class Tag(models.Model):
    tag = models.CharField(max_length=200)
        
    def __str__(self):
        return "{}".format(self.tag)

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return "{}.{}".format(self.id, self.title)