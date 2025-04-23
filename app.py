from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize notes as an empty list
notes = []

@app.route("/")
def index():
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    note_content = request.form.get("content")
    if not note_content or not note_content.strip():
        return "Note content is required", 400
    notes.append({"content": note_content})
    return redirect(url_for("index"))

@app.route("/delete/<int:note_id>")
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        notes.pop(note_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
