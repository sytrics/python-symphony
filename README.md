# python-symphony

## Introduction 

### Projet initial : 

Le but initial était de compiler un algorithme simple en python, d'y extraire sa structure algorithmique, puis de composer un fichier de description musicale de type MIDI en fonction de sa structure. 

### Projet réalisé : 

Le projet peut à l'heure actuel parser et compiler un fichier python de structure simple, et le recopier dans un autre fichier à l'aide d'un pretty-printer utilisant un pattern visiteur. 

le visiteur permettant la création d'un fichier midi marche mais est en WIP. 

## Usage : 

Executer la commande `python3 main.py -h` affiche l'aide suivante : 

```bash
usage: main.py [-h] [--compiler COMPILER] [--verbose VERBOSE] input output

Le script permet de compiler un programme écrit en python (plus ou moins, voir doc) en utilisant le pattern Visiteur

positional arguments:
  input                the name of the file to be compiled
  output               the name of the file where we will print using Pretty-printer

optional arguments:
  -h, --help           show this help message and exit
  --compiler COMPILER  choose the compiler PP: prettyprinter / MIDI: MIDI-Compiler
  --verbose VERBOSE    BOOL : if verbose set to 1, displays every visit method for debug purposes

made by @sytrics for ENSTA Bretagne
```

Exemple de commande : 

`python3 main.py test.py output.py --compiler PP`

Commande pour compiler le fichier test.py et recopier le contenu dans output (pretty-printer)

`python3 main.py test.py output.py --verbose 1 `

Cette commande fait la même chose mais affiche tout les passages dans les noeuds de l'AST (le visiteur par défaut est le pretty-printer)

```
Verbosity set to True
visitRoot root
visitStatement
visit Node :a
visit Node :=
visitExpression
visitTerm term
visitFactorfactor
visit Node :1
visitStatement
visit Node :b
visit Node :=
visitExpression
...
```

`python3 main.py test.py out.mid --compiler MIDI `

Cette commande permet la génération d'un fichier MIDI rudimentaire. La tonalité des notes et le volume dépendent des entiers renseignés dans le programme. 

Pour lire le fichier créé, il existe des lecteurs sur linux comme `timidity` 

```bash
sudo apt install timidity
python3 main.py test.py out.mid --compiler MIDI
timidity out.mid
```



## Syntaxe accepté 

Le fichier `test.py` est représentatif de la syntaxe interpreté par le compilateur : 

```python
a = 1
b = 2
a = a + 1
var = a + b
if a == b : 
    a = 1
elif a > b : 
    b = 1
else :
    a = 0
while a!= b : 
    a = a + 1 
a = 2
```

Tout ce qui ne figure pas dans le test est considéré comme non implémenté, en particulier : 

* certains mots clés : in range() , is, return, print
* les flottants (problème au niveau des regex)
* la POO 

