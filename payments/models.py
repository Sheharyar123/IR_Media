from django.db import models
from django.contrib.auth import get_user_model
from courses.models import UserCourse

User = get_user_model()


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_course = models.ForeignKey(UserCourse, on_delete=models.SET_NULL, null=True)
    stripe_payment_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.amount}"
