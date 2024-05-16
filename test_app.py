import requests

def test_status_endpoint():
    url = "https://votre-api.com/status"  # Remplacez par l'URL réelle du point de terminaison
    response = requests.get(url)

    if response.status_code == 200:
        print("Le point de terminaison est actif !")
    else:
        print(f"Erreur : Code d'état {response.status_code}")

if __name__ == "__main__":
    test_status_endpoint()
