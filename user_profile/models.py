from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.utils.text import slugify
 
# Create your models here.

def upload_location(instance, filename):
	extension = filename.split('.')[-1]
	path = "profile_images"
	return "%s/%s-%s.%s" %(path, instance.user.username, instance.id, extension)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    slug = models.SlugField(unique=True, default='')
    bio = models.TextField(verbose_name='About Me', default='', blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    email = models.TextField(blank=True, default='')
 
    def __unicode__(self):
        return self.user.username
 
    def get_absolute_url(self):
        return reverse("profile:detail", kwargs={"slug": self.user.username})

    def save(self, *args, **kwargs):
    	if not self.id:
    		self.slug = slugify(self.user.username)
    	super(UserProfile, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)
