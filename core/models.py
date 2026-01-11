from django.db import models


class PromptTest(models.Model):
    prompt = models.TextField()
    response = models.TextField()
    attack_type = models.CharField(max_length=100)
    is_secure = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.attack_type
