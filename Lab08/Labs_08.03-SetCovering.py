import json

def main():
    check = []
    find = set(json.loads(input()))
    city = dict()
    for _ in range(int(input())):
        input_set = json.loads(input())
        city[input_set['Name']] = set(input_set['Cities'])

    while find:
        best_city = None
        covered_cities = set()
        for c, cities in city.items():
            covered = find & cities
            if len(covered) > len(covered_cities):
                best_city = c
                covered_cities = covered
        if not best_city:
            break
        check.append(best_city)
        find -= covered_cities

    print(sorted(check))
main()
