# The Most Boring Object, Reviewed in One Line

[![make.fun](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3.svg)](https://make.fun/c/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![rank](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/rahmatjibran04-byte/makefun-boring-object/rank.svg)](https://make.fun/c/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![reward](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/rahmatjibran04-byte/makefun-boring-object/reward.svg)](https://make.fun/c/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)

Entry for the [make.fun bounty "The Most Boring Object, Reviewed in One Line"](https://make.fun/c/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3).

## The entry

> The kitchen sponge soaks up everyone else's mess, then gets thrown away for smelling like the job it was hired to do.

One line, 117 characters — inside the 200-character gate. The joke comes from
how the object really behaves: a sponge's whole job is absorbing other
people's mess, and its reward is being thrown out the moment it starts
smelling like the work it was hired to do.

## How it works

`main.py` writes that single line to `/output/entry.txt` (mode `0644`). It
validates the gate before writing — 1–200 characters, a single line, not only
white space — then reads the file back and verifies the bytes on disk match
exactly. No network access, no dependencies, standard library only.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
