# Zigzag

Simple terminal animation refactored into a module with CLI.

Quick commands (Windows PowerShell):

- Run the animation (default):

```powershell
python "c:\Users\FaizalHall\Documents\UTS SEM5\Python Lanjut\zigzag.py"
```

- Run with options (example):

```powershell
python "c:\Users\FaizalHall\Documents\UTS SEM5\Python Lanjut\zigzag.py" --width 12 --speed 0.05 --char "#" --count 100
```

- Use the provided PowerShell helper scripts in `scripts/`:

```powershell
# Run with defaults
.\scripts\run.ps1

# Run with custom values
.\scripts\run.ps1 -width 15 -speed 0.02 -char "#" -count 50

# Run tests (requires pytest)
.\scripts\test.ps1

# Run linters/format checks (requires black, flake8)
.\scripts\lint.ps1
```

Makefile targets (if you have `make`):

- `make run` — run the app
- `make test` — run tests
- `make lint` — run format/lint checks

Requirements for development (put in `requirements.txt`):

- `pytest`
- `black`
- `flake8`

Notes

- On Windows use PowerShell to run the `scripts/*.ps1` files. The Makefile is included for convenience on systems that have `make` installed.
- To run the module as a library, import `run_zigzag` from `zigzag`.
