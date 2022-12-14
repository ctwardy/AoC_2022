AoC_2022
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This is my first year of AoC, and I’ve decided to use it to practice
with [nbdev](https://nbdev.fast.ai) to automatically generate modules
and [documentation](https://ctwardy.github.io/AoC_2022/) from my
notebooks.

I’ll probably evolve my organization as I go. I did Day 1 with a regular
python module and that made sense to put each day in its own folder with
data as `input.txt`. But I think with nbdev it makes sense to have the
usual `nbs` folder for all the notebooks, one per day. In that case I’ll
put the data in `data/dayX_input.txt`. Like so:

``` python
!ls data/
```

    day0_example.txt day3_input.txt   day6_example.txt
    day0_input.txt   day4_input.txt   day6_input.txt
    day2_input.txt   day5_input.txt   day7_input.txt

![CI](https://github.com/ctwardy/AoC_2022/actions/workflows/test.yaml/badge.svg)
![Deploy](https://github.com/ctwardy/AoC_2022/actions/workflows/deploy.yaml/badge.svg)

Not sure the AoC badges are working quite right? Do I have to update
manually?

![](https://img.shields.io/badge/day%20📅-8-blue.png)
![](https://img.shields.io/badge/stars%20⭐-14-yellow.png)
![](https://img.shields.io/badge/days%20completed-7-red.png)

## Explore

Please feel free to:

- [Browse the lovely documentation](https://ctwardy.github.io/AoC_2022/)
  automatically generated by nbdev, or
- [View the code](https://github.com/ctwardy/AoC_2022).

## How to use

Nbdev creates python modules from notebooks, so if you clone the repo
you can call exported functions using the `AoC_2022` package.

1.  Get the code. If using the GitHub CLI:

``` shell
gh repo clone ctwardy/AoC_2022
```

2.  Install the package locally so `AoC_2022` is in your namespace.

``` shell
pip install -e '.[dev]'
```

Then you can do something like this:

``` python
import AoC_2022.day2 as day2

with open("data/day2_input.txt") as f:
    data = [day2.rps_decode(x.strip()) for x in f.readlines()]
day2.score_strategy(data)
```

    13022

# Observations

## Day 1: Calorie Counting

Wait! It’s December already? OK, just write Python using nano and
commandline. That wasn’t so bad. I’m not fast, but it was
straightforward.

## Day 2: Rock Paper Scissors

OK, installed the new nbdev. Used `str.translate` to change from ABC to
RPS. In Part 2 that needed an extra step to look at the opponents move,
but strategy dictionary seemed an okay approach.

## Day 3: Rucksack Reorg

Learning more nbdev features like docments and code-folding. I think
docments make the function declaration slightly uglier, but the
generated docs are amazing. Worth it.

**Programming**: got to use `functools.reduce`.

**Nbdev**: Local docs were pretty easy. Spent *hours* troubleshooting on
GitHub. Docs didn’t like index.ipynb using `../data/` for file location.
Solved by making `nbs/data -> ../data` and then referring to `data/`.
Later saw this in the docs:

<div>

> **Note**
>
> All documentation related files should be included in your nbs_path,
> and all paths should be relative to it. …

</div>

## Day 4: Camp Cleanup

Was able to follow the Day 3 nbdev template. Solution was
straightforward, but all told still me a bit more than an hour. Hm. Over
90 minutes after adding this section to the README (index.ipynb). Nbdev
makes documentation tempting. That’s not necessarily a bad thing.

**Nbdev**: `nbdev_prep` caught a leftover day3 cell at the bottom of my
day4 notebook. Cool. But after fixing, the running preview still didn’t
have day4. But stopping and re-running did. Guess that’s a thing.

## Day 5: Supply Stacks

This took me surprisingly long. I had the example parsed in 45 minutes,
but then realized `move()` would be easier with stacks, and iterating on
that entered a regress. Once the example ran, Part 1 followed with one
tweak, then Part 2 needed only a quick rewrite of `move()`.

**Nbdev**: Worked locally but GitHub CI still failed. Hoo boy.

1.  `import numpy` but `numpy` not found. Either add `numpy` dependency
    to `settings.ini` or drop. Not using yet. Dropped.
2.  I had used 3.10 type hints like `int|str`. But GH was using 3.9 so
    this failed in CI. Bumped `settings.ini` to specify 3.10.
3.  GH still using 3.9, which now failed to satisfy min version.
4.  Changed `setup.py` to force 3.10. Same error.
5.  Modify `.github/workflows/test.yml` per [this forum
    post](https://forums.fast.ai/t/python-version-error-while-running-ci-operations-in-github/98482/8).
    Same type hints error.
6.  Go back to min of 3.8, and use `from __future__ import annotations`.
    Supposed to work. Same error.
7.  Add 3.10 to `.github/workflows/deploy.yml` as well. Kill
    `__future__`. Success.

Combo of something not quite working in `nbdev` config, and me not
knowing how GitHub CI worked. Better now, I think.

## Day 6: Tuning Trouble

This one was much easier. About 7-10 minutes to write up the example,
and another 5-10 minutes to solve. It was quick to see that
`len(set(s)) == n` would do it. The rest was just typing and fixing.

**Nbdev:** ran find, but `nbdev_preview` hit a weird glitch where it
forgot `examples` in the cell defining `get_pos_firstn_uniq()`, despite
knowing it in the previous or next cell. So I just split the cell.

## Day 7: No space on device

Needed recursive ops to make & query a directory tree. Started with a
simple class, then two helpers. Then noticed calls could be simpler if I
defined magic methods like `__getitem__` and `__iter__`. Realized dirs
needed to track `parent` which provided full `path` and `depth`.
Recursion took some tuning. **Lessons learned:**

- **Software Eng:** Beware copy/paste! Lost hours because call to Part1
  had the wrong input. 🤦‍♂️
- **Software Eng:** Incremental tests helped. Also, don’t be clever.
- **Classes:**
  [`Directory`](https://ctwardy.github.io/AoC_2022/day7.html#directory)
  methods *can* use `isinstance(arg, Directory)`: it’s not defined yet,
  but it *will be* before use. Clearer and more correct than
  `if type(x) == type(me)`. But until 3.11 we can’t use
  [`Directory`](https://ctwardy.github.io/AoC_2022/day7.html#directory)
  as a type hint inside
  [`Directory`](https://ctwardy.github.io/AoC_2022/day7.html#directory).
- **Default mutable!** Declaring `_kids = []` as a `@dataclass` is a
  default mutable in `__init__`. Bad!

## –\> Remove Data, Break CI & Pages \<–

**Removed AoC data from GitHub.**

Alas, that means the GitHub CI fails because the notebooks won’t find
their data. And that means the nice pages docs won’t build.

Hm.

Fetching the data from AoC requires login - will have to look into how
to use secrets in GitHub CI.

## Day 8: Treehouse

Straightforward but finicky. Many off-by-one-ish errors, esp. Part 2.
Two mornings.

**Part 1** had two short functions: `edges()` used `np.pad()` to make a
border of `1`s, then `vismap()` used a nested for loop to check the
interior. Had to remember `.all()`, like `(row < height).all()`.

**Part 2** is just a nested loop, but ugly math to handle off-by-one and
edge effects. Like

    right = 1 + where_if(row[j+1:] >= height, 
                         _else=cols-j-2)[0]

I’m sure there must be a clearer approach.
