from collections import defaultdict

city_list = [
    ('TX', 'Austin'),
    ('TX', 'Houston'),
    ('NY', 'Albany'),
    ('NY', 'Syracuse')
]

cities_by_state = defaultdict(list)

for state, city in city_list:
    cities_by_state[state].append(city)

print(cities_by_state)

food_list = 'spam spam spam spam spam spam spam egg spam'
food_count = defaultdict(int)


