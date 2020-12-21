#!/usr/bin/env python3

import pprint
import collections
import itertools
import re
import sys

# Functions

def process_ingredients_list(stream=sys.stdin):
    all_ingredients = collections.defaultdict(int)
    all_allergens   = {}

    for ingredients, allergens in re.findall(r'(.*)\(contains (.*)\)', stream.read()):
        ingredients = set(ingredients.split())
        allergens   = allergens.split(', ')
        
        for ingredient in ingredients:
            all_ingredients[ingredient] += 1

        for allergen in allergens:
            if allergen in all_allergens:
                # WTF: all_allergens[allergen] &= ingredients produces different results???
                all_allergens[allergen] = all_allergens[allergen] & ingredients
            else:
                all_allergens[allergen] = ingredients

    return all_ingredients, all_allergens

def determine_dangerous_ingredients(ingredients, allergens):
    dangerous_ingredients = {}

    while any(len(bad_ingredients) == 1 for bad_ingredients in allergens.values()):
        for allergen, bad_ingredients in allergens.items():
            if len(bad_ingredients) != 1:
                continue

            bad_ingredient = list(bad_ingredients)[0]
            dangerous_ingredients[bad_ingredient] = allergen

            for other_allergen in allergens:
                allergens[other_allergen] = allergens[other_allergen] - bad_ingredients

    return dangerous_ingredients

# Main Execution

def main():
    ingredients, allergens = process_ingredients_list()
    dangerous_ingredients  = determine_dangerous_ingredients(ingredients, allergens)
    canonical_list         = ','.join(sorted(dangerous_ingredients, key=dangerous_ingredients.get))

    print(canonical_list)


if __name__ == '__main__':
    main()
