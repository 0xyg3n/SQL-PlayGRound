from flask import Flask, jsonify, request, render_template
import mysql.connector
import psycopg2
import pyodbc
import oracledb
import sqlite3
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/version/<dbtype>")
def version(dbtype):
    dbtype = dbtype.upper()
    if dbtype == "MYSQL":
        return jsonify(result=get_mysql_version())
    elif dbtype == "POSTGRESQL":
        return jsonify(result=get_postgresql_version())
    elif dbtype == "MSSQL":
        return jsonify(result=get_mssql_version())
    elif dbtype == "ORACLE":
        return jsonify(result=get_oracle_version())
    elif dbtype == "SQLITE":
        return jsonify(result=get_sqlite_version())
    else:
        return jsonify(error="Unsupported DBMS"), 400

@app.route("/query/<dbtype>", methods=["POST"])
def run_query(dbtype):
    dbtype = dbtype.upper()
    data = request.get_json()
    user_query = data.get("query")

    if not user_query:
        return jsonify(error="No SQL query provided"), 400

    try:
        if dbtype == "MYSQL":
            conn = mysql.connector.connect(
                host="mysql", user="root", password="password", database="sql_injection_lab"
            )
        elif dbtype == "POSTGRESQL":
            conn = psycopg2.connect(
                host="postgres", user="postgres", password="postgres", database="sql_injection_lab"
            )
        elif dbtype == "MSSQL":
            conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql;UID=sa;PWD=YourStrong!Passw0rd;DATABASE=master"
            )
        elif dbtype == "ORACLE":
            conn = oracledb.connect(user="system", password="oracle", dsn="oracle:1521/FREE")
        elif dbtype == "SQLITE":
            init_sqlite()
            conn = sqlite3.connect("sqlite_lab.db")
        else:
            return jsonify(error="Unsupported DBMS"), 400

        cur = conn.cursor()
        cur.execute(user_query)

        if cur.description:
            columns = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
            result = [dict(zip(columns, row)) for row in rows]
        else:
            conn.commit()
            result = {"message": "Query executed successfully."}

        return jsonify(result=result)

    except Exception as e:
        return jsonify(error=str(e))

def init_sqlite():
    if not os.path.exists("sqlite_lab.db"):
        conn = sqlite3.connect("sqlite_lab.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);")
        cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpass');")
        conn.commit()
        conn.close()

def get_sqlite_version():
    try:
        init_sqlite()
        conn = sqlite3.connect("sqlite_lab.db")
        cur = conn.cursor()
        cur.execute("SELECT sqlite_version();")
        version = cur.fetchone()[0]
        return version
    except Exception as e:
        return f"SQLite Error: {e}"

def get_mysql_version():
    try:
        conn = mysql.connector.connect(
            host="mysql", user="root", password="password", database="sql_injection_lab"
        )
        cur = conn.cursor()
        cur.execute("SELECT @@version;")
        return cur.fetchone()[0]
    except Exception as e:
        return f"MySQL Error: {e}"

def get_postgresql_version():
    try:
        conn = psycopg2.connect(
            host="postgres", user="postgres", password="postgres", database="sql_injection_lab"
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        return cur.fetchone()[0]
    except Exception as e:
        return f"PostgreSQL Error: {e}"

def get_mssql_version():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER=mssql;UID=sa;PWD=YourStrong!Passw0rd;DATABASE=master"
        )
        cur = conn.cursor()
        cur.execute("SELECT @@version;")
        return cur.fetchone()[0]
    except Exception as e:
        return f"MSSQL Error: {e}"

def get_oracle_version():
    try:
        conn = oracledb.connect(user="system", password="oracle", dsn="oracle:1521/FREE")
        cur = conn.cursor()
        cur.execute("SELECT banner FROM v$version")
        return cur.fetchone()[0]
    except Exception as e:
        return f"Oracle Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
