from django.db import models

# Create your models here.
class Memo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    detail = models.TextField()
    date = models.DateTimeField(defalut=timezone.now)
    del_flag = models.BooleanField(default=False)

    def delete_memo(self):
        self.del_flag = True
        self.save()

    def __str__(self):
        return self.title

