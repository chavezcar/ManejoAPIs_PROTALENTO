import pandas as pd
import requests

def ej_1_cargar_iso_codes() -> list[str]:
    # Cargar el archivo currency_codes.csv
    df = pd.read_csv("currency_codes.csv")
    
    # Extraer los ISO codes de la columna AlphabeticCode
    iso_codes = df["AlphabeticCode"].tolist()
    
    return iso_codes

def ej_2_cargar_tipos_de_cambio(monedas: list[str]) -> None:
    base_url = "https://api.api-ninjas.com/v1/exchangerate?pair="
    api_key = "zniefnNGQ52Zt6vFLkmKog==tbOHCrP5KhsYDhlC"
    usd_to_iso_rates = {}

    for iso_code in monedas:
        print(iso_code)
        response = requests.get(f"{base_url}USD_{iso_code}", headers={'X-Api-Key': api_key})
        if response.status_code == 200:
            data = response.json()
            print(data)
            usd_to_iso_rates[iso_code] = data["exchange_rate"]
        else:
            print(f"No se encontró correspondencia para {iso_code}")

    # Crear un DataFrame con las tasas de cambio
    df = pd.DataFrame(usd_to_iso_rates.items(), columns=["iso_code", "tipo_de_cambio"])
    df.to_csv("monedas.csv", index=False)

def ej_3_convertir(moneda_origen: str, monto: float, moneda_destino: str) -> float:
    # Carga los tipos de cambio desde el archivo monedas.csv
    df = pd.read_csv("monedas.csv")
    
    # Obtiene el tipo de cambio de la moneda de origen a USD
    tipo_cambio_origen = df.loc[df['iso_code'] == moneda_origen, 'tipo_de_cambio'].values[0]
    
    # Obtiene el tipo de cambio de USD a la moneda de destino
    tipo_cambio_destino = df.loc[df['iso_code'] == moneda_destino, 'tipo_de_cambio'].values[0]
    
    # Convierte el monto de la moneda de origen a USD y luego a la moneda de destino
    monto_usd = monto / tipo_cambio_origen
    monto_destino = monto_usd * tipo_cambio_destino
    
    return monto_destino
