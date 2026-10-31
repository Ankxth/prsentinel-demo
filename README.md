# PRSentinel demo project

A tiny Python project used to show [PRSentinel](https://github.com/Ankxth/prsentinel)
working on real pull requests.

Every module here is self-contained (it only uses the standard library), because
PRSentinel tests each changed file on its own.

| module | what it does |
| --- | --- |
| `scores.py` | the most recent scores, and their average |
| `cart.py` | add and remove items in a shopping cart |
| `offers.py` | pick which offer code to apply |
| `textutils.py` | word count and initials |

When a pull request changes one of these files, the PRSentinel workflow in
`.github/workflows/prsentinel.yml` generates tests for the changed functions,
runs them against the old and the new code, and leaves one comment on the pull
request saying which tests point to a real bug.
