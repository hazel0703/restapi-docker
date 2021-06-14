from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

#Model for projects, it will save the associated user
# creation date, a title, a url (it does exist), and a project description
class Education(models.Model):
    """Education model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ini = models.DateTimeField()
    date_end = models.DateTimeField(null=True)
    title = models.CharField(max_length=255)


    def __str__(self):
        """Return education and first_name and last_name."""
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'