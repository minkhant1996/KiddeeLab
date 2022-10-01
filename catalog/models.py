from django.db import models

# Create your models here.
##################################################
class Category(models.Model):
    """Model representing a product category."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

#################################################
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class Teacher(models.Model):
    """Model representing an Manufacturer."""
    name = models.CharField(max_length=100)
    work_experience = models.TextField(max_length=1000, help_text='Enter the work experience')
    education = models.TextField(max_length=1000, help_text='Enter the background education')

    def get_absolute_url(self):
        """Returns the URL to access a particular Teacher instance."""
        return reverse('teacher_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

#####################################################
class Location(models.Model):
    """Model representing a book (but not a specific copy of a product)."""
    name = models.CharField(max_length=100)

    Address = models.TextField(max_length=1000, help_text='Enter the address')

    Ph = models.TextField(max_length=30, help_text='Enter the phone number')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for location."""
        return reverse('location-detail', args=[str(self.id)])

##################################################
class Age_recommend(models.Model):
    """Model representing a product category."""
    age_limit = models.CharField(max_length=30)

    def __str__(self):
        """String for representing the Model object."""
        return self.age_limit

##################################################
class Duration(models.Model):
    """Model representing a product category."""
    duration = models.CharField(max_length=20)

    def __str__(self):
        """String for representing the Model object."""
        return self.duration

######################################################
class Course(models.Model):
    """Model representing a course."""
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'media/', default = 0)
    price = models.TextField(max_length = 10, help_text='Enter the price')
    category = models.ManyToManyField(Category)
    age_recommend = models.ManyToManyField(Age_recommend)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the Course')
    duration = models.ForeignKey('Duration', on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this product."""
        return reverse('course-detail', args=[str(self.id)])
        
    def display_category(self):
        """Create a string for the Category. This is required to display category in Admin."""
        return ', '.join(category.name for category in self.category.all()[:3])

    def display_age_recommend(self):
        """Create a string for the Category. This is required to display age recommendation in Admin."""
        return ', '.join(age_recommend.age_limit for age_recommend in self.age_recommend.all()[:3])

    display_category.short_description = 'Category'
    display_age_recommend.short_description = 'Age_Recommend'