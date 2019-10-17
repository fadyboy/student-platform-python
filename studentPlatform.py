from studentapp import app, db
from studentapp.models import Admin

@app.shell_context_processor
def make_shell_context():
    return {"app": app, "db":db, "Admin":Admin}