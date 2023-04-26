from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Instructor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    instructors = models.ManyToManyField(Instructor, blank=True, related_name="courses")
    students = models.ManyToManyField("Student", blank=True, related_name="courses")
    image = models.ImageField(upload_to="courses/course_images", null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField("Is Active", default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
