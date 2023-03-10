FROM python:3.10-slim AS base

ARG WORKDIR=/app
ENV PATH="$WORKDIR/.venv/bin:$PATH"
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

WORKDIR $WORKDIR

# Install pip and poetry
RUN pip install --upgrade pip && \
    pip install poetry==1.1.12 && \
    poetry config virtualenvs.in-project true

COPY ./pyproject.toml ./

RUN poetry install --no-dev

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

FROM base AS donkeyapp
COPY ./donkeyapp ./

FROM base AS definitelynotevilapp
COPY ./definitelynotevilapp ./
