FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/arch_agent/ .

EXPOSE 8082

CMD ["uvicorn", "arch_agent:app", "--host", "0.0.0.0", "--port", "8082"]
