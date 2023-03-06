from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = RichTextField(blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    img = CloudinaryField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["id", "-updated_on", "-created_on"])]
        ordering = ["-updated_on", "-created_on"]

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("projects:project_detail", kwargs={"slug": self.slug})
