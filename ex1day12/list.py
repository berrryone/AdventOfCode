# Funkcja do znalezienia sąsiednich komórek
def adjacent(coord):
    return [coord + 1, coord - 1, coord + 1j, coord - 1j]

# Funkcja do wypełnienia regionu (DFS)
def fill_region(grid, visited, start, plant_type):
    region = []
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            region.append(current)
            x, y = int(current.real), int(current.imag)
            for adj in adjacent(current):
                adj_x, adj_y = int(adj.real), int(adj.imag)
                if 0 <= adj_x < len(grid[0]) and 0 <= adj_y < len(grid) and grid[adj_y][adj_x] == plant_type and adj not in visited:
                    stack.append(adj)
    return region

# Funkcja do obliczenia obwodu regionu
def calculate_perimeter(region, grid):
    perimeter = 0
    for coord in region:
        x, y = int(coord.real), int(coord.imag)
        # Sprawdzanie 4 sąsiednich stron
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid) or grid[ny][nx] != grid[y][x]:
                perimeter += 1
    return perimeter

# Funkcja do obliczenia całkowitego kosztu ogrodzenia
def total_fence_cost(grid):
    visited = set()
    total_cost = 0
    
    # Przejście po siatce, aby znaleźć wszystkie regiony
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x + 1j * y) not in visited:
                plant_type = grid[y][x]
                region = fill_region(grid, visited, x + 1j * y, plant_type)
                area = len(region)
                perimeter = calculate_perimeter(region, grid)
                total_cost += area * perimeter
    
    return total_cost

# Odczyt danych z pliku 'text.txt'
def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

# Odczytanie mapy z pliku i obliczenie całkowitego kosztu
grid = read_grid_from_file('text.txt')

# Obliczenie i wyświetlenie całkowitego kosztu ogrodzenia
print(total_fence_cost(grid))
