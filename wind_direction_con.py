# wind_direction_con.py

def wind_direction(degrees):
    """Converts wind direction in degrees to a cardinal direction."""
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = int((degrees // 22.5) % 8)
    return directions[index]
