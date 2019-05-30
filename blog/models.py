from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

def gen_slug(clss,title):
    orig_slug = slugify(title)
    uniq_slug = orig_slug
    n = 1
    while clss.objects.filter(slug=uniq_slug).exists():
        uniq_slug = '{}-{}'.format(uniq_slug,n)
        n += 1
    return uniq_slug


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length=150,unique = True,blank=True)
    body = models.TextField(blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank = True,null=True)
    tags = models.ManyToManyField('Tag',blank = True)

    pub_date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return '{},{}'.format(self.title,self.author)

    def get_absolute_url(self):
        return reverse('post_detail_url',kwargs = {'slug':self.slug})

    def get_update_url(self):
        return reverse('post_update_url',kwargs = {'slug':self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url',kwargs = {'slug':self.slug})

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = gen_slug(Post,self.title)
        super().save(*args,**kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=150,unique = True,blank=True)
    slug = models.SlugField(max_length = 150,unique = True,blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag_detail_url',kwargs = {'slug':self.slug})

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = gen_slug(Tag,self.title)
        super().save(*args,**kwargs)


class Comment(models.Model):
    text = models.CharField(max_length = 150)
    author = models.ForeignKey(User,on_delete = models.CASCADE,blank = True,null=True)
    post= models.ForeignKey('Post',on_delete = models.CASCADE, blank = True,null=True)

    pub_date = models.TimeField(auto_now_add = True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text

    def get_delete_url(self):
        return reverse('comment_delete_url',kwargs = {'id':self.id})
