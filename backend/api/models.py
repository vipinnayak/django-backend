from django.db import models

class Insurance(models.Model):
    policy_number = models.CharField(max_length=6)
    witnesses = models.IntegerField()
    police_report = models.CharField(max_length=10)
    loss_type = models.CharField(max_length=10)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.policy_number} - {self.status}"

