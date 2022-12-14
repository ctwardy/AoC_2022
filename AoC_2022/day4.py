# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/day4.ipynb.

# %% auto 0
__all__ = ['get_assignments', 'right_contains_left', 'left_contains_right', 'contains', 'disjoint', 'overlap']

# %% ../nbs/day4.ipynb 7
#| code-fold: true
def get_assignments(data: list[str] # List of assignment pairs "2-4,6-8"
                    ) -> list[list[int]]: # List of [min,max,min,max]
    """Split each assignment by commas and dashes."""
    _ = (row.replace("-",",").split(",") for row in data)
    return [[int(x) for x in row] for row in _]

# %% ../nbs/day4.ipynb 9
#| code-fold: true
def right_contains_left(row: list[int] # [min,max,min,max]
                       )-> bool: # Right pair contains left
    return (row[2] <= row[0]) and (row[3] >= row[1])

def left_contains_right(row: list[int] # [min,max,min,max]
                       )-> bool: # Left pair contains right
    return (row[0] <= row[2]) and (row[1] >= row[3])

def contains(row: list[int] # [min,max,min,max]
            )-> bool: # One pair contains the other
    return right_contains_left(row) or left_contains_right(row)



# %% ../nbs/day4.ipynb 18
#| code-fold: true
def disjoint(row: list[int] # [min,max,min,max]
            )-> bool:       # The ranges are disjoint
    # min1 > max2 or max1 < min2
    return (row[0] > row[3]) or (row[1] < row[2])

def overlap(row: list[int] # [min,max,min,max]
            )-> bool:       # The ranges overlap
    return not disjoint(row)

