#!/usr/bin/env python
# coding: utf-8

# ## Utilisationn de scikit-learn:
# Apprentissage des modèles suivants: Arbre de décision, Réseau de Neurones et SVM
# Évaluation en utilisant le GridSearch

# In[1]:


#importatation de modules commun
import lxml.etree
import lxml
from lxml import etree
from defusedxml.lxml import fromstring
from defuxedxml import lxml as potatoe

xmlString = "<note>\n<to>Tove</to>\n<from>Jani</from>\n<heading>Reminder</heading>\n<body>Don't forget me this weekend!</body>\n</note>"
root = lxml.etree.fromstring(xmlString)
root = fromstring(xmlString)

import numpy as np
import pandas as pd

# pour la énération de seed
np.random.seed(4)

# pur l'afficae de figures
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
from time import *


# In[2]:


#lecture des deux datasets Train_spam et Test_spam pour la détection de spam
#consulter le site de UCI pour avoir de l'information sur le data spambas
#https://archive.ics.uci.edu/ml/datasets/spambase
data_train = pd.read_csv("train_spam.CSV")
data_test = pd.read_csv("test_spam.CSV")


# In[3]:


data_train.info()


# In[4]:


data_train.shape


# In[5]:


data_test.shape


# In[6]:


data_train.head()


# In[95]:


# Séparer des données des variables prédictives (X) 
# de la variable cible (Y)
X_train=data_train.iloc[:,:-1]
y_train=data_train['Class']


# # Entrainement et visualisation

# In[65]:


#Maintenant, nous pouvons entrainer  pour constuire un classeur : clf
#en utilisant le nouveau dataframe modifié.:

#l'option criterion : indique l'utilisation de l'entropie 
#comme heuristique pour le choix de la meilleure variable

from sklearn.tree import DecisionTreeClassifier
clf= DecisionTreeClassifier(criterion="entropy", max_depth=5)
clf.fit(X_train, y_train)


# In[66]:


#affichage de l'arbre
from sklearn.tree import plot_tree
plot_tree(clf, feature_names=list(data_train.columns[:-1]), filled=True)


# In[67]:


#affichage avec une meilleure visibilité
import matplotlib.pyplot as plt
plt.figure(figsize=(50,50))
plot_tree(clf, feature_names=list(data_train.columns),filled=True)
plt.show()


# In[68]:


#Pour avoir une idée sur les variables impliquées
#Nous récupérons le champ "feature_importances_" de la structure de l'arbre
#que nous plaçons dans un dataframe 
#pour pouvoir afficher les contributions des variables associées 
#à leurs noms, et triées de manière décroissante.
#les variables qui apparaissent dans l'arbres sont celles dont l'importance est
#est différent de zéro.

ImportanceVariables={"Variable":data_train.columns[:-1],
                         "Importance":clf.feature_importances_}
print(pd.DataFrame(ImportanceVariables).sort_values(by="Importance",ascending=False))


# ## Validation avec un jeu de test
# 
# Validation du classeur clf avec le jeu de test.
# Il faut s'assurer que le jeu de test est dans la même configuration
# 

# In[69]:


#séparons les donnees de test des variables prédictives de celles 
#de la variable cible

X_test=data_test.iloc[:,:-1]
y_test=data_test['Class']


# In[70]:


#Voici un exemple de résultat de test avec le modele clf obtenu initialement 
# avec les données de test

from sklearn.metrics import accuracy_score
y_pred = clf.predict(X_test)
accuracy_score(y_test, y_pred)

# le résultat est de l'ordre de 100%
#c'est normal car le modele a été entrainé 
#et testé avec les même données !


# In[71]:


#test
y_pred = clf.predict(X_test)
from sklearn.metrics import classification_report
print('Results on the test set:')
print(classification_report(y_test, y_pred))


# # Amélioration :Hyperparamètres de régulation
# 
# Utilisation de la méthode "GridSearchCV" 
# avec la validation croisée pour trouver la meilleure valeur de 
# l'hyerparametre 'max_depth' d'un classeur de type arbre de décision.
# On peut aussi faire le calibrage avec d'autres hyperparametres.
# Voir les options dans scikit-learn de la classe DecisionTreeClassifier

# In[72]:


from sklearn.model_selection import GridSearchCV
params = {'max_depth': list(range(2, 20)), 'min_samples_split': [10, 15, 20]}


grid_search_cv = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1, verbose=1, cv=3)
grid_search_cv.fit(X_train, y_train)


# In[73]:


#le meilleur estimateur (modele) trouvé est:
grid_search_cv.best_estimator_


# Il a fait une sorte d'optimisation du modele clf obtenu auparavant
# au lieu d'avoir une profondeur 5. Il a trouvé une bonne valeur à 9.
# Maintenant, on peut faire évaluer le meilleur modèle trouvé à l'étape précédente par le GridSearcCV en utilisant le jeu de test.

# In[74]:


from sklearn.metrics import accuracy_score

y_pred = grid_search_cv.predict(X_test)
accuracy_score(y_test, y_pred)

#Voici le résultat de la performance qui est de l'ordre:


# In[84]:


#Comparaison avec un MLP
#importation du module mlp

from sklearn.neural_network import MLPClassifier

#utilsation 2 couches cachées. La premiere est composé de 100 neurones et l'autre de 50.
#la fonction d'activation est le relu
#la regle d'apprentissage est la descente du gradient: solver=sgd

#clf = MLPClassifier(hidden_layer_sizes=(100,50), solver='sgd', max_iter=12500, activation='relu', random_state=42)
clf = MLPClassifier(hidden_layer_sizes=(100,50), solver='adam', max_iter=500, activation='relu', random_state=42)
#clf = MLPClassifier(hidden_layer_sizes=(100), solver='lbfgs', max_iter=500, activation='relu', random_state=42)
#mesure du temps courant
tc = clock()
clf.fit(X_train,y_train)
tt = clock()
print("le temps d'entrainement en secondes", tt-tc)


# In[85]:


#Voici un exemple de résultat de test avec le modele clf obtenu initialement 
# testé avec les données de test

from sklearn.metrics import accuracy_score
y_pred = clf.predict(X_test) 
accuracy_score(y_test, y_pred)

# le taux de détection est de l'ordre de :


# In[86]:


#entrainement d'un support vector macine
#importation du module SVC, l'équivalemnt du SVM mais multi-classes
from sklearn.svm import SVC
#l'option kernel -noyau- peut être: fonction lineare, polynomial, fonction radiale -rbd-, sigmoide..

#clf = SVC(kernel='rbf')
#clf = SVC(kernel='linear')
clf = SVC(kernel='poly')
#mesure du temps courant
tc = clock()
clf.fit(X_train,y_train)
tt = clock()
print("le temps d'entrainement en secondes", tt-tc)


# In[87]:


#les vecteurs support de la fonction de décision de la fonction de decision
clf.support_vectors_


# In[88]:


#Voici un exemple de résultat de test avec le modele clf obtenu initialement 
# avec les données de test

from sklearn.metrics import accuracy_score
y_pred = clf.predict(X_test)
accuracy_score(y_test, y_pred)

# le résultat est de l'ordre de 100%
#c'est normal car le modele a été entrainé 
#et testé avec les même données !


# In[80]:


#test
y_pred = clf.predict(X_test)
from sklearn.metrics import classification_report
print('Results on the test set:')
print(classification_report(y_test, y_pred))


# In[ ]:




