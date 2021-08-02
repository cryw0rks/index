from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

P_WORK_TYPE = (
    (0, "Personal"),
    (1, "Commission")
)

P_TYPE = (
    (0, "Game Development"),
    (1, "Web Development"),
    (2, "Web Design"),
    (3, "UI/UX"),
    (4, "API"),
    (5, "Web Slicing")
)

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    thumbnail = models.ImageField(upload_to='storage/image/%Y/%m/%d/', blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_projects')
    work_year = models.CharField(max_length=200)
    work_type = models.IntegerField(choices=P_WORK_TYPE, default=0)
    project_type = models.IntegerField(choices=P_TYPE, default=0)
    url = models.CharField(max_length=256)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    logo = models.ImageField(upload_to='storage/image/%Y/%m/%d/', blank=True)
    logo_fa = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_services')
    description = models.TextField()
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return self.title

class Banner(models.Model):
    title = models.CharField(max_length=200, unique=True)
    thumbnail = models.ImageField(upload_to='storage/banner', blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_banners')
    description = models.TextField()
    url = models.CharField(max_length=255, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return self.title