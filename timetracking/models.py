from django.db import models

from django.db import models

class TimeLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return f"Log {self.log_id} on {self.date}"
