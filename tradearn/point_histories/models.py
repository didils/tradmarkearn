from django.db import models
from tradearn.users import models as user_models

class Point_history(models.Model):
    
    STATUS_CHOICES = (
        ('적립','적립'),
        ('사용','사용')
    )
    
    owner = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    point_name = models.CharField(max_length=80, null=True, blank=True)
    add_date = models.DateField(auto_now_add=True)
    change_amount = models.PositiveSmallIntegerField(blank=True, null=True)
    use_status = models.CharField(max_length=80, choices=STATUS_CHOICES, blank=True, null=True)

    
    def __str__(self):
        return '유저: {} - {} {}'.format(self.owner.username, self.use_status, self.change_amount)