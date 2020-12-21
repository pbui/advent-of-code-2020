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

def determine_safe_ingredients(ingredients, allergens):
    return [
        ingredient for ingredient in ingredients if all(ingredient not in bad_ingredients for allergen, bad_ingredients in allergens.items())
    ]

# Main Execution

def main():
    ingredients, allergens = process_ingredients_list()
    safe_ingredients       = determine_safe_ingredients(ingredients, allergens)
    safe_ingredients_count = sum(ingredients[ingredient] for ingredient in safe_ingredients)

    print(safe_ingredients_count)

if __name__ == '__main__':
    main()
