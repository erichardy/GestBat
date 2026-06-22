
.. include:: links.rst


Documentation technique
=======================

.. note::
    Des différences peuvent apparaître entre le schémas et la réalité. Idem pour
    les N° des pins du RPI-Pico. De plus, toutes les fonctionnalités n'ont pas
    été implémentées.

------------------
Le montage général
------------------

.. image:: SchemasComplet.png

---------------------------------
Le Coeur du dispositif : RPI-Pico
---------------------------------

Bien que l'ensemble du dispositif contienne des éléments d'électricité et d'électonique, il est
piloté par un micro-contrôleur : le `Raspberry Pi Pico`_

Le choix de ce microcontrolleur s'est fait essentiellement sur la base de ces éléments :

* je n'avais pas besoin de connections WIFI ou BlueTooth
* il a tout ce dont j'ai besoin
* il est aisé de programmer en `MicroPython`_


------------------
Les fonctionalités
------------------

.. note::
    Tout au long de la description de l'utilisation de ce boîtier, il ne sera pas fait
    état des divers clignotements des LEDs et des Bips du buzzer. Ces deux types d'indicateurs
    n'ont pas de fonction particulière si ce n'est que `d'amuser la galerie !`... mais
    aussi, éventuellement, pour montrer l'utilisation des :code:`Timers`


La mise sous tension
--------------------

Un problème que que nous rencontrons en France est l'absence de norme forte et contraignante techniquement
concernant la configuration des prises de courant. On peut indifférement avoir la phase sur l'une des
broches d'une prise (évidemment à l'exception de la terre), et le neutre sur l'autre.

Or, pour un système branché au secteur, si l'interrupteur est positionné côté neutre, le dispositif est
en permanence sous tension côté phase. Certains interrupteurs opère l'ouverture du circuit à la fois
à la phase et le neutre, mais ce n'est pas le cas systématiquement.

C'est pour cette raison que, dans le boitier *GestBat*, il y a deux relais au niveau de la connection au
secteur, un relai pour la phase et l'autre pour le neutre, sachant qu'il n'y en a aucun de pré-déterminé.

La mise sous tension est donc réalisée d'abord par l'appui sur les 2 boutons qui contournent les
deux relais SSR et permettent le passage de la phase et du neutre. Le RPI-Pico peut alors être alimenté
et mettre à l'état haut les signaux qui gèrent les relais SSR.

Fichier :code:`gestbatMain.py`, :code:`fonction startUP()`


Le délai avant le début de la charge
------------------------------------

Compte tenu que l'utilisation principale est avec la batterie de mon VAE et comme indiqué ci-dessus,
le délai configuré par défaut est de 30mn.

Celui-ci est réglable avec le bouton rotatif à droite, en plus ou en moins (toujours en minutes),
et la validation se fait par un appui (vertical) qui effectue un 'clic'.

Le compte à rebours commence alors.

Au niveau programmation, la gestion de ce délai se fait dans le fichier :code:`gestBatRoptary.py`
où l'on voit qu'une :code:`IRQ` est utilisée pour le bouton rotatif.


Le début de la charge
---------------------

La charge commence donc une fois le délai expiré et à l'activation du relai SSR : :code:`chargerRelay.value(1)`

La durée de la charge ne se fait pas en fonction du temps, mais en fonction de la mesure du courant
consommé par le chargeur. Cette mesure se fait par un `transformateur de courant` récupéré, le signal est
amplifié et redressé par un circuit avec 2 AOP `LM741`.

Le signal est envoyé sur le GPIO26 du `RPI-Pico`_ qui est un ADC.

Une moyenne des 10 dernières valeurs est faite (fonction :code:`averageValues()`) et quand le résultat
devient inférieur ou égal à **600**, la charge se termine.

La valeur de **600** n'est pas arbitraire, elle est la valeur mesurée par l'**ADC** qui correspond
à ce qui a été mesuré avec un ampèremètre au
moment où le chargeur détecte que la batterie est chargée et qu'il stoppe la charge.

A ce moment-là, la fonction :code:`shutdown()` est appelée, les relais principaux sont alors mis
à **off**, et TOUT est coupé !

-----------------------
Quelques autres détails
-----------------------

L'alimentation
--------------


Le bouton resset
----------------


Utilisation pour un autre chargeur que celui du VAE
---------------------------------------------------



