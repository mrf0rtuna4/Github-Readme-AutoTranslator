FROM python:3.11-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml uv.lock ./

RUN uv export --no-dev --frozen --format requirements-txt > /tmp/requirements.txt \
    && uv pip install --system -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY core ./core

ENTRYPOINT ["python", "core/main.py"]