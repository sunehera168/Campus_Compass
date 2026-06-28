from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class InstituteInfo(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    description = models.TextField()
    location = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    contact = models.TextField()
    status_choices = (
        ('Closed', 'Closed'),
        ('Apply', 'Apply')
    )
    status = models.CharField(max_length=50, choices=status_choices, default='Closed')

    def __str__(self):
        return self.title

class InstituteImage(models.Model):
    institute = models.ForeignKey(InstituteInfo, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='institutes/')

    def __str__(self):
        return f"Image for {self.institute.title}"
