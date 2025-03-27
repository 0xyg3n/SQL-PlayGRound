FROM python:3.11-slim

WORKDIR /app

# --- Install Microsoft SQL Server ODBC Driver ---
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl gnupg2 apt-transport-https \
 && apt-get remove -y unixodbc unixodbc-dev libodbc1 libodbccr2 libodbcinst2 odbcinst odbcinst1debian2 \
 && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
 && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
 && apt-get update \
 && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev \
 && rm -rf /var/lib/apt/lists/*

# --- Install Python dependencies ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy app source files ---
COPY app.py .
COPY static ./static
COPY templates ./templates

# --- Start the Flask app ---
CMD ["python", "app.py"]
