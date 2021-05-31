FROM python:latest

COPY ./ /deploy/venv

RUN pip install django
RUN python -m pip install requests

EXPOSE 8000

CMD ["/bin/sh", "-c", "/deploy/venv/start-app.sh"]