from django.db import models

# Create your models here.

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class TaskManage(models.Model):
    description = models.CharField(max_length=200, blank=False, null=False, verbose_name="Описание")
    status = models.CharField(max_length=200, choices=status_choices, verbose_name="Статус")
    deadline = models.DateField(verbose_name='Дедлайн')
    detailed_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}. {self.description} {self.status} {self.deadline}"

    class Meta:
        db_table = "tasks list"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
