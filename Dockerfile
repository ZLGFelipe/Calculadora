FROM python:3.12.4-slim

COPY . .

CMD ["python", "Calculadora.py"]