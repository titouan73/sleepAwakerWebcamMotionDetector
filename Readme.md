[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/titouan73/webcamMotionDetector/blob/master/Readme-EN.md)

# Detection de mouvement avec une webcam et gestion de veille
Ce script Python permet de détecter les mouvements devant une webcam et de sortir l'ordinateur de veille lorsqu'un mouvement est détecté.

## Prérequis
Pour utiliser ce script, vous avez besoin de :

- Python 3.x (testé avec la version 3.8)
- OpenCV (`pip install opencv-python`)
- PyAutoGUI  (`pip install pyautogui`)


## Optionnel

- xscreensaver (pour mettre l'ordinateur en veille lorsqu'aucun mouvement n'est détecté)
- Un gestionnaire de paquets tel que apt ou yum (pour installer xscreensaver)


## Utilisation

1. Connectez une webcam à votre ordinateur.
2. Ouvrez un terminal et naviguez jusqu'au répertoire contenant le script.
3. Exécutez le script en tapant python nom_du_script.py.
4. La fenêtre de la webcam s'ouvre et affiche en temps réel ce qui se passe devant la caméra.
5. Lorsqu'un mouvement est détecté, un rectangle vert apparaît autour de l'objet en mouvement et l'ordinateur sort de veille.
6. Appuyez sur "q" pour quitter le script.


## Remarques

- Vous pouvez ajuster le seuil de détection de mouvement en modifiant la valeur de threshold dans la fonction cv2.threshold().
- Vous pouvez ajuster la taille minimale des objets considérés comme des mouvements en modifiant la valeur de min_area dans la condition if cv2.contourArea(c) < min_area:.

## Lancer le script automatiquement au démarage

Pour lancer le script automatiquement à chaque démarrage de votre ordinateur avec PM2, suivez ces étapes :

1. Assurez-vous d'avoir installé PM2 en exécutant `npm install pm2 -g` (nécessite Node.js et npm)
2. Ouvrez un terminal et naviguez jusqu'au répertoire contenant le script
3. Exécutez la commande `pm2 start nom_du_script.py` (remplacez "nom_du_script.py" par le nom de votre fichier Python)
4. Exécutez la commande `pm2 save` pour enregistrer l'état de PM2
5. Exécutez la commande `pm2 startup` pour créer un script de démarrage de PM2 qui sera exécuté à chaque démarrage de votre ordinateur
6. Suivez les instructions affichées dans le terminal pour finaliser la configuration de PM2 au démarrage

Une fois ces étapes terminées, votre script devrait être exécuté automatiquement à chaque démarrage de votre ordinateur. Vous pouvez vérifier si le script est en cours d'exécution en utilisant la commande pm2 list.

> Note : si vous souhaitez arrêter le script exécuté par PM2, utilisez la commande `pm2 stop nom_du_script.py`. Si vous souhaitez le supprimer de la liste des processus gérés par PM2, utilisez la commande `pm2 delete nom_du_script.py`.

## Licence

Ce script est sous licence MIT. N'hésitez pas à l'utiliser et à l'adapter selon vos besoins.