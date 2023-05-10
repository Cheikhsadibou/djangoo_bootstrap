Tache à faire:
Page Webs:

I) Page d'accueil

 A) Présentez mon site et afficher les 4 derniers articles du blog
  1) De s'inscrire

    - une id(type = clee primaire) - Int(auto)
    - un nom (type = varchar, longeur= 150) CharField(max)
    - un prenom (type = varchar, longeur = 150) CharField(max)
    - mots de passe (type = varchar, longuer = 150) CharField(max)
    - un email (type = varchar, longeur = 150) EmailField(max)
    - l'utilisateur qui la creer (type = Cle etranger) ForegntKey()

  <!-- 2) de connecter avec un compte existant

    - un email (type = varchar, longeur = 150) EmailField(max)
    - mots de passe (type = varchar, longuer = 150) CharField(max) -->
    
  3) Page Blog
  4) Page détail article
  5) Création d'article
  6) Modifier un article
  7) Page Contact
  8) Page a Propos
  9) d'afficher les 4 derniers articles du blog  
 
 

II) Page Blog

  A) Affichez la liste des articles, maximum 10 avec la pagination

    1) Titre: Le titre de l'article
    2) Résumé: Une petite description de l'article
    3) Miniature: L'image de l'article

III) Page détail article

  A) Affichez les détails d'un article

      Article

      - Titre: Le titre de l'article
      - Résumé: Une petite description de l'article
      - Miniature: L'image de l'article
      - Contenu: Les détails de l'article
      - Auteur: Celui ou celle qui a écrit l'article
      - Date de création(type = Date TimeStamp) DateTime(auto)
      - Date de dernière mise à jour (type = Date TimeStamp) DateTime(auto)

IV) Création d'article

 A) Ajoutez un formulaire qui permet d'ajouter un article

  Article

  - Ajouter-Titre: Le titre de l'article
  - Ajouter-Résumé: Une petite description de l'article
  - Ajouter-Miniature: L'image de l'article
  - Ajouter-Contenu: Les détails de l'article
  - Ajouter-Auteur: Celui ou celle qui a écrit l'article
  - Date de création (type = Date TimeStamp) DateTime(auto)
  - Date de dernière mise à jour (type = Date TimeStamp) DateTime(auto)

V) Modifier un article

 A) Ajoutez un formulaire qui permet de modifier un article

    Article

  - Modifier-Titre: Le titre de l'article
  - Modifier-Résumé: Une petite description de l'article
  - Modifier-Miniature: L'image de l'article
  - Modifier-Contenu: Les détails de l'article
  - Modifier-Auteur: Celui ou celle qui a écrit l'article


VI) Page Contact

 A) Vous mettez vos infos ainsi que votre géolocalisation
  - Profil personnelle
  - Coordonner 
  - Etudes et realisation
  - géolocalisation

VII) Page a Propos
- Vous vous présentez sur cette page
    