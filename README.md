# PRSentinel demo project

A tiny calculator, used to show [PRSentinel](https://github.com/Ankxth/prsentinel)
working on real pull requests. It is one file, `calculator.py`, and only uses
the standard library.

| function | what it does |
| --- | --- |
| `add(a, b)` | a + b |
| `subtract(a, b)` | a - b |
| `multiply(a, b)` | a * b |
| `divide(a, b)` | a / b; dividing by zero raises `ValueError` |
| `calculate(operator, a, b)` | applies `+`, `-`, `*` or `/`; any other operator raises `ValueError` |
| `evaluate(expression)` | reads text such as `"12 / 4"` and returns `3.0` |
| `main(argv)` | command line: `python calculator.py "12 / 4"` |

When a pull request changes `calculator.py`, the PRSentinel workflow in
`.github/workflows/prsentinel.yml` lists the changed functions and updates the
code map of this repository. Test generation and vulnerability checks are not
switched on yet.
