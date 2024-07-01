FROM python:3.11

COPY . /src
WORKDIR /src

RUN chmod +x /src/requirements.txt
RUN pip install -r requirements.txt

CMD ["uvicorn", "--port", "8000", "--host", "0.0.0.0", "main:app"]

EXPOSE 8000