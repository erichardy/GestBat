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


-------------------------------
A propos de cette documentation
-------------------------------

Cette documentation est réalisée en format `rst` avec `sphinx`_.

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



