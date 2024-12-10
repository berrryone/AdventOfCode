from collections import Counter

def calculate_similarity_score(left_list, right_list):
    # Liczymy wystąpienia liczb w prawej liście
    right_counter = Counter(right_list)
    
    # Obliczamy wynik podobieństwa
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counter[num]
    
    return similarity_score

# Funkcja do wczytywania danych z pliku i podziału na listy
def read_data_from_file(filename):
    left_list = []
    right_list = []
    
    # Otwieramy plik i wczytujemy dane
    with open(filename, 'r') as file:
        for line in file:
            # Dzielimy każdą linię na dwie liczby
            left_num, right_num = map(int, line.split())
            left_list.append(left_num)
            right_list.append(right_num)
    
    return left_list, right_list

# Wczytujemy dane z pliku
filename = 'text.txt'  # Ścieżka do pliku
left_list, right_list = read_data_from_file(filename)

# Obliczamy wynik podobieństwa
similarity_score = calculate_similarity_score(left_list, right_list)
print(f"Wynik podobieństwa: {similarity_score}")
