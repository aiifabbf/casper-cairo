# casper-cairo
cairo's pure python and pycairo-compatible binding, as a drawing backend of casper project

This project is inspired by [Qahriah](https://github.com/ldo/qahirah), which is the original cairo's pure python binding using python's builtin facility ctypes. Since Qahriah invents a different interface compared with the official python binding pycairo, this project tries to provide APIs that are compatible to pycairo as much as possible.

By the way, cairo's drawing model is fun!

## Features

- *almost* same as pycairo in APIs
- pure Python, no compiling, no GCC! (Well, you still have to get a libcairo.so)
- copy, import and work, thanks to `ctypes`

## Examples

You can run ./test/bach_signature.py to get this pic. Path data is taken from [Wikipedia](https://commons.wikimedia.org/wiki/File:Johann_Sebastian_Bach_signature.svg)

![Bach's Signature](/test/bach_signature.png)

## Docs

No need for me to write docs since you can refer to [pycairo's](http://cairographics.org/documentation/pycairo/3/reference).

But I wrote some notes along with the source codes and you can check out them about the origins of the callables, and my confusals during the implementing process :D.

## Todos

- Error handling (This is urgent)
- Performance (Since I intend to use it to draw GUI)
- Other surface types