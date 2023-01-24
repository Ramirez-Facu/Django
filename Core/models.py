from django.db import models

# About section

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/', height_field=None, width_field=None, max_length=None)
    
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.career
    
    
class profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)
    
    
    
#Skill section

class Category (models.Model):
    name = models.CharField(max_length=20)
    
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        
    def __str__(self) -> str:
        return self.name
    
class Skillss (models.Model):
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)
    
    
#Portfolio section

class Portfolio (models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
    
    def __str__(self) -> str:
        return f'Portfolio{self.id}'
    