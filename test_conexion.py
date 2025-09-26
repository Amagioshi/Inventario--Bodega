import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=localhost\\SQLEXPRESS;'
        'DATABASE=InventarioBodega;'
        'Trusted_Connection=yes;'
        'Encrypt=no;'
    )
    print(" Conexión exitosa a la base de datos.")
    conn.close()
except Exception as e:
    print("❌ Error al conectar:", e)