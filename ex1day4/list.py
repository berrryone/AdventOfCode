def count_xmas(grid):
    word = "XMAS"
    word_len = len(word)
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    # Funkcja sprawdzająca słowo w różnych kierunkach
    def check_word(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols):
                return False
            if grid[nx][ny] != word[i]:
                return False
        return True

    # Sprawdzanie poziomo, pionowo i na ukos w czterech kierunkach
    for i in range(rows):
        for j in range(cols):
            # Sprawdzanie w prawo
            if j + word_len <= cols and check_word(i, j, 0, 1):
                count += 1
            # Sprawdzanie w lewo
            if j - word_len + 1 >= 0 and check_word(i, j, 0, -1):
                count += 1
            # Sprawdzanie w dół
            if i + word_len <= rows and check_word(i, j, 1, 0):
                count += 1
            # Sprawdzanie w górę
            if i - word_len + 1 >= 0 and check_word(i, j, -1, 0):
                count += 1
            # Sprawdzanie na ukos w dół w prawo
            if i + word_len <= rows and j + word_len <= cols and check_word(i, j, 1, 1):
                count += 1
            # Sprawdzanie na ukos w górę w prawo
            if i - word_len + 1 >= 0 and j + word_len <= cols and check_word(i, j, -1, 1):
                count += 1
            # Sprawdzanie na ukos w dół w lewo
            if i + word_len <= rows and j - word_len + 1 >= 0 and check_word(i, j, 1, -1):
                count += 1
            # Sprawdzanie na ukos w górę w lewo
            if i - word_len + 1 >= 0 and j - word_len + 1 >= 0 and check_word(i, j, -1, -1):
                count += 1

    return count

# Odczytanie zawartości pliku text.txt
with open('text.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]

# Liczenie wystąpień
result = count_xmas(grid)
print(f"Znaleziono {result} wystąpień słowa 'XMAS'.")
