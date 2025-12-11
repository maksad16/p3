from flask import Flask, render_template_string
app = Flask(__name__)
HTML = """
<!doctype html>
<html><body>
 <h1>Student Portal</h1>
 <p>Registration form:</p>
 <form>
 Name: <input name="name"><br>
 Email: <input name="email"><br>
 Phone: <input name="phone"><br>
 Department: <input name="department"><br>
 </form>
</body></html>
"""
@app.route("/")
def home():
 return render_template_string(HTML)
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)

# docker build -t student-portal:v1 .
# docker run -d --name student-portal -p 5000:5000 student-portal:v1
# curl -s http://localhost:5000 | head -n 10

# PROGRAM 5
# docker ps -a
# docker images
# docker stop student-portal
# docker rm student-portal
# docker rmi student-portal:v1
