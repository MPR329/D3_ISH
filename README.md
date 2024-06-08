# Une visualisation des commentaires sur les posts Instagram d'Arsenal F.C durant la saison 2021-2022

I. Auteur
------
Matthieu Perring

II. Description du projet
------
Ce projet créé 3 visualisations à partir des données issues du scraping des commentaires sur les posts Instagram que le compte d'Arsenal F.C a posté après chaque match de sa saison 2021-2022.

Les informations récoltées pour chaque post étaient les suivantes : 
* "USERNAME": "joelbeya1", // Le nom d'utilisateur de la personne qui a commenté
* "ID":"0", // Juste un id unique généré par le bot pour chaque commentaire du post
* "DATE": "2022-02-19", // La date du commentaire
* "TIME": "17:16:48", // L'heure du commentaire
* "LIKES": "936 ", // Le nombre de likes sur ce commentaire
* "REPLIES": "4", // Le nombre de replies (malheureusement je n'ai pas fait l'effort d'également scraper les replies à chaque commentaire)
* "COMMENTS": "Hale End Academy baby!!!", // Le commentaire
* "TAGS": 0, // Le nombre de tags (p.ex @arsenalFC)
* "HASHTAGS": 0, // Le nombre de tags (p.ex #ARSENAL)
* "ACCOUNT_STATUS": true, // Le statut du compte (vérifié ou non)

III. Informations sur le code
------
Le projet est structuré de la manière suivante : 
* Un dossier _audios_ qui contient tous les fichier .mp3 utilisés
* Un dossier _models_ qui contient tous les modèles 3d .glb utilisés
* Un fichier html.html_ utilisant a-frame
* Ce fichier _readme.md_ qui explique le projet

Il y a parfois un souci avec les fichiers audios. Ceux-ci ne se jouent pas tout le temps automatiquement. L'audioContext se suspend parfois et les empêche de se lancer tout seul. Il faut parfois charger plusieurs fois la page pour que les audios fonctionnent. J'ai tenté de résoudre ce problème mais sans succès...

IV. Contenu du projet 
------
#### ${\color{lightgreen}COULOIR}$
L'expérience auditive se passe à l'intérieur d'un long couloir noir fixe
#### ${\color{lightgreen}PRESENTOIRS}$
Chaque objet est exposé en suspension au-dessus d'un cylindre. Le modèle 3d de l'objet "flotte" avec une animation de rotation et un déplacement sur l'axe des y.
#### ${\color{lightgreen}LUMIERES}$
Les présentoirs et les objets sont éclairés par plusieurs spots de lumières. Une de en haut, une de en-bas et deux de côté.
#### ${\color{lightgreen}CIEL}$ 
Pour ajouter un peu de couleur, le ciel est bleu
#### ${\color{lightgreen}ELEMENTS \space INTERACTIFS/AUDIO}$
Chaque objet a un fichier audio qui joue et que l'utilisateur entend une fois qu'il s'en approche assez.

V. GIF de l'expérience 
------
![projet_aframe_gif_readme](https://github.com/MPR329/ISH_PROJET_AFRAME/assets/62051312/3827980a-62e4-4b90-b268-8045a3f1991e)

VI. Installation et lancement de l'expérience
------
Aucune installation particulière n'est nécessaire pour explorer la scène VR.
L'appel au framework A-Frame se fait en ligne avec la ligne de code `<script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>`.

VII. Assets
------
Les assets sont donc dans le dossier _audios_ et dans le dossier _models_

VIII. Sources
------
Les fichier .mp3 utilisés sont des enregistrements qui m'appartiennent à l'exception du bruit de boîte en plastique qui s'ouvre qui vient de youtube studio (Opening Plastic Storage Container à https://studio.youtube.com/channel/UC-qt0AvcROj2u2Qe7eQ1xXw/music)
Les fichiers .glb utilisés sont des modèles 3d que j'ai créé avec l'application Luma et un Iphone 13
Les modèles 3D proviennet du site https://sketchfab.com/. Les crédits de chaque modèle sont mentionnés au-dessus du téléchargement du modèle dans le fichier `index.html`.

IV. Contexte de développement
------
Ce projet a été développé dans le cadre du cours de _Réalité virtuelle et augmentée_ dispensé par Isaac Pante (SLI, Lettres, UNIL).
