# Lab 5 — Static Code Analysis Findings

## Initial Analysis

- **Program:** `support_ticket_tracker.py`
- **Pylint initial score:** 5.00/10
- **Bandit:** 2 findings (1 Low, 1 Medium)
- **Flake8:** 12 reported violations

## Issue Documentation

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Bug / Code quality | 10 | `audit_log=[]` is shared between calls when no argument is provided. | Change the default to `None` and initialize a new list inside the function. |
| Bare exception | Bug / Security | 24 | A bare `except` catches unexpected exceptions and the code silently ignores them. | Catch the specific expected exception, such as `KeyError`, and remove the silent `pass`. |
| Unsafe `eval()` | Security | 92 | Bandit B307 identifies potentially unsafe dynamic code execution. | Remove the unnecessary unsafe demo or replace it with a normal, explicit operation. |
| File handling | Code quality | 46, 53 | Files are opened without context managers or an explicit encoding. | Use `with open(...)` and specify `encoding="utf-8"`. |
| Incorrect `None` comparison | Style / Code quality | 37 | Uses `status != None`. | Use `status is not None`. |
| Unused imports | Style | 4, 5 | `sys` and `random` are imported but unused. | Remove the unused imports. |
| Unused variable | Style | 84 | `count` is assigned but never used. | Remove the variable or use it meaningfully. |
| Overlong lines | Style | 10, 14, 63–80 | Several lines exceed the configured Flake8 line-length limit. | Split long expressions and calls across multiple lines. |

## Verification

- Initial reports saved before changes.
- Final reports to be generated after fixes.
- Final Pylint target: greater than 9.5/10.
- All Bandit findings and Flake8 violations to be addressed.
