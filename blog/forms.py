from django import forms
from django.forms import ModelForm
from .models import UserInput

# creer une formulaire 

class InputForm(ModelForm):
  class Meta:
      model = UserInput 
      fields = ('titre', 'resume', 'contenu', 'auteur', 'date_de_creation', 'date_mise_a_jour', 'miniature')
      
      
      labels = {
        'titre':'',
        'resume':'',
        'contenu':'',
        'contenu':'',
        'auteur':'',
        'date_de_creation':'',
        'date_mise_a_jour':'',
        'miniature':'Ajouter une photo ',
      }
      
      widgets = {
        'titre':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Non de votre Vehicule'}),
        'resume':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Petite Resumer'}),
        # 'Miniature':forms.ImageField(attrs={'class':'form-control'}),
        'contenu':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Description complet'}),
        'auteur':forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':"L'auteur du vehicule"}),
        'date_de_creation':forms.DateInput(attrs={'class':'form-control form-control-lg', 'placeholder':'La date de creation'}),
        'date_mise_a_jour':forms.DateInput(attrs={'class':'form-control form-control-lg', 'placeholder':'La date de mise en vente'}),
      }