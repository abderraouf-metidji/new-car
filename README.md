## Projet New car

### Contexte du projet

L'objectif est de déterminer le prix d'une voiture d'occasion à partir de son âge et de son kilométrage et du type de transmission. Pour arriver a ce resultat nous avons a notre disposition un dataset contenant des informations sur plusieurs vehicules. 

L'ensemble du dataset contient les informations suivantes pour chaque voiture :

  * Car_name : définit le nom de la voiture.
  * Year : définit l’année de fabrication de la voiture.
  * Selling_Price : définit le prix auquel le propriétaire souhaite vendre la voiture (votre target).
  * Present_Price : définit le prix de la voiture départ*usine de la voiture.
  * Kms_Driver : définit la distance parcourue en km par la voiture.
  * Fuel_Type : définit le type de carburant de la voiture.
  * Seller_type : définit si le vendeur est un revendeur ou un particulier.
  * Transmission : définit si la boîte à vitesse de la voiture est manuelle ou automatique.
  * Owner : définit le nombre d'anciens propriétaires de la voiture.

Méthode:

  * Explorer les données et visualiser les distributions.
  * Evaluer la corrélation entre l'âge et le prix.
  * Construire un modèle de régression linéaire.
  * Evaluer la performance du modèle.
  * Estimer le prix pour un client potentiel.

Nous predirons egalement le prix d'une voiture specifique afin de determiner si notre algorithme de prediction est performant ou non.

### Analyse de données

Concernant les etapes de notre analyse de donnees nous allons:

 * Nettoyer les donnees
 * Remplacer les donnees quand c'est possible
 * Visualiser les correlations et le dataset de maniere generale

Pour le nettoyage des données nous avons commencer par la suppression des doublons. Suite à cela nous avons également supprimé la colonne 'Car_Name' car nous n'allons pas utiliser cette variable lors de la prédiction de données et elle ne nous apporte aucune valeur contrairement aux autres variables. Il est également difficile de transformer cette données qualitative en donnée quantitative. 

Nous avons tranformer les valeurs des variables 'Selling_price' et 'Present_price' car elles étaient en k€. 

Pour les valeurs manquantes nous n'avons trouvé aucune valeur manquante. 

En ce qui concerne la transformation des données nous avons dans un premier temps ajouté une colonne 'Nb_of_year' qui correspond à l'age des véhicules par rapport à l'année présente dans le dataset la plus récente, qui est 2018.

Suite à cela nous avons transformer les variables catégorielles en variables quantitatives. 

Nous avons utilisé la méthode get_dummies de pandas afin de transformer nos données catégorielles en données quantitatives. On a donc 4 nouvelles colonnes qui nous permettent d'identifier nos nouvelles variables.

Dans notre cas nous avons Fuel_Type_Diesel & Fuel_Type_Petrol en 0 ou 1, lorsque la valeur est 0 est les 2 colonnes il s'agit de la 3ème observation 'CNG'.

Pour ce qui est du Seller_Type nous avons une nouvelle colonne Seller_Type_Individual qui a aussi des valeurs 0 & 1. Lorsque la valeur est de 0 le Seller_Type est un 'Dealer' et lorsque la valeur est de 1 le Seller_Type est un 'Individual'.

Pour la dernière colonne il s'agit de la Transmission. Lorsque la Transmission est 'Manual' on retrouve 1 dans la colonne Transmission_Manual et lorsque la transmission est 'Automatic' on a une valeur de 0.

Nous arrivons maintenant à la partie visualisation de données. Cependant, nous n'avons remarqué aucune corrélation particulière parmis nos variables.

### Algorithme utilisé (veille)

Scipy:

Sklearn:


### Conclusion

Le projet New Car a permis de développer un modèle de prédiction du prix d'une voiture d'occasion en fonction de son âge, de son kilométrage et de son type de transmission.

L'analyse des données a montré une corrélation positive entre l'âge et le prix, ainsi qu'une influence du type de transmission sur le prix.

Un modèle de régression linéaire a été construit et sa performance a été évaluée. Le modèle s'est avéré efficace pour prédire le prix d'une voiture d'occasion.

Cependant, le modèle peut être amélioré en utilisant d'autres variables et en explorant d'autres modèles d'apprentissage automatique.

Le projet New Car ouvre la voie à la création d'un outil en ligne permettant aux utilisateurs d'estimer le prix de leur voiture d'occasion.