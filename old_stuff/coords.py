def generate_grid(southwest, northeast, rows, cols):
    lat_step = (northeast[0] - southwest[0]) / rows
    lon_step = (northeast[1] - southwest[1]) / cols

    grid = []
    for i in range(rows):
        for j in range(cols):
            sw_lat = southwest[0] + i * lat_step
            sw_lon = southwest[1] + j * lon_step
            ne_lat = sw_lat + lat_step
            ne_lon = sw_lon + lon_step
            grid.append((sw_lat, sw_lon, ne_lat, ne_lon))
    
    return grid

# Slovenia coordinates
southwest = (45.42, 13.38)
northeast = (46.88, 16.61)

# Generate grid for Slovenia
grid_cells = generate_grid(southwest, northeast, 5, 5)

# Example grid cell output
for cell in grid_cells:
    print(f"SW: {cell[0]}, {cell[1]} | NE: {cell[2]}, {cell[3]}")
