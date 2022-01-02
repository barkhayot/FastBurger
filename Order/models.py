from django.db import models
from Meal.models import Food 



class testOrderType(models.Model):
    Order_Class = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Order_Class

 
class testOrder(models.Model):
    food    = models.ForeignKey(Food, on_delete=models.CASCADE)
    count   = models.IntegerField(default=1)
    price   = models.FloatField()
    order_t = models.ForeignKey(testOrderType,  on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    Completed_Status = 1
    UnCompleted_Status = 0
    STATUS_CHOICES = (
        (Completed_Status, 'Completed'),
        (UnCompleted_Status, 'Uncompleted'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=UnCompleted_Status)
    
    def __str__(self):
        return self.food.food_name
