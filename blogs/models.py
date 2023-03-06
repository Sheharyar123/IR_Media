from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    slug = models.SlugField()
    subject = models.CharField(max_length=255)
    body = RichTextField()
    is_active = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True)
    img = CloudinaryField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_on", "-created_on"]

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.subject)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("blogs:post_detail", kwargs={"slug": self.slug})
