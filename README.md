# feistel-cipher-and-RSA-Crypotsystem
Voici un guide détaillé sur l'exécution de mon programme en console:

1. Assurez-vous que vous avez Python 3 installé sur votre ordinateur.
2. Clonez le dépôt GitHub contenant les deux fichiers Python sur votre ordinateur.
3. Ouvrez une fenêtre de terminal et accédez au répertoire dans lequel vous avez cloné le dépôt.
4. Tapez la commande suivante pour exécuter le fichier main.py:
python main.py

5. Le programme affichera un message de bienvenue et vous demandera de choisir l'algorithme de chiffrement que vous souhaitez exécuter (Feistel ou RSA).
Si vous choisissez l'algorithme de chiffrement Feistel, le programme vous demandera d'entrer la clé K et le bloc N de 8 bits que vous souhaitez chiffrer. Vous pouvez choisir de configurer l'algorithme avec des paramètres personnalisés ou d'utiliser les paramètres par défaut. Si vous choisissez de configurer l'algorithme, le programme vous demandera d'entrer la permutation H pour la génération de clé, la permutation π pour le chiffrement et le déchiffrement, l'ordre de décalage à gauche et l'ordre de décalage à droite. Si vous choisissez d'utiliser les paramètres par défaut, le programme exécutera l'algorithme avec les valeurs par défaut.
6. Si vous choisissez l'algorithme de chiffrement RSA, le programme vous demandera d'entrer deux nombres premiers différents (p et q). Le programme générera ensuite les clés publiques et privées à partir de ces nombres premiers. Le programme vous demandera également d'entrer le bloc de chiffrement que vous souhaitez utiliser (256, 512 ou 1024).
7. Le programme affichera le message original, le message chiffré et le message déchiffré pour l'algorithme de chiffrement que vous avez choisi.
8. Vous pouvez exécuter à nouveau le programme en tapant la commande python main.py dans le terminal. 
