def init_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="ivan"
        )
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'annuaire'")
        exists = cursor.fetchone()

        if not exists:
            cursor.execute('CREATE DATABASE annuaire')
            print("Base de données 'annuaire' créée avec succès!")

        cursor.close()
        conn.close()

        conn = psycopg2.connect(
            host="localhost",
            database="annuaire",
            user="postgres",
            password="ivan"
        )
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contactxst (
                id SERIAL PRIMARY KEY,
                nom VARCHAR(100) NOT NULL,
                prenom VARCHAR(100) NOT NULL,
                telephone VARCHAR(20) NOT NULL,
                poste VARCHAR(100) NOT NULL,
                agence VARCHAR(100) NOT NULL,
                date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

    except Exception as e:
        print(f"Erreur lors de l'initialisation de la base de données: {e}")
        if conn:
            conn.rollback()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    import psycopg2
    init_db()