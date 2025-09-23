from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()

    class Meta:
        db_table = 'todos'