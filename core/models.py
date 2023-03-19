from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AitverFullProjectTeamMember(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='members_images', null=True)
    work_role = models.CharField(max_length=200)
    roll = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) -> str:
        return self.name

class ProjectFile(models.Model):
    file_name = models.CharField(max_length=200)
    file= models.FileField(upload_to='all_files')
    uploaded_by =models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.file_name