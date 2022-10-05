"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.drop_duplicates(inplace=(True))	
    df.dropna(inplace=(True))
    df.drop(['Unnamed: 0'], axis=1, inplace=(True))
    
    df['sexo'] = df['sexo'].str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['barrio'] = df['barrio'].str.lower()
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].str.lower()
    df['monto_del_credito'] = df['monto_del_credito'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.lower()

    df['línea_credito'].replace({" ": '_'}, inplace=(True),  regex=True)
    df['línea_credito'].replace({"-": '_'}, inplace=(True),  regex=True)
    df['línea_credito'].replace({"soli_diaria": 'solidaria'}, inplace=(True),  regex=True)
    df['línea_credito'].replace({"_": ' '}, inplace=(True),  regex=True)
    df['línea_credito'] = df['línea_credito'].str.strip()

    df['idea_negocio'].replace({" ": '_'}, inplace=(True),  regex=True)
    df['idea_negocio'].replace({"-": '_'}, inplace=(True),  regex=True)	
    df['idea_negocio'].replace({"_": ' '}, inplace=(True),  regex=True)
    df['idea_negocio'] = df['idea_negocio'].str.strip()

    df['barrio'].replace({" ": '_'}, inplace=(True),  regex=True)
    df['barrio'].replace({"-": '_'}, inplace=(True),  regex=True)	
    df['barrio'].replace({"antonio_nari¿o": 'antonio_nariño'}, inplace=(True),  regex=True)	
    df['barrio'].replace({"bel¿n": 'belen'}, inplace=(True),  regex=True)	
    df['barrio'].replace({"_": ' '}, inplace=(True),  regex=True)
    df['barrio'] = df['barrio'].str.strip()

    for index, element in enumerate (df['monto_del_credito']):
        if element[0] == '$':
            df['monto_del_credito'].iloc[index] = df['monto_del_credito'].iloc[index][2:-3]
    df['monto_del_credito'].replace({",": ''}, inplace=(True),  regex=True)	        
    df['monto_del_credito'] = df['monto_del_credito'].astype(int) 

    for index, element in enumerate (df['fecha_de_beneficio']):
        if (element[1] == '/') or (element[2] == '/'):
            partes = element.split("/")
            nueva_fecha = "/".join(reversed(partes))        
            df['fecha_de_beneficio'].iloc[index] = nueva_fecha
        
    df.dropna(inplace=(True)) 
    df.drop_duplicates(inplace=(True))	

    return df
