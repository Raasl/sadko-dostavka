FROM python:3.11.3-alpine
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root
COPY . .
EXPOSE 8000
# ENTRYPOINT ["python", "sadko/manage.py", "runserver"]
# CMD ["0.0.0.0:8000"]