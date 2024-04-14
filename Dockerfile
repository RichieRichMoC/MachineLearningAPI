FROM python:3.12.1

WORKDIR /app

COPY requirement.txt /requirement.txt


RUN python -m pip install -r /requirement.txt

COPY . /app

EXPOSE 800

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "800"]
