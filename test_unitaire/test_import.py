import os
import csv
import sys
from importation_objects.abstract_importation_liste import AbstractImportationListe


FICHIER = "listeformatCSV.csv" #le nom du fichier de test
dossier = sys.path[1] #récupération chemin du projet
dossier = dossier.replace(os.sep, '/') #transformation




liste_res = []
with open(f'{dossier}/test_unitaire/{FICHIER}','r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')
    for row in reader:
        liste_res.append(row[0])
print(liste_res)
