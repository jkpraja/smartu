from django.db import models

# Create your models here.
class Course(models.Model):
    courseID = models.CharField(max_length=10)
    courseName = models.CharField(max_length=255)
    coursePrice = models.CharField(max_length=10)
    coursePaymentPeriod = models.CharField(max_length=10)

    def __str__(self):
        return self.courseName

