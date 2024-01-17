from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)

class Contact:
    def __init__(self, contact_tuple) -> None:
        self.id=contact_tuple[0]
        self.name=contact_tuple[1]
        self.phone=contact_tuple[2]
        self.email=contact_tuple[3]
        self.address=contact_tuple[4]
        self.user=contact_tuple[5]

def get_contacts():
    with sqlite3.connect("contacts.db") as conn:
        cur=conn.cursor()
        rows=cur.execute("SELECT * FROM contacts")
        return [Contact(row) for row in rows.fetchall()]


@app.route('/')
def home():
    return render_template("home.html", contacts=get_contacts())
