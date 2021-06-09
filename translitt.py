#Importation du module pour la capitalisation
import re

"""Définition du dictionnaire de translittération
Il est important de définir les caractères diacrités avant les simples
Puisqu'il n'y a pas de caractères précomposés pour les diacritiques du svane"""
Geor2Latn = {
"ა̄̈": "ǟ",
 "ა̄": "ā",
 "ა̈": "ä",
 "ა": "a",
 "ბ": "b",
 "გ": "g",
 "დ": "d",
 "ე̄": "ē",
 "ე": "e",
 "ვ": "v",
 "ჱ": "ė",
 "ზ": "z",
 "თ": "t",
 "ი̄": "ī",
 "ი": "i",
 "კ": "k’",
 "ლ": "l",
 "მ": "m",
 "ნ": "n",
 "ო̄̈": "ȫ",
 "ო̈": "ö",
 "ო̄": "ō",
 "ო": "o",
 "პ": "p’",
 "ჟ": "ž",
 "რ": "r",
 "ს": "s",
 "ტ": "t’",
 "უ̄̈": "ǖ",
 "უ̄": "ū",
 "უ̈": "ü",
 "უ̂": "w",
 "უ": "u",
 "ფ": "p",
 "ქ": "k",
 "ღ": "ɣ",
 "ყ": "q’",
 "შ": "š",
 "ჩ": "č",
 "ც": "c",
 "ძ": "ʒ",
 "წ": "c’",
 "ჭ": "č’",
 "ხ": "x",
 "ჯ": "ǯ",
 "ჰ": "h",
 "ჴ": "q",
 "ჸ": "ʔ",
 "ჷ̄": "ə̄",
 "ჷ": "ə",
 "ჲ": "j",
 "ჶ": "f",
}
#définition du dictionnaire inverse de translittération
Latn2Geor = {v: k for k, v in Geor2Latn.items()}

#Ouverture du fichier en mode lecture
fin = open(input("Source : "),"r")
#Copie du contenu du fichier dans une nouvelle variable "data"
data = fin.read()
#fermeture du fichier
fin.close()

#Remplacement des caractères définis dans le dictionnaire
for key in Geor2Latn.keys():
    data = data.replace(key, Geor2Latn[key])
    
#Création d'une fonction de capitalisation
def capital(match):
    return match.group(1).upper()
#Capitalisation des lettres après ponctuation
data = re.sub(r'([!\?\.]\s.)', capital, data)

#ouverture du fichier en mode écriture
fout = open(input("Cible : "), "w")
#écriture et fermeture
fout.write(data)
fout.close()
