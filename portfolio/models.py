import sys
from django.db import models
from django.contrib.auth.models import User

from PIL import Image

PROJECT_IMAGE_SIZE = 600
PROJECT_PROFILE_SIZE = 450


class Profile(models.Model):
    name = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(help_text='452x588px recommmended', upload_to='portfolio/profile_pics')
    title = models.CharField(max_length=100, blank=True)
    linkedin_url = models.CharField(max_length=100, blank=True)
    github_url = models.CharField(max_length=50, blank=True)
    cv_link = models.FileField(upload_to='portfolio/resume/')
    cv_link_external = models.CharField(max_length=100, blank=True)
    about_me = models.CharField(max_length=500, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # # Override the save function in Profile class:
    # def save(self, *args, **kwargs):
    #     # run the parent class' save() function:
    #     super().save(*args, **kwargs)
    #
    #     # open the image of the current instance:
    #     image = Image.open(self.image.path)
    #
    #     if image.height > PROJECT_PROFILE_SIZE or image.width > PROJECT_PROFILE_SIZE:
    #         image = image.resize((PROJECT_IMAGE_SIZE, PROJECT_IMAGE_SIZE), Image.ANTIALIAS)
    #         image.save(self.image.path)




class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now=True)
    repo_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    external_link = models.URLField(blank=True)

    image = models.ImageField(upload_to='portfolio/images/')
    tech_and_tools = models.ManyToManyField('TechAndTools', related_name='techandtools')

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):

        super(Project, self).save(force_insert, force_update)

        image = Image.open(self.image.path)
        if image.height > PROJECT_IMAGE_SIZE or image.width > PROJECT_IMAGE_SIZE:
            image = image.resize((PROJECT_IMAGE_SIZE, PROJECT_IMAGE_SIZE), Image.ANTIALIAS)
            image.save(self.image.path)


class TechAndTools(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    score = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author




