FROM python:3.11-slim


WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

COPY models/ /app/models/

COPY . /app/

EXPOSE 5000

CMD ["pipenv", "run", "python", "app/app.py"]
