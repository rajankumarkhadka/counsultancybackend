from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from filehub.fields import ImagePickerField


class Blog(models.Model):
    category = models.CharField(max_length=200, db_index=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField(db_index=True)
    image = ImagePickerField(upload_to="blogs/")
    slug = models.SlugField(unique=True, blank=True, max_length=255, db_index=True)

    class Meta:
        ordering = ['-published_date', 'title']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        indexes = [
            models.Index(fields=['-published_date']),
            models.Index(fields=['category', '-published_date']),
        ]

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
