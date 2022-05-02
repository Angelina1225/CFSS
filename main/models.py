from django.db import models

# Create your models here.
class user(models.Model):
    email_addr = models.TextField()
    pswd = models.TextField()

class files(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE)
    title = models.TextField()
    folder = models.ForeignKey('folder', on_delete=models.CASCADE, default=0)
    file_size = models.TextField()
    file_link = models.TextField()

class shared(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE, related_name='owner')
    sharedUser = models.ForeignKey('user', on_delete=models.CASCADE, related_name='share_holder')
    file = models.IntegerField()
    is_folder = models.BooleanField(default=False)

class folder(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE)
    folder_name = models.TextField()
    folder_link = models.TextField()
    parent = models.ForeignKey('folder', on_delete=models.CASCADE)