.. include:: links.rst

=======
Annexes
=======

--------------------------
Améliorations potentielles
--------------------------

#. un affichage plus descriptif lors du déroulement de la recharge. L'affichage actuel ne fourni aucune
   information
   réellement lisible ou utile. Il pourrait y avoir une indication du temps écoulé, de la puissance
   consommée, etc...
#. un compte rendu de la charge : temps complet de la charge, courant tiré en temps réel, tension aux
   bornes du chargeur, d'où puissance consommée, etc...
#. mesure de la tension aux bornes du chargeur
#. mise en mémoire des données de la dernière recharge (et pourquoi pas des précédentes)
#. nouvelle tare pour l'utilisation possible d'un autre chargeur


---------------------------
Les chargeurs USB et autres
---------------------------

Il n'est pas rare de voir, dans les maisons, un ou plusieurs chargeurs de téléphonne qui sont laissés
dans la prise de courant alors que la charge du téléphone, ou autre appareil, est terminée.
Il faut bien comprendre que le fait d'avoir retiré l'appareil à recharger n'empêche pas
que le chargeur qui est resté branché consomme toujours du courant... et pour s'en convaincre,
on peut facilement constater qu'il chauffe toujours un peu.

On a vu, dans ce document, que le chargeur de la batterie de mon VAE consomme 22mA s'il est resté
branché alors que la charge de la batterie est terminée, de même que si la batterie est déconnectée
du chargeur.

Les quelques autres mesures de courant que j'ai pu faire avec des chargeurs, même de petite taille, ont
montré une consommation au minimum de 1.5mA, mais cela pouvait aller jusqu'à plus de 15mA

Faisons un calcul rapide avec la mesure la plus faible : **1.5mA**

On peut facilement supposer que, par famille (ou ménage, au sens INSEE), il y aurait en moyenne 1
chargeur en permanence laissé sur le secteur sans appareil à recharger sur lui. L'INSEE nous dit qu'il
y a près de 31 millions de ménages en France. donc :

#. 0.0015 A * 240 V = 0.36 Watts
#. 0.36Watts * 31000000 = 11160000 Watts, ou 11 Mega Watts !

En résumé, on peut facilement admettre qu'en France, **à chaque instant, 11 Mega Watts sont gaspillés !!**
soit environ 10% de la production instantanée d'un réacteur nucléaire.

Ces 11 Megawatts instantanés correspondent à un gaspillage annuel de plus de 97 GWh,
l'équivalent de la consommation annuelle d'une ville d'environ 20.000 habitants !


.. note::
    Le calcul que je fais ici est discutable, dans un sens ou dans l'autre car il n'est pas
    facile d'établir le nombre de chargeurs qui sont restés brachés inutilement au secteur
    dans les maisons des particuliers... mais il faudrait aussi évaluer les chargeurs restés
    branchés sur les lieux de travail, les appareils restés en veille (TV, enceintes BlueTooth, etc...).
    L'objet de ce calcul est juste pour donner une idée.

-------------------------------
A propos de cette documentation
-------------------------------

Cette documentation est réalisée en format `RST`_ avec `sphinx`_.

Dans le dossier de la réalisation de ce module `GestBat`, un dossier `doc` est créé. La procédure de
création de la documentation est initialisée avec la commande `sphinx-quickstart`.

:code:`sphinx-quickstart`

D'autre part, dans ce dossier ``doc``, on lance la commande (dans un terminal) :

:code:`sphinx-autobuild . ./_build/html/`

qui, en premier lieu, produit (entre autres) la sortie suivante :

::

    The HTML pages are in _build/html.
    [I 260608 23:20:45 server:335] Serving on http://127.0.0.1:8000

Il suffit donc, avec le navigateur, d'ouvrir l'URL ``http://127.0.0.1:8000`` et à chaque enregistrement
d'un fichier `rst`, la page est mise à jour dans le navigateur. **Très pratique !!**

Enfin, il est possible de construire `à la main` la documentation en allant, toujours dans un terminal,
dans le dossier `doc`, et taper la commande :

:code:`make html`

par exemple pour générer le code HTML.

Pour produire un PDF :

:code:`make latexpdf`

Le PDF se trouve à ``doc/_build/latex/gestbat.pdf``

.. note::
    une erreur en lançant `make latexpdf`

    :code:`! LaTeX Error: File `tgtermes.sty' not found.``

    L'erreur corrigée avec :

    :code:`apt install tex-gyre fonts-texgyre texlive-fonts-extra`



