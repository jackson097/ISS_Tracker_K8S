FROM python:latest

COPY ./ /deploy/venv

RUN pip install django
RUN python -m pip install requests

EXPOSE 8000
CMD ["python", "/deploy/venv/src/manage.py", "runserver", "0.0.0.0:8000"]