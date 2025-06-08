# Classificateur de Température 🌡️

Ce script Python simple permet de classifier une température en trois catégories : **Froid**, **Modéré** ou **Chaud**, selon la valeur saisie par l'utilisateur.

## 🧠 Fonctionnalité

* L'utilisateur entre une température en degrés Celsius.
* Le programme classe automatiquement la température :

  * Moins de 15°C : **Froid**
  * De 15°C à moins de 25°C : **Modéré**
  * 25°C ou plus : **Chaud**

## 📄 Exemple d'utilisation

```bash
$ python3 temperature_classifier.py
Entrez la température en °C : 18
La météo est : Modéré
```

## 🔧 Pré-requis

* Python 3.x installé
* Terminal ou console pour exécuter le script

## 📁 Structure du script

* `classify_temperature(temp)` : Fonction principale de classification
* Entrée utilisateur via `input()`
* Affichage du résultat avec `print()`

## 💡 Améliorations possibles

* Ajouter une gestion des erreurs en cas de saisie invalide
* Permettre la classification de plusieurs températures dans une même session
* Ajouter un mode graphique (GUI) avec Tkinter ou PyQt

