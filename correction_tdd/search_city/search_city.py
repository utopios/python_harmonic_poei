CITIES = [
"Paris", "Budapest", "Skopje", "Rotterdam", "Valence", "Vancouver", "Amsterdam", "Vienne", "Sydney", "New York", "Londres", "Bangkok", "Hong Kong", "Dubaï", "Rome", "Istanbul"
]

def city_search(query):
    if not isinstance(query,str):
        raise TypeError()
    if query == "*":
        return CITIES
    if len(query) < 2:
        return []

    list_towns = []
    for town in CITIES:
        if query.lower() in town.lower():
            list_towns.append(town)

    return list_towns
