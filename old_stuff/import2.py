import requests
import json
import time


# Function to generate grid coordinates
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

# Function to make Strava API call for segments
def get_segments_for_area(sw_lat, sw_lon, ne_lat, ne_lon):
    url = "https://www.strava.com/api/v3/segments/explore"
    
    # Define parameters for the API request
    params = {
        "bounds": f"{sw_lat},{sw_lon},{ne_lat},{ne_lon}",
        'activity_type': 'riding'
    }
    headers = {
    'accept': 'application/json',
    'authorization': "", # Add your access token here
    }

    try:
        # Make the API request
        response = requests.get(url, headers=headers, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()  # Return the segments data in JSON format
        else:
            print(f"Error: {response.status_code} for bounds {sw_lat}, {sw_lon}, {ne_lat}, {ne_lon}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed for bounds {sw_lat}, {sw_lon}, {ne_lat}, {ne_lon}: {e}")
        return None

# Function to save segments data to a file
def save_segments_to_file(data, filename="segments_data.json"):
    with open(filename, 'a') as f:
        json.dump(data, f)
        f.write("\n")  # To separate each entry with a newline

# Function to loop over grid cells and collect data
def fetch_and_save_segments(southwest, northeast, rows, cols):
    grid_cells = generate_grid(southwest, northeast, rows, cols)
    
    # Loop over all grid cells and fetch segments
    for i, (sw_lat, sw_lon, ne_lat, ne_lon) in enumerate(grid_cells):
        print(f"Fetching segments for grid cell {i+1}/{len(grid_cells)}: SW({sw_lat}, {sw_lon}) - NE({ne_lat}, {ne_lon})")
        
        # Fetch segments for this grid cell
        segments_data = get_segments_for_area(sw_lat, sw_lon, ne_lat, ne_lon)
        
        if segments_data:
            # Save the fetched data to a file
            save_segments_to_file(segments_data)
        
        # To avoid hitting the API rate limits, add a delay
        time.sleep(10)

# Define the southwest and northeast coordinates for Slovenia
southwest = (45.42, 13.38)
northeast = (46.88, 16.61)

# Fetch and save segments for the entire region, divided into 5x5 grid cells
fetch_and_save_segments(southwest, northeast, 10, 10)
