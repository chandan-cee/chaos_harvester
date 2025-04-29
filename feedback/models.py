from django.db import models

# Create your models here.
class Feedback(models.Model):
    user_name= models.CharField(max_length=100)
    email= models.EmailField()
    message= models.TextField()
    submitted_At= models.DateTimeField(auto_now_add=True)
    gpt_review = models.TextField(blank=True, null=True)
    needs_attention = models.BooleanField(default=False)



    def __str__(self):
        return f"{self.user_name} - {self.submitted_At.strftime('%Y-%m-%d')}"

