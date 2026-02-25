from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from filehub.fields import ImagePickerField


class Blog(models.Model):
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField()
    image = ImagePickerField(upload_to="blogs/")
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            i = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
