import requests

def monitorear_sismos_el_salvador(url_geojson):
    # Hacer la solicitud GET al GeoJSON
    response = requests.get(url_geojson)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta a JSON
        geojson_data = response.json()
        
        # Filtrar los sismos en El Salvador
        sismos_el_salvador = [feature for feature in geojson_data['features'] if feature['properties']['place'].startswith('El Salvador')]
        
        # Imprimir la información de los sismos
        for sismo in sismos_el_salvador:
            magnitud = sismo['properties']['mag']
            lugar = sismo['properties']['place']
            fecha = sismo['properties']['time']
            print(f"Magnitud: {magnitud}, Lugar: {lugar}, Fecha: {fecha}")
    else:
        print("Error al obtener los datos.")

if __name__ == "__main__":
    url_geojson = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
    monitorear_sismos_el_salvador(url_geojson)
