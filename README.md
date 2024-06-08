# VISUALIZATION OF ARSENAL F.C'S MATCH DAY INSTAGRAM POSTS COMMENTS FOR THE 2021-22 SEASON

I. Auteur
------
Matthieu Perring

II. Description du projet
------
Ce projet propose 3 visualisations pour les **136058** commentaires Instagram laissés sous les posts qu'Arsenal F.C a fait après chaque match de la saison 2021-2022 de la Premier League. 

III. Informations sur le code
------
Le code utilise la librairie javascript D3. La librairoe est accédée via la ligne de code ` <script src="https://d3js.org/d3.v7.min.js"></script>`. Le code a été en partie généré par chatgpt sur des prompts précis de ma part puis retravaillé pour le rendre opérationnel puis modifié si besoin pour ajouter des informations à la visualisation. Vous trouverez les échanges avec chatGPT dans le fichier `echanges_chat_gpt.pdf` avec ceux-ci classés par visualisation.

III. Dataset
------
Les données utilisées provienne d'un projet précédent réalisé dans le cadre du cours de _Traitement informatique des corpus textuels II_ dispensé par Aris Xanthos (SLI, Lettres, UNIL). 
Vous trouverez le repo du projet au lien suivant : [Instagram_Comment_Scraping_Bot](https://github.com/MPR329/Instagram_Comment_Scraping_Bot). 

Arsenal F.C fait un post Instagram après chaque match pour annoncer le score et donner diverses informations à ce sujet. J'ai scrapé les commentaires sous tous ce type de posts fait durant la saison 2021-2022 de Premier League. Quelques posts n'avaient pas été scrapé mais sinon quasiment tous les commentaires des autres posts avaient été scrapés. Les données suivantes ont été scrapé pour les **136058** commentaires : 

* **"USERNAME":**                           Le nom d'utilisateur de la personne qui a commenté
* **"ID":**                                 Juste un id unique généré par le bot pour chaque commentaire du post
* **"DATE":**                               La date du commentaire
* **"TIME":**                               L'heure du commentaire
* **"LIKES":**                              Le nombre de likes sur ce commentaire
* **"REPLIES":**                            Le nombre de replies (malheureusement je n'ai pas fait l'effort d'également scraper les replies à chaque commentaire)
* **"COMMENTS":**                           Le commentaire
* **"TAGS":**                               Le nombre de tags (p.ex @arsenalFC)
* **"HASHTAGS":**                           Le nombre de tags (p.ex #ARSENAL)
* **"ACCOUNT_STATUS":**                     Le statut du compte (vérifié ou non)

Afin de faciliter le travail lors de ce projet j'ai fusionné les fichiers _.json_ des commentaires que j'avais pour chaque post scrapé et j'ai ajouté à chaque commentaire l'ID du post duquel il avait été scrapé. (dans le fichier `combined_data.json`)

J'ai aussi utilisé un fichier _.csv_, que j'avais également fait dans le cadre de ce même cours, qui recense différentes informations pour chaque match joué par Arsenal durant la saison (score, nom des buteurs, lien du post instagram, nombre de commentaires, etc). (fichier csv convertit en fichier json dans `matches_info.json`)

IV. Contenu du projet 
------
Le projet comporte 3 visualisations : 

##### ${\color{lightgreen}[GRAPHE \space 1] \space :}$ `BUBBLE_CHART_top_words_during_season.html`
* Cette visualisation met en évidence les 5000 commentaires les plus likés de tous les posts instagram. Plus la bulle est grande, plus le commentaire a été liké un grand nombre de fois. Les commentaires issus d'un même post ont la même couleur. Lorsqu'une bulle est survolée par la souris un tooltip apparaît et montre quelques informations sur le commentaire concerné : nom d'utilisateur, nombre de likes, commentaire, ID du post instagram. 

* On voit vite qu'un commentaire fait par le club lui-même est celui qui a le plus de likes. On voit aussi que, parmi les centaines de milleurs de commentaires, relativement peu ont plus de 10 likes.

##### ${\color{lightgreen}[GRAPHE \space 2] \space :}$ `WORD_CLOUD_top_100_words_per_posts_interactive.html`
* Ce fichier html permet de voir une visualisation des 100 mots les plus fréquents pour tous les posts durant la saison. En addition à la visualisation un tableau est affiché avec diverses information concernant le match.
* Il est assez aisé de voir que si le résultat du match est négatif les mots sont plus négatifs. La performance des joueurs affecte également la fréquence d'apparition de leur nom. Une performance particulièrement bonne ou mauvaise augmente cette fréquence.

##### ${\color{lightgreen}[GRAPHE \space 3] \space :}$ `BARPLOT_top_commentors.html`
* Ce simple barplot permet de voir quel utilisateur a commenté le plus de fois sur chaque commentaires. Lorsque la souris survole une bar, un tooltip affiche le nom de l'utilisateur ainsi que le nombre de commentaire sur le post concerné.
* Un examen rapide du fichier json permet de voir que les commentaires des ces utilisateurs sont différents mais que chacun répète souvent la même série de commentaires. Cela fait penser que ces utilisateurs sont des bots. En regardant ensuite le profil de ses utilisateurs on constate qu'il apparaissent comme des utilisateur "normaux".
* Il serait intéressant de creuser plus cette piste et faire des visualisation spécifiquement sur les données de commentaires de ces utilisateurs. Notamment comment leur temps de latence pour poster un commentaire, après que le post soit mis en ligne par le club, comparé
 aux autres utilisateurs. Cette visualisation, malgré sa simplicité, est celle qui, je trouve, a permis de mettre en évidence l'information la plus intéressante.

V. GIFs de l'expérience 
------


VIII. Sources
------
Les fichier .mp3 utilisés sont des enregistrements qui m'appartiennent à l'exception du bruit de boîte en plastique qui s'ouvre qui vient de youtube studio (Opening Plastic Storage Container à https://studio.youtube.com/channel/UC-qt0AvcROj2u2Qe7eQ1xXw/music)
Les fichiers .glb utilisés sont des modèles 3d que j'ai créé avec l'application Luma et un Iphone 13
Les modèles 3D proviennet du site https://sketchfab.com/. Les crédits de chaque modèle sont mentionnés au-dessus du téléchargement du modèle dans le fichier `index.html`.

IV. Contexte de développement
------
Ce projet a été développé dans le cadre du cours de _Réalité virtuelle et augmentée_ dispensé par Isaac Pante (SLI, Lettres, UNIL).
