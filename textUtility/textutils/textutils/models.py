from django.db import models

class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.message_id