from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    course_type = models.CharField(max_length=10)

    def str(self):
        return self.name
