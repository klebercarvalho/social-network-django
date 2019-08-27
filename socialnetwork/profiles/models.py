from django.db import models

# Create your models here.

class Profile(models.Model):

    name = models.CharField(max_length=255, name=False)
    email = models.CharField(max_length=255, name=False)
    phone = models.CharField(max_length=15, name=False)
    company = models.CharField(max_length=255, name=False)

    def invite(self, profile_invited):
        invite = Invite(sender=self, receiver=profile_invited)
        invite.save()

class Invite(models.Model):
    sender = models.ForeignKey(Profile, related_name="invites_sent")
    receiver =models.ForeignKey(Profile, related_name="invites_received")

