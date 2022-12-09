# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_template.ipynb.

# %% auto 0
__all__ = ['f', 'g', 'h', 'get_answer', 'baz_the_foo']

# %% ../nbs/00_template.ipynb 10
#| code-fold: true
def f():
    pass

def g():
    pass



# %% ../nbs/00_template.ipynb 11
#| code-fold: true
def f(x: int,   # An x
               y: int,   # A y
              )-> str:   # An xy
    """Find the ...."""
    return "f"

def g(x: int) -> None:
    """Find the ...."""
    pass

# %% ../nbs/00_template.ipynb 14
#| code-fold: true
# Probably more defs here.

# %% ../nbs/00_template.ipynb 17
#| code-fold: true
# Like before

# %% ../nbs/00_template.ipynb 20
#| code-fold: true
def h() -> str:
    return "What, another stub?"


# %% ../nbs/00_template.ipynb 31
#| code-fold: true
def get_answer(x: int,   # An x
               y: int,   # A y
              )-> str:   # An xy
    """Find the ...."""
    return "CMZ"

# %% ../nbs/00_template.ipynb 42
#| code-fold: true
def baz_the_foo(
    n:   int|str,  # Move this many
    old: list,     # From this stack
    new: list,     # To this stack
    )-> None:      # MODIFIES the stacks!
    """Move `n` things from `from_col` to `to_col` AS A GROUP."""
    for x in reversed([old.pop() for i in range(int(n))]):
        new.append(x)