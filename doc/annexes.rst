.. include:: links.rst

Annexes
=======

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
