FROM python:3.8-slim AS temp_image
RUN apt-get update && apt-get install -y
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN mkdir -p /app/static
COPY requirements.txt /app
RUN pip install --upgrade pip && \
    pip install wheel && \
    pip install -r /app/requirements.txt
FROM python:3.8-slim
COPY --from=temp_image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY app /app/app
RUN mkdir -p /app/app/static

# add a simple user
RUN groupadd -r --gid 1234 www && useradd -r -u 1234 -g www www

# give ownership and switch to this user
RUN chown -R www:www /app
USER www:www

WORKDIR /app/

EXPOSE 8000
ENTRYPOINT gunicorn -k uvicorn.workers.UvicornWorker app.main:app -b 0.0.0.0:8000
