from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


"""
django model field :
    html widget
    validation
    db size
"""
JOB_TYPE=(
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),
)
def image_upload(instance,filename):
    image_name , extention=filename.split('.')
    return 'photos/%s/%s.%s'%(instance.id,instance.id,extention)
class Job(models.Model): #table
    owner=models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title=models.CharField(max_length=100) #column
    #local
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    experience=models.IntegerField(default=1)
    image=models.ImageField(upload_to=image_upload)
    slug=models.SlugField(blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title
        
class Category(models.Model):
    name=models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

class Apply(models.Model):
    job=models.ForeignKey(Job,related_name='apply',on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=100)
    portfolio_url=models.URLField()
    cv=models.FileField(upload_to='apply/',null=True)
    cover_letter=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name

