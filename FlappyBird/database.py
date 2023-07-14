import sqlite3,os

def crear_tabla():
    """
    Creo una tabla, si no esta creada la crea con las 2 columnas, name y score.
    Utilizo la biblioteca sqlite para conectarme a la base de datos.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "scores.db")

    # Creo una conexión a la base de datos
    conn = sqlite3.connect(db_path)
    """
    c = conn.cursor() Creo un objeto cursor que permite interactuar con la base de datos a 
    través de la conexión establecida (conn).
    """
    c = conn.cursor()

    # Creo la tabla si no existe
    c.execute("CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)")

    # Guardo cambios y cierro la conexión
    conn.commit()
    conn.close()

def guardo_score(name, score):
    """
    Guarda un puntaje en la base de datos. Recibe como parámetros el nombre y el puntaje a guardar. 
    Primero, se conecta a la base de datos y obtiene el puntaje más alto existente. 
    Si el puntaje pasado como parámetro es mayor que el puntaje más alto existente o no hay puntaje 
    existente, se elimina el puntaje existente (si hay alguno) y se inserta el nuevo puntaje en 
    la tabla "scores". La función asegura que el puntaje se almacene como un número entero.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "scores.db")

    # Conectar a la base de datos y obtener el puntaje actual
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT score FROM scores ORDER BY score DESC LIMIT 1")
    result = c.fetchone()

    if result is None or score > result[0]:
        # Eliminar el puntaje existente si hay alguno
        c.execute("DELETE FROM scores")
        
        # Insertar el nuevo puntaje más grande
        c.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, int(score)))

    conn.commit()
    conn.close()

def verifico_tabla_existente():
    """
    Verifico si la tabla "scores" existe en la base de datos. 
    Utilizo una consulta para buscar la tabla en el esquema de la base de datos. 
    Devuelve True si la tabla existe y False en caso contrario.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "scores.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Verifico si la tabla "scores" existe en la base de datos
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='scores'")
    table_exists = cursor.fetchone() is not None

    cursor.close()
    conn.close()

    return table_exists

def obtengo_puntaje_mas_alto():
    """
    Obtengo el puntaje más alto registrado en la tabla "scores". 
    Se conecta a la base de datos, ejecuta una consulta que devuelve el máximo puntaje de la columna 
    "score" y luego extrae el valor del resultado obtenido. Si no hay puntajes registrados, devuelve 0.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "scores.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Obtengo el puntaje más alto de la tabla "scores"
    cursor.execute("SELECT MAX(score) FROM scores")
    result = cursor.fetchone()
    highest_score = result[0] if result and result[0] else 0

    cursor.close()
    conn.close()

    return highest_score

def nombre_puntaje_mas_alto():
    """
    Obtengo el nombre asociado al puntaje más alto registrado en la tabla "scores". 
    Primero, obtiene el puntaje más alto utilizando la función obtengo_puntaje_mas_alto(). 
    Luego, ejecuta una consulta para obtener el nombre correspondiente a ese puntaje. 
    Si se encuentra un resultado, se extrae el nombre; de lo contrario, se devuelve "N/A" (no disponible).
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "scores.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Obtener el puntaje más alto de la tabla "scores"
    cursor.execute("SELECT MAX(score) FROM scores")
    result = cursor.fetchone()
    highest_score = result[0] if result and result[0] else 0

    # Obtener el nombre asociado al puntaje más alto
    cursor.execute("SELECT name FROM scores WHERE score=?", (highest_score,))
    result = cursor.fetchone()
    highest_score_name = result[0] if result else "N/A"

    cursor.close()
    conn.close()

    return highest_score_name
