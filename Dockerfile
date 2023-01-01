FROM python

WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt

RUN pip install -Ur requirements.txt

COPY . /app/

ENV JWTS_HOST=0.0.0.0 JWTS_PORT=80

EXPOSE $JWTS_PORT

CMD ["python3", "main.py" ]