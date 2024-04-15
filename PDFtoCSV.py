import csv
import re
import pdfplumber
import pandas as pd
import numpy as np

# Chemin vers le fichier PDF
pdf_path = r'C:\Users\alari\Documents\Cours M1 alarig\Projet tutoré\VERSION BAPTISTE\FICHIER2.pdf'

# Initialisation d'une liste pour stocker le texte
text_data = []

# Ouvrir le fichier PDF avec pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    # Itérer sur chaque page du PDF
    for page in pdf.pages:
        # Extraire le texte de la page
        text = page.extract_text()
        # Ajouter le texte à notre liste
        text_data.append(text)

# Convertir la liste de texte en un DataFrame pandas
df = pd.DataFrame(text_data, columns=['Text'])

# Afficher les premières lignes du DataFrame
print(df.head())

# Optionnel: enregistrer le DataFrame dans un fichier CSV
df.to_csv("texte_pdf_extrait.csv",index=False)

fichier_csv = "texte_pdf_extrait.csv" # REMPLACER LE LIEN PAR LE PDF QUE L'ON VEUT EXTRAIRE

# Lire le fichier CSV et stocker le contenu dans la variable csv_content
with open(fichier_csv, 'r', encoding="utf8") as file:
    csv_content = file.read()

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_number(s):
    return bool(re.match(r'^[0-9]+$', s))

# Prétraitement de la chaîne CSV
filtered_rows = [row for row in csv_content.strip().split('\n') if row.strip()]

# Initialisation des variables
current_entry = {}
is_judge_scores = False
is_program_components = False
player = "No"
num_judges = 0


# Créer un DataFrame vide avec les colonnes spécifiques


for i, row in enumerate(filtered_rows):
    if "Composition" in row :

        num_judges = len(row.split()) - 3
        #if num_judges // 2 == 0 : Ref = True
        break
print("Nombre de juges :",num_judges)
if num_judges == 5 :
    columns = ["Numéro","Elements", "info", "base_value", "GEO / FACTOR", "J1", "J2", "J3", "J4", "J5", "Score_panel", "Player_ID","NomPren","Nation","StartingNb","ScoreTotal","Rank","ScoreElem","ScoreComp","Deduction"]

if num_judges == 6 :
    columns = ["Numéro","Elements", "info", "base_value", "GEO / FACTOR", "J1", "J2", "J3", "J4", "J5","J6", "Score_panel", "Player_ID","NomPren","Nation","StartingNb","ScoreTotal","Rank","ScoreElem","ScoreComp","Deduction"]

if num_judges == 7 :
    columns = ["Numéro","Elements", "info", "base_value", "GEO / FACTOR", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "Score_panel", "Player_ID","NomPren","Nation","StartingNb","ScoreTotal","Rank","ScoreElem","ScoreComp","Deduction"]

if num_judges == 8 :
    columns = ["Numéro","Elements", "info", "base_value", "GEO / FACTOR", "J1", "J2", "J3", "J4", "J5","J6","J7","J8", "Score_panel", "Player_ID","NomPren","Nation","StartingNb","ScoreTotal","Rank","ScoreElem","ScoreComp","Deduction"]

if num_judges == 9 :
    columns = ["Numéro","Elements", "info", "base_value", "GEO / FACTOR", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "Score_panel", "Player_ID","NomPren","Nation","StartingNb","ScoreTotal","Rank","ScoreElem","ScoreComp","Deduction"]

