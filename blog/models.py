from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from filehub.fields import ImagePickerField  # if using your same image field

# --- Blog Type / Category ---
class BlogType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# --- Blog Model ---
class Blog(models.Model):
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=200)
    description = HTMLField()  # TinyMCE rich text
    published_date = models.DateField()
    image = ImagePickerField(upload_to='blogs/')
    slug = models.SlugField(unique=True,auto_created=True, blank=False, max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
