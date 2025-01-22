from django.db import models
from django.utils import timezone
class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
    
    
    def delete(self,using=None, soft=True, *args, **kwargs):
        if soft:
            self.deleted_at = now()
            self.save()
        else:
            super().delete(using=using,*args, **kwargs)

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(blank=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        if self.pk:
            self.updated_at = now()
        super().save(*args, **kwargs)