if num_judges == 10 :
    columns = ["Numéro","Elements", "info", "base_value", "GEO / FACTOR", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9","J10", "Score_panel", "Player_ID","NomPren","Nation","StartingNb","ScoreTotal","Rank","ScoreElem","ScoreComp","Deduction"]

if num_judges == 11 :
    columns = ["Numéro","Elements", "info", "base_value", "GEO / FACTOR", "J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9","J10","J11","Score_panel", "Player_ID","NomPren","Nation","StartingNb","ScoreTotal","Rank","ScoreElem","ScoreComp","Deduction"]


df = pd.DataFrame(columns=columns)

# Parcourir les lignes du CSV
for i, row in enumerate(filtered_rows):
    if "Legend:" in row :
        break
    if "Score Score" in row:
        # Extraire le numéro, nom et prénom du joueur
        player_info = filtered_rows[i + 1].split()
        
        for index,value in enumerate(player_info[1:]):
           
            if is_number(value) :
            
                break    
            
        player_id = player_info[0]
        player_nation = player_info[index]
        player_name = ' '.join(player_info[1:index])
        player = f"{player_id} {player_name}"
        player_startingNb = player_info[index+1]
        player_total_Segment_Score = player_info[index+2]
        player_total_Element_Score = player_info[index+3]
        player_total_Component_Score = player_info[index+4]
        player_Deduction = player_info[index+5]
        
    elif "#" in row:
        # Activation du drapeau pour indiquer que nous sommes dans la section des détails des juges
        is_judge_scores = True
        is_program_components = False
    elif "Program Components" in row:
        # Activation du drapeau pour indiquer que nous sommes dans la section des composants du programme
        is_program_components = True
        is_judge_scores = False
    elif "Judges Total Program Component Score (factored)" in row:
        # Désactivation des deux drapeaux à la fin de la section des composants du programme
        is_judge_scores = False
        is_program_components = False
    
        
    if num_judges == 11 :
        if is_judge_scores:
            # Traitement des données des juges  
            if "Base Scores of # Executed Elements GOE J1 J2 J3 J4 J5 J6 J7 J8 J9 J10 J11 Ref."  not in row and "Value" not in row and len(row.split()) > num_judges :
                
                if is_float(row.split()[2]):
                    
                    
                    if len(row.split()) == 17 :
                        new_row_split = row.split()[:3] + row.split()[4:]
                        nb ,elements, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, panel = new_row_split
                        
                    else :    
                        nb ,elements, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        #"info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "J7": j7,
                        "J8": j8,
                        "J9": j9,
                        "J10": j10,
                        "J11": j11,
                        "Score_panel": panel,
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                else :
                  
                    if len(row.split()) == 18 :
                        new_row_split = row.split()[:4] + row.split()[5:]
                        nb ,elements, info, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, panel = new_row_split
                        
                    else :    
                        nb ,elements,info, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        "info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "J7": j7,
                        "J8": j8,
                        "J9": j9,
                        "J10": j10,
                        "J11": j11,
                        "Score_panel": panel,
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                    
            if len(row.split()) == 2 and "Value" not in row :
                total_base , total_panel = row.split()
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                    
                    'base_value' : total_base,
                    'Score_panel': total_panel,
                    'Numéro' : 'Total',
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}    
        elif is_program_components:
            # Traitement des données des composants du programme
            if "Program Components" not in row and "Judges" not in row and "Skating" not in row:
                # Utilisez des indices spécifiques pour extraire les données
                
            
                name, Factor,j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": name,
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "J7": j7,
                "J8": j8,
                "J9": j9,
                "J10": j10,
                "J11": j11,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
            if "Skating" in row :
                name,name2, Factor,j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": f"{name} {name2}",
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "J7": j7,
                "J8": j8,
                "J9": j9,
                "J10": j10,
                "J11": j11,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
        
    if num_judges == 10 :
        if is_judge_scores:
            # Traitement des données des juges  
            if "Base Scores of # Executed Elements GOE J1 J2 J3 J4 J5 J6 J7 J8 J9 Ref."  not in row and "Value" not in row and len(row.split()) > num_judges :
              
                if is_float(row.split()[2]):
                    
                  
                    if len(row.split()) == 16 :
                        new_row_split = row.split()[:3] + row.split()[4:]
                        nb ,elements, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, panel = new_row_split
                        
                    else :    
                        nb ,elements, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9,j10, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        #"info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "J7": j7,
                        "J8": j8,
                        "J9": j9,
                        "J10": j10,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                else :
                  
                    if len(row.split()) == 17 :
                        new_row_split = row.split()[:4] + row.split()[5:]
                        nb ,elements, info, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9,j10, panel = new_row_split
                        
                    else :    
                        nb ,elements,info, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        "info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "J7": j7,
                        "J8": j8,
                        "J9": j9,
                        "J10": j10,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                    
            if len(row.split()) == 2 and "Value" not in row :
                total_base , total_panel = row.split()
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                    
                    'base_value' : total_base,
                    'Score_panel': total_panel,
                    'Numéro' : 'Total',
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
        elif is_program_components:
            # Traitement des données des composants du programme
            if "Program Components" not in row and "Judges" not in row and "Skating" not in row:
                # Utilisez des indices spécifiques pour extraire les données
              
            
                name, Factor,j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": name,
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "J7": j7,
                "J8": j8,
                "J9": j9,
                "J10": j10,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
            if "Skating" in row :
                name,name2, Factor,j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": f"{name} {name2}",
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "J7": j7,
                "J8": j8,
                "J9": j9,
                "J10": j10,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
    
    if num_judges == 9 :
        if is_judge_scores:
            # Traitement des données des juges  
            if "#"  not in row and "Value" not in row and len(row.split()) > num_judges :
              
                if is_float(row.split()[2]):
                    
                  
                    if len(row.split()) == 15 :
                        new_row_split = row.split()[:3] + row.split()[4:]
                        nb ,elements, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9, panel = new_row_split
                        
                    else :    
                        nb ,elements, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        #"info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "J7": j7,
                        "J8": j8,
                        "J9": j9,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                else :
                  
                    if len(row.split()) == 16 :
                        new_row_split = row.split()[:4] + row.split()[5:]
                        nb ,elements, info, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9, panel = new_row_split
                        
                    else :    
                        nb ,elements,info, base_value, geo, j1, j2, j3, j4, j5, j6, j7, j8, j9, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        "info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "J7": j7,
                        "J8": j8,
                        "J9": j9,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                    
            if len(row.split()) == 2 and "Value" not in row :
                total_base , total_panel = row.split()
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                    
                    'base_value' : total_base,
                    'Score_panel': total_panel,
                    'Numéro' : 'Total',
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
        elif is_program_components:
            # Traitement des données des composants du programme
            if "Program Components" not in row and "Judges" not in row and "Skating" not in row:
                # Utilisez des indices spécifiques pour extraire les données
              
            
                name, Factor,j1,j2,j3,j4,j5,j6,j7,j8,j9,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": name,
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "J7": j7,
                "J8": j8,
                "J9": j9,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
            if "Skating" in row :
                name,name2, Factor,j1,j2,j3,j4,j5,j6,j7,j8,j9,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": f"{name} {name2}",
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "J7": j7,
                "J8": j8,
                "J9": j9,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
                
    if num_judges == 8 :
        if is_judge_scores:
            # Traitement des données des juges  
            if "#"  not in row and "Value" not in row and len(row.split()) > num_judges :
            
             
                if is_float(row.split()[2]):
                    
                
                    if len(row.split()) == 14 :
                        new_row_split = row.split()[:3] + row.split()[4:]
                        nb ,elements,  base_value, geo, j1, j2, j3, j4, j5, j6, j7,j8, panel = new_row_split
                        
                    else :    
                        nb ,elements,  base_value, geo, j1, j2, j3, j4, j5, j6, j7,j8 ,panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        #"info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "J7": j7,
                        "J8": j8,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                else :
                   
                    if len(row.split()) == 15 :
                        new_row_split = row.split()[:4] + row.split()[5:]
                        nb ,elements, info, base_value, geo, j1, j2, j3, j4, j5, j6, j7,j8, panel = new_row_split
                        
                    else :    
                        nb ,elements,info, base_value, geo, j1, j2, j3, j4, j5, j6, j7,j8, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        "info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "J7": j7,
                        "J8": j8,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                    
            if len(row.split()) == 2 and "Value" not in row :
                total_base , total_panel = row.split()
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                    
                    'base_value' : total_base,
                    'Score_panel': total_panel,
                    'Numéro' : 'Total',
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
        elif is_program_components:
            # Traitement des données des composants du programme
            if "Program Components" not in row and "Judges" not in row and "Skating" not in row:
                # Utilisez des indices spécifiques pour extraire les données
             
                name, Factor,j1,j2,j3,j4,j5,j6,j7,j8,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": name,
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "J7": j7,
                "J8": j8,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
            if "Skating" in row :
                name,name2, Factor,j1,j2,j3,j4,j5,j6,j7,j8,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": f"{name} {name2}",
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "J7": j7,
                "J8": j8,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
    
    if num_judges == 7 :
        if is_judge_scores:
            # Traitement des données des juges  
            if "#"  not in row and "Value" not in row and len(row.split()) > num_judges :
            
             
                if is_float(row.split()[2]):
                    
                
                    if len(row.split()) == 13 :
                        new_row_split = row.split()[:3] + row.split()[4:]
                        nb ,elements,  base_value, geo, j1, j2, j3, j4, j5, j6, j7, panel = new_row_split
                        
                    else :    
                        nb ,elements,  base_value, geo, j1, j2, j3, j4, j5, j6, j7, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        #"info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "J7": j7,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                else :
                   
                    if len(row.split()) == 14 :
                        new_row_split = row.split()[:4] + row.split()[5:]
                        nb ,elements, info, base_value, geo, j1, j2, j3, j4, j5, j6, j7, panel = new_row_split
                        
                    else :    
                        nb ,elements,info, base_value, geo, j1, j2, j3, j4, j5, j6, j7, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        "info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "J7": j7,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                    
            if len(row.split()) == 2 and "Value" not in row :
                total_base , total_panel = row.split()
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                    
                    'base_value' : total_base,
                    'Score_panel': total_panel,
                    'Numéro' : 'Total',
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
        elif is_program_components:
            # Traitement des données des composants du programme
            if "Program Components" not in row and "Judges" not in row and "Skating" not in row:
                # Utilisez des indices spécifiques pour extraire les données
             
                name, Factor,j1,j2,j3,j4,j5,j6,j7,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": name,
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "J7": j7,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
            if "Skating" in row :
                name,name2, Factor,j1,j2,j3,j4,j5,j6,j7,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": f"{name} {name2}",
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "J7": j7,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
    
    if num_judges == 6 :
        if is_judge_scores:
            # Traitement des données des juges  
            if "Base Scores of # Executed Elements GOE J1 J2 J3 J4 J5 J6 J7 J8 J9 Ref."  not in row and "Value" not in row and len(row.split()) > num_judges :
              
                if is_float(row.split()[2]):
                    
                
                    if len(row.split()) == 12 :
                        new_row_split = row.split()[:3] + row.split()[4:]
                        nb ,elements, base_value, geo, j1, j2, j3, j4, j5,j6, panel = new_row_split
                        
                    else :    
                        nb ,elements, base_value, geo, j1, j2, j3, j4, j5,j6, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        #"info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                else :
                    
                    if len(row.split()) == 13 :
                        new_row_split = row.split()[:4] + row.split()[5:]
                        nb ,elements, info, base_value, geo, j1, j2, j3, j4, j5,j6, panel = new_row_split
                        
                    else :    
                        
                        nb ,elements,info, base_value, geo, j1, j2, j3, j4, j5,j6, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        "info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "J6": j6,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                    
            if len(row.split()) == 2 and "Value" not in row :
                total_base , total_panel = row.split()
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                    
                    'base_value' : total_base,
                    'Score_panel': total_panel,
                    'Numéro' : 'Total',
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
                 
            
        elif is_program_components:
            # Traitement des données des composants du programme
            if "Program Components" not in row and "Judges" not in row and "Skating" not in row:
                # Utilisez des indices spécifiques pour extraire les données
            
            
                name, Factor,j1,j2,j3,j4,j5,j6,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": name,
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
            if "Skating" in row :
                name,name2, Factor,j1,j2,j3,j4,j5,j6,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": f"{name} {name2}",
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "J6": j6,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
    
    if num_judges == 5 :
        if is_judge_scores:
            # Traitement des données des juges  
            if "Base Scores of # Executed Elements GOE J1 J2 J3 J4 J5 J6 J7 J8 J9 Ref."  not in row and "Value" not in row and len(row.split()) > num_judges :
              
                if is_float(row.split()[2]):
                    
                
                    if len(row.split()) == 11 :
                        new_row_split = row.split()[:3] + row.split()[4:]
                        nb ,elements, base_value, geo, j1, j2, j3, j4, j5, panel = new_row_split
                        
                    else :    
                        nb ,elements, base_value, geo, j1, j2, j3, j4, j5, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        #"info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                else :
                    
                    if len(row.split()) == 12 :
                        new_row_split = row.split()[:4] + row.split()[5:]
                        nb ,elements, info, base_value, geo, j1, j2, j3, j4, j5, panel = new_row_split
                        
                    else :    
                        nb ,elements,info, base_value, geo, j1, j2, j3, j4, j5, panel = row.split() #1,2,1,1,1,1,1,2,1,1,1,1,1,2,3 
                    
                    current_entry["Player_ID"] = player
                    current_entry["Player_ID"] = player
                    current_entry["NomPren"] = player_name
                    current_entry["Nation"] = player_nation
                    current_entry["StartingNb"] = player_startingNb
                    current_entry["ScoreTotal"] = player_total_Segment_Score
                    current_entry["Rank"] = player_id
                    current_entry["ScoreElem"] = player_total_Element_Score
                    current_entry["ScoreComp"] = player_total_Component_Score
                    current_entry["Deduction"] = player_Deduction
                    current_entry.update({
                        "Numéro": nb,
                        "Elements": elements,
                        "info": info,
                        "base_value": base_value,
                        "GEO / FACTOR": geo,
                        "J1": j1,
                        "J2": j2,
                        "J3": j3,
                        "J4": j4,
                        "J5": j5,
                        "Score_panel": panel
                        
                    })
                    df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                    current_entry = {}
                    
            if len(row.split()) == 2 and "Value" not in row :
                total_base , total_panel = row.split()
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                    
                    'base_value' : total_base,
                    'Score_panel': total_panel,
                    'Numéro' : 'Total',
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
                 
            
        elif is_program_components:
            # Traitement des données des composants du programme
            if "Program Components" not in row and "Judges" not in row and "Skating" not in row:
                # Utilisez des indices spécifiques pour extraire les données
            
            
                name, Factor,j1,j2,j3,j4,j5,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": name,
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
            if "Skating" in row :
                name,name2, Factor,j1,j2,j3,j4,j5,total, = row.split()
                
                current_entry["Player_ID"] = player
                current_entry["Player_ID"] = player
                current_entry["NomPren"] = player_name
                current_entry["Nation"] = player_nation
                current_entry["StartingNb"] = player_startingNb
                current_entry["ScoreTotal"] = player_total_Segment_Score
                current_entry["Rank"] = player_id
                current_entry["ScoreElem"] = player_total_Element_Score
                current_entry["ScoreComp"] = player_total_Component_Score
                current_entry["Deduction"] = player_Deduction
                current_entry.update({
                
                "Elements": f"{name} {name2}",
                
                "GEO / FACTOR": Factor,
                "J1": j1,
                "J2": j2,
                "J3": j3,
                "J4": j4,
                "J5": j5,
                "Score_panel": total,
                
                })
                df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
                current_entry = {}
                
            

    if current_entry and not is_judge_scores and not is_program_components:
        # Ajouter l'entrée actuelle au DataFrame et réinitialiser l'entrée actuelle
        df = pd.concat([df, pd.DataFrame([current_entry])], ignore_index=True)
        current_entry = {}

