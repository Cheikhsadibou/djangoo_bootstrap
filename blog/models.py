from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DetailCar(models.Model):
  nom = models.CharField(max_length=120)
  resumer = models.TextField(blank=True)
  contenu = models.TextField(blank=True)
  auteur = models.CharField(max_length=60)
  date_creer = models.DateField()
  images = models.ImageField(upload_to='images/', blank=True, null=True)
  date_mise_en_vente = models.DateTimeField(null=True)
  users = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    
  
    
  def __str__(self) :
      # return self.list_car
      return str(self.nom)
    
class UserInput(models.Model):
  titre = models.CharField(max_length=150, null=True, blank=True)
  resume = models.TextField(blank=True)
  contenu = models.TextField()
  auteur = models.CharField(max_length=60)
  date_de_creation = models.DateField()
  date_mise_a_jour = models.DateField(null=True)
  miniature = models.ImageField(upload_to='images/', blank=True, null=True)
  users = models.ForeignKey( User, on_delete=models.CASCADE, blank=True, null=True)  
  
      
  def __str__(self):
      return self.titre
