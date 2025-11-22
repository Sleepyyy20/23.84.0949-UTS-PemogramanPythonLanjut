run:
	python "c:\Users\FaizalHall\Documents\UTS SEM5\Python Lanjut\zigzag.py" --width 20 --speed 0.1

test:
	pytest -q

lint:
	black --check .
	flake8 .