# Afficher le DataFrame final
# print(df)

is_program_components = False
is_judge_scores = False
listepanel=[]
listecalcul = []
listecalculNoR = []
listecalculNoRNoT = []
for i, row in enumerate(filtered_rows):
    if "Components" in row :
        is_program_components = True
    
    if is_program_components:
        if "Program Components" not in row and "Judges" not in row and "Skating" not in row:
            for j in range(i,i+3):
                #print(filtered_rows[j].split(),len(filtered_rows[j].split()))
                RowS = filtered_rows[j].split()
                listepanel.append(RowS[-1])
                Val = []
                if "Skating" in RowS :
                    for i in RowS[3:-1] :
                    
                        Val.append(i)
                     #   print(Val)
                    m = min(Val)
                    #print("Min  ",m)
                    Val.remove(m)
                    M = max(Val)
                    #print("Max =",M)
                    Val.remove(M)
                    #print(Val)
                    test = 0
                    for i in Val :
                        test = test + float(i)
                    test = test / (num_judges-2)
                    listecalcul.append(round(test,2))
                    Val = []
                    for i in RowS[3:-2] :
                    
                        Val.append(i)
                     #   print(Val)
                    m = min(Val)
                    #print("Min  ",m)
                    Val.remove(m)
                    M = max(Val)
                    #print("Max =",M)
                    Val.remove(M)
                    #print(Val)
                    test = 0
                    for i in Val :
                        test = test + float(i)
                    test = test / (num_judges-3)
                    listecalculNoR.append(round(test,2))
                    Val = []
                    for i in RowS[3:-2] :
                    
                        Val.append(i)
                     #   print(Val)
                    #print(Val)
                    test = 0
                    for i in Val :
                        test = test + float(i)
                    test = test / (num_judges-1)
                    listecalculNoRNoT.append(round(test,2))
                    Val = []
                else :
                    for i in RowS[2:-1] :
                    
                        Val.append(i)
                        #print(Val)
                    m = min(Val)
                    #print("Min  ",m)
                    Val.remove(m)
                    M = max(Val)
                    #print("Max =",M)
                    Val.remove(M)
                    #print(Val)
                    test = 0
                    for i in Val :
                        test = test + float(i)
                    test = test / (num_judges-2)
                    listecalcul.append(round(test,2))
                    Val = []
                    for i in RowS[2:-2] :
                    
                        Val.append(i)
                     #   print(Val,"VAL SANS R ?")
                    m = min(Val)
                    #print("Min  ",m)
                    Val.remove(m)
                    M = max(Val)
                    #print("Max =",M)
                    Val.remove(M)
                    #print(Val)
                    test = 0
                    for i in Val :
                        test = test + float(i)
                    test = test / (num_judges-3)
                    listecalculNoR.append(round(test,2))
                    Val = []
                    for i in RowS[2:-2] :
                    
                        Val.append(i)
                        #print(Val,"VAL SANS R ?")
                   
                    test = 0
                    for i in Val :
                        test = test + float(i)
                    test = test / (num_judges-1)
                    listecalculNoRNoT.append(round(test,2))
                    Val = []
            break
for i, value in enumerate(listepanel):
    listepanel[i] = float(value)
    
#print(listepanel,"Panel")
#print(listecalcul,"Base")
#print(listecalculNoR,"Pas de Arbitre")
#print(listecalculNoRNoT,"Pas trim pas Arb")

REF = False
if listecalculNoRNoT == listepanel or listepanel == listecalculNoR :
   # print("YESSSSSSSSSSSSSS")
    REF = True
    

if REF :
    #print( df.columns[num_judges + 4])
    df.rename(columns ={df.columns[num_judges + 4] : 'JRef'},inplace = True)


print(df)    
      # Exporter le DataFrame en fichier CSV
csv_filename = "FICHIER_ANALYSE.csv"
df.to_csv(csv_filename, index=False)

    # Afficher le nom du fichier CSV généré
print(f"Dataset exporté en tant que fichier .cvs sous le nom : {csv_filename}")