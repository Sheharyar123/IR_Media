# from django.db import models
# from django.contrib.auth import get_user_model
# from courses.models import Enrollment

# User = get_user_model()


# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     user_course = models.ForeignKey(Enrollment, on_delete=models.SET_NULL, null=True)
#     order_id = models.CharField(max_length=250, blank=True)
#     amount = models.DecimalField(max_digits=6, decimal_places=2)
#     status = models.CharField(max_length=50, null=True, blank=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.name} - {self.amount}"
