# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/day6.ipynb.

# %% auto 0
__all__ = ['f', 'g', 'h', 'get_answer', 'baz_the_foo']

# %% ../nbs/day6.ipynb 10
#| code-fold: true
def f():
    pass

def g():
    pass



# %% ../nbs/day6.ipynb 11
#| code-fold: true
def f(x: int,   # An x
               y: int,   # A y
              )-> str:   # An xy
    """Find the ...."""
    return "f"

def g(x: int) -> None:
    """Find the ...."""
    pass

# %% ../nbs/day6.ipynb 14
#| code-fold: true
# Probably more defs here.

# %% ../nbs/day6.ipynb 17
#| code-fold: true
# Like before

# %% ../nbs/day6.ipynb 20
#| code-fold: true
def h() -> str:
    return "What, another stub?"


# %% ../nbs/day6.ipynb 31
#| code-fold: true
def get_answer(x: int,   # An x
               y: int,   # A y
              )-> str:   # An xy
    """Find the ...."""
    return "CMZ"

# %% ../nbs/day6.ipynb 42
#| code-fold: true
def baz_the_foo(
    n:   int|str,  # Move this many
    old: list,     # From this stack
    new: list,     # To this stack
    )-> None:      # MODIFIES the stacks!
    """Move `n` things from `from_col` to `to_col` AS A GROUP."""
    for x in reversed([old.pop() for i in range(int(n))]):
        new.append(x)