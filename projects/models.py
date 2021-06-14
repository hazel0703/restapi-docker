from django.db import models
from users.models import User

#This model will be for saving an associated user, start date 
#end date (field has null=True), company name, a description for jobs that the user has experience in

# django-ckeditor
from ckeditor.fields import RichTextField

class Project(models.Model):
    """Project model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.URLField(null=True)
    description = RichTextField()


    def __str__(self):
        """Return project title and first_name and last_name."""
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'