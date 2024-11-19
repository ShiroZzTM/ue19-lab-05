import requests
import random

def get_random_competitions():
    # URL de l'API Football-Data
    url = "http://api.football-data.org/v4/competitions/"

    # Faire une requête GET pour obtenir les compétitions sans clé API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Vérifiez si la réponse contient des compétitions
        if 'competitions' in data:
            competitions = data['competitions']

            # Sélectionner 5 compétitions aléatoires
            random_competitions = random.sample(competitions, 5)
            print("-" * 36)
            print("Liste des compétitions disponibles :")
            print("-" * 36)
            # Afficher les 5 compétitions choisies
            for i, comp in enumerate(random_competitions, 1):
                print(f"Compétition {i}:")
                print(f"Nom: {comp['name']}")
                print(f"Code: {comp['code']}")
                print(f"Zone: {comp['area']['name']}")
                print("-" * 36)

        else:
            print("Aucune compétition trouvée dans la réponse de l'API.")

    else:
        print(f"Erreur lors de la récupération des données: {response.status_code}")

# Appel de la fonction
if __name__ == "__main__":
    get_random_competitions()

    # Test Action
