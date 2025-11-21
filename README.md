#  SAMI – Système Autonome de Mobilité Intelligente

### **Projet pluridisciplinaire : Mathématiques – Automatique – Informatique**

##  **Description du projet**

Le projet **SAMI** a pour objectif d’étudier, modéliser et programmer le déplacement autonome d’un robot LEGO EV3 capable d’atteindre plusieurs points sur une carte en parcourant **la distance minimale possible**.
Le robot doit ainsi résoudre une version du **problème du voyageur de commerce (TSP)** tout en appliquant un contrôleur automatique réaliste et en se localisant via un système de caméras.

Le travail est structuré en trois pôles complémentaires :

* **Mathématiques** : calcul du chemin optimal (TSP heuristique)
* **Automatique** : modélisation dynamique + lois de commande
* **Informatique** : interface graphique, communication et pilotage du robot

---

##  **Fonctionnalités principales**

### ###  **1. Partie Mathématiques — Optimisation du Trajet**

Implémentation de plusieurs heuristiques pour approximer une solution du TSP :

* **Plus Proche Voisin (Nearest Neighbor)** – O(n²)
* **Méthode d’Insertion** – O(n³)
* **Amélioration locale 2-opt**, permettant de supprimer les croisements et réduire la distance totale.

La sortie de cette partie est **une liste ordonnée de points** représentant le chemin final à suivre.

---

###  **2. Partie Automatique — Modélisation & Commande du Robot**

La partie automatique assure la dynamique réelle du robot :

* Modèle cinématique différentiel du robot EV3
* Identification expérimentale des constantes du robot :

  * Gain statique **Ks = 0.06**
  * Constante de temps **τ = 0.4**
* Conception d’un **correcteur** basé sur les erreurs de position et d’orientation
* Simulation complète sous **MATLAB/Simulink**
* Choix final des gains :

  * **K1 = 0.09**
  * **K2 = 6.5**

Cette partie fournit une fonction permettant de calculer **Vg** et **Vd**, les vitesses moteurs nécessaires pour atteindre chaque point.

---

###  **3. Partie Informatique — Pilotage & Interface Graphique**

Cette partie lie les mathématiques et l’automatique :

* Récupération de la position (X, Y, θ) via le système **Cortex** (multicast)
* Classe `Coords` permettant :

  * `getCoords()` → récupération temps réel
  * `Excel()` → enregistrement périodique des positions
* Interface graphique Tkinter :

  * Affichage de la carte et du trajet optimal
  * Visualisation de la position en temps réel du robot
  * Connexion au robot via IP
  * Boutons de commande : **Avancer**, **Arrêter**
* Fonction `Move_robot()` intégrant :

  * Le correcteur automatique
  * L’avancement point par point jusqu’à la destination

---

##  **Technologies utilisées**

### **Matériel**

* Robot **LEGO Mindstorms EV3**
* Réseau de caméras **Cortex**
* Poste utilisateur

### **Logiciels / Frameworks**

* **Python 3**
* **Tkinter** (interface utilisateur)
* **MATLAB / Simulink** (modélisation automatique)
* **Regressi** (régression expérimentale)
* **Excel / CSV** pour la collecte de coordonnées





