from django.db import models


class Design(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


class Step(models.Model):
    description = models.CharField(max_length=80)

    def __str__(self):
        return self.description


class Process(models.Model):
    name = models.CharField(max_length=200)
    steps = models.ManyToManyField(Step, through='ProcessStep')

    def __str__(self):
        return self.name


class ProcessStep(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.order}: {self.step}'


class Review(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    process = models.ForeignKey(Process, null=True, blank=True, on_delete=models.SET_NULL)
    step = models.ForeignKey(
        Step,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def steps_for_process(self):
        return self.process.processstep_set.order_by('order')

    def __str__(self):
        return f'{self.process} {self.design}'
