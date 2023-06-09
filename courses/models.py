import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

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
    CHOICES = (("FREE", "FREE"), ("PAID", "PAID"))
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    instructors = models.ManyToManyField(Instructor, blank=True, related_name="courses")
    students = models.ManyToManyField("Student", blank=True, related_name="courses")
    # image = models.ImageField(upload_to="courses/course_images", null=True, blank=True)
    image = models.URLField(max_length=2000, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    description = RichTextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    choice = models.CharField(choices=CHOICES, max_length=4, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField("Is Active", default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "courses:course_detail", kwargs={"course_slug": slugify(self.slug)}
        )

    @property
    def imageURL(self):
        if not self.image:
            return ""
        else:
            return self.image


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "course")

    def __str__(self):
        return f"{self.user.name} - {self.course.title}"


class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    video_url = models.URLField(max_length=500, null=True, blank=True)
    video = models.FileField(upload_to="course_videos", null=True, blank=True)
    download_link = models.FileField(upload_to="course_files", null=True, blank=True)
    order = models.IntegerField()

    class Meta:
        ordering = ["order"]

    @property
    def videoURL(self):
        if self.video_url:
            return self.video_url
        elif self.video.url:
            return self.video.url
        else:
            return ""
