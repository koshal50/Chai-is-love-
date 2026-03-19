from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class chaiVariety(models.Model):
    CHAI_TYPE_CHOICE=[
            ('black','Black Tea'),
            ('green','Green Tea'),
            ('herbal','Herbal Tea'),
            ('oolong','Oolong Tea'),
            ('white','White Tea'),
            ('pu-erh','Pu-erh Tea'),
            ('rose','Rose Tea'),
            ('ginger','Ginger Tea'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=200, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    prices = models.DecimalField(max_digits=6, decimal_places=2,default='0.00')    

    def __str__(self):
        return self.name # k  returns the name of the chai variety when the object is printed
    
class CHaiReview(models.Model):
    chai = models.ForeignKey(chaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 8)])
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['chai', 'user']  # Optional: one review per user per chai
    
    def __str__(self):
        return f"{self.user.username} - {self.chai.name} ({self.rating}★)"
    
#many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(chaiVariety, related_name='stores')

    def __str__(self):
        return self.name
    
#one to one

class Certificate(models.Model):
    chai = models.OneToOneField(chaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=50)
    issued_date = models.DateTimeField(default=timezone.now)
    valid = models.DateTimeField()

    def __str__(self):
        return self.chai.name
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} <{self.email}>"
    
class about_description(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, default='')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100, default='General')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title