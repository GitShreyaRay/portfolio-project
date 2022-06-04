from django.db import models

# Create blog model here.
#title
#pub_date
#body
#image

class Blog(models.Model):
  title = models.CharField(max_length=100)
  pub_date = models.DateTimeField(auto_now=True)
  body = models.TextField()
  image = models.ImageField(upload_to='images/')
# Add the Blog app to the settings

# create a migration

# Migrate

# Add to the admin
