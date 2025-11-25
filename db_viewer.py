#!/usr/bin/env python3
"""Simple SQLite Database Viewer"""
import sqlite3
from flask import Flask, render_template_string
import json

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Database Viewer - Ask Chopper</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            background: #0d0d0d;
            color: #ffffff;
            padding: 40px;
        }
        h1 { margin-bottom: 30px; color: #ffffff; }
        h2 {
            color: #ffffff;
            margin: 30px 0 15px 0;
            padding: 10px;
            background: #1a1a1a;
            border-radius: 5px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 40px;
            background: #1a1a1a;
            border-radius: 10px;
            overflow: hidden;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #2d2d2d;
        }
        th {
            background: #000000;
            font-weight: 600;
            color: #ffffff;
        }
        td { color: #cccccc; }
        tr:hover { background: #222222; }
        .empty {
            padding: 20px;
            color: #666666;
            font-style: italic;
        }
        .stats {
            background: #1a1a1a;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 30px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <h1>📊 Ask Chopper Database Viewer</h1>

    {% for table_name, data in tables.items() %}
        <h2>{{ table_name }} <span class="stats">({{ data|length }} rows)</span></h2>

        {% if data %}
            <table>
                <thead>
                    <tr>
                        {% for column in data[0].keys() %}
                            <th>{{ column }}</th>
                        {% endfor %}
                    </tr>
                </thead>
                <tbody>
                    {% for row in data %}
                        <tr>
                            {% for value in row.values() %}
                                <td>{{ value }}</td>
                            {% endfor %}
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% else %}
            <div class="empty">No data in this table yet</div>
        {% endif %}
    {% endfor %}
</body>
</html>
"""

def dict_factory(cursor, row):
    """Convert database row to dictionary"""
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

@app.route('/')
def view_database():
    conn = sqlite3.connect('/tmp/ask_chopper.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()

    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    table_names = [row['name'] for row in cursor.fetchall()]

    tables = {}
    for table_name in table_names:
        cursor.execute(f"SELECT * FROM {table_name}")
        tables[table_name] = cursor.fetchall()

    conn.close()

    return render_template_string(HTML_TEMPLATE, tables=tables)

if __name__ == '__main__':
    print("Database Viewer running at: http://127.0.0.1:8080")
    print("                          : http://192.168.100.216:8080")
    app.run(host='0.0.0.0', port=8080, debug=False)
