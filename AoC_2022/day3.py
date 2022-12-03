# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_day3.ipynb.

# %% auto 0
__all__ = ['shared', 'BASE_LOWER', 'BASE_UPPER', 'get_compartments', 'get_shared', 'priority', 'intersect', 'get_badge',
           'get_groups']

# %% ../nbs/03_day3.ipynb 4
example = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

packs_ex = example.split()

# %% ../nbs/03_day3.ipynb 8
def get_compartments(packs: list[str]) -> list[tuple]:
    """Split each pack down the middle."""
    lengths = [len(x) for x in packs]
    return [(pack[:lengths[i]//2], pack[lengths[i]//2:]) 
                for i, pack in enumerate(packs)]

get_compartments(packs_ex)

# %% ../nbs/03_day3.ipynb 10
def get_shared(compartments: list[tuple]) -> list[str]:
    """Find the shared item in each pack: same in both compartments."""
    return [set(left).intersection(right).pop()
            for left, right in compartments]

shared = get_shared(get_compartments(packs_ex))
shared

# %% ../nbs/03_day3.ipynb 12
BASE_LOWER = ord("a") - 1
BASE_UPPER = ord("A") - 27
def priority(char: str) -> int:
    """Return priority 1..52 of item in pack."""
    if char.lower() == char:
        return ord(char) - BASE_LOWER
    return ord(char) - BASE_UPPER


# %% ../nbs/03_day3.ipynb 23
def intersect(left, right) -> str:
    """Find set intersection btw two args."""
    return set(left).intersection(right)

def get_badge(group: list[str]) -> str:
    """Find common item """
    return reduce(intersect, group).pop()

# %% ../nbs/03_day3.ipynb 26
def get_groups(packs: list[str]) -> list[list]:
    """Split packlist into groups of 3"""
    return [[packs[i], packs[i+1], packs[i+2]]
            for i in range(0, len(packs), 3)]