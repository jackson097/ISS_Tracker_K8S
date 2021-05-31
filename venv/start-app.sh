manage=/deploy/venv/src/manage.py
python $manage makemigrations Coords
python $manage migrate
python $manage runserver 0.0.0.0:8000