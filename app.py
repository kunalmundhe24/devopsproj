from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize tasks as an empty list
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task_content = request.form.get("content")
    if not task_content or not task_content.strip():
        return "Task is required", 400
    tasks.append({"content": task_content, "completed": False})
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

# Ensure app does not run when imported
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)