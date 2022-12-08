# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_day3.ipynb.

# %% auto 0
__all__ = ['example', 'packs_ex', 'shared', 'BASE_LOWER', 'BASE_UPPER', 'get_compartments', 'get_shared', 'priority', 'intersect',
           'get_badge', 'get_groups']

# %% ../nbs/03_day3.ipynb 5
example = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

packs_ex = example.split()

# %% ../nbs/03_day3.ipynb 9
#| code-fold: true
def get_compartments(packs: list[str] # List of pack contents like ['vJrwpWtw', ...]
                    ) -> list[tuple]: # Split each pack like ('vJrw', 'pWtw')
    """Split each pack down the middle."""
    lengths = [len(x) for x in packs]
    return [(pack[:lengths[i]//2], pack[lengths[i]//2:]) 
                for i, pack in enumerate(packs)]

get_compartments(packs_ex)

# %% ../nbs/03_day3.ipynb 11
#| code-fold: true
def get_shared(compartments: list[tuple] # ('vJrw','pWtw')
              ) -> list[str]: # Single char like 'w' here.
    """Find the shared item in each pack: same in both compartments."""
    return [set(left).intersection(right).pop()
            for left, right in compartments]

shared = get_shared(get_compartments(packs_ex))
shared

# %% ../nbs/03_day3.ipynb 13
#| code-fold: true
BASE_LOWER = ord("a") - 1    # 1..26
BASE_UPPER = ord("A") - 27   # 27..52

def priority(char: str # Single char like 'w'
            ) -> int: # Priority 1..52
    """Return priority 1..52 of item in pack."""
    if char.lower() == char:
        return ord(char) - BASE_LOWER
    return ord(char) - BASE_UPPER


# %% ../nbs/03_day3.ipynb 23
#| code-fold: true
from typing import Collection
from functools import reduce

def intersect(left: Collection, # Items in first group
              right: Collection # Items in second group
             ) -> str: # Items common to both 
    """Find set intersection btw two args."""
    return set(left).intersection(right)

def get_badge(group: list[str] # List of item names
             ) -> str: # The single item common to all
    """Find common item. Assumes there is precisely 1."""
    return reduce(intersect, group).pop()

# %% ../nbs/03_day3.ipynb 26
#| code-fold: true
def get_groups(packs: list[str] # List of all packs
              ) -> list[list]:  # Divided into lists of 3
    """Split packlist into groups of 3"""
    return [[packs[i], packs[i+1], packs[i+2]]
            for i in range(0, len(packs), 3)]
