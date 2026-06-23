import requests
import json

usuario = "Pablo07as"
headers = {
    "User-Agent": "andressalgadopablo@gmail.com"
}

url_archivos = f"https://api.chess.com/pub/player/{usuario}/games/archives"
respuesta_archivos = requests.get(url_archivos, headers=headers)

urls_meses = respuesta_archivos.json().get("archives", [])
print(f"¡Encontrado! Has jugado en {len(urls_meses)} meses distintos.")

todas_las_partidas = [] 

for url in urls_meses:
    respuesta = requests.get(url, headers=headers)
    
    if respuesta.status_code == 200:
        partidas_mes = respuesta.json().get("games", [])
        
        for partida in partidas_mes:
            # Comprobamos que sea una partida rapid
            es_rapid = partida.get("time_class") == "rapid"
            es_ajedrez_normal = partida.get("rules") == "chess"
            
            if es_rapid and es_ajedrez_normal:
                todas_las_partidas.append(partida)
        
    else:
        print(f"Error al descargar {url}. Status code: {respuesta.status_code}")
        

with open("mis_partidas_rapid.json", "w", encoding="utf-8") as f:
    json.dump(todas_las_partidas, f, indent=4)