from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER_DEF = (
        ('male','MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER')
)

class Profile(models.Model):
    user_id     = models.OneToOneField(User, on_delete = models.CASCADE , primary_key = True)
    profession  = models.CharField(max_length = 50)
    gender      = models.CharField(max_length = 10, choices = GENDER_DEF, default = 'Select')
    profile_img = models.ImageField(default = 'default.png', upload_to = 'profile_pics', blank = True, null = True)
    website     = models.CharField(max_length = 50, null=True)
    mobile      = models.IntegerField(null = True)
    location    = models.CharField(max_length = 30, null = True,)

    def __str__(self):
        # return self.username
        return '{}'.format(self.user_id)

    class Meta:
        verbose_name = 'User Details'
        verbose_name_plural = 'Profile Table'

class Post(models.Model):
    author_id       = models.ForeignKey(Profile, on_delete = models.CASCADE)
    title           = models.CharField(max_length = 50, verbose_name='Post Title',)
    about           = models.CharField(max_length = 100)
    article         = models.TextField()
    publish_date    = models.DateTimeField(null = True)
    modified_date   = models.DateTimeField(null = True)
    article_img     = models.ImageField(default = 'default.gpg', upload_to = 'article_pics', blank = True, null = True)
    thumbs_up       = models.IntegerField(null = True)
    thumbs_down     = models.IntegerField(null = True)
    view_count      = models.IntegerField(default = 0)
    def __str__(self):
        return '{}'.format(self.title)

class Comment(models.Model):
    user_id  = models.ForeignKey(User, on_delete = models.CASCADE)
    article  = models.ManyToManyField(Post)
    comment  = models.TextField()
    liked    = models.BooleanField(default=False)
    disliked = models.BooleanField(default=False)

    def __str__(self):
        return self.comment
