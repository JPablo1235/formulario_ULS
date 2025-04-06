@app.before_first_request
    def create_tables():
        db.create_all()  # Crea las tablas en la base de datos