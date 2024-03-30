

thing0: str
thing1: str = "yeti"
thing1 = "47"


# mypy stuff.py

# (venv) (base) ➜  testing-fast-api git:(main) ✗ mypy stuff.py
# stuff.py:5: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 1 error in 1 file (checked 1 source file)
# (venv) (base) ➜  testing-fast-api git:(main) ✗ mypy stuff.py
# Success: no issues found in 1 source file
# (venv) (base) ➜  testing-fast-api git:(main) ✗
