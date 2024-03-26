import flask, time, waitress

inp=""
out = ""

app= flask.Flask(__name__)

@app.route("/")
def home():
  return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Submit Command</title>
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f4f4f4;
    }
    .container {
        text-align: center;
    }
    input[type="text"] {
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 5px;
        margin-right: 10px;
    }
    input[type="submit"] {
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        background-color: #007bff;
        color: #fff;
        cursor: pointer;
    }
    input[type="submit"]:hover {
        background-color: #0056b3;
    }
</style>
</head>
<body>
<div class="container">
    <form action="/run" method="get">
        <input type="text" name="cmd" placeholder="Enter command">
        <input type="submit" value="Submit">
    </form>
</div>
</body>
</html>

"""

@app.route("/successful")
def success():
  cmd=flask.request.args.get("cmd")
  return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Submit Command</title>
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f4f4f4;
    }
    .container {
        text-align: center;
    }
    input[type="text"] {
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 5px;
        margin-right: 10px;
    }
    input[type="submit"] {
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        background-color: #007bff;
        color: #fff;
        cursor: pointer;
    }
    input[type="submit"]:hover {
        background-color: #0056b3;
    }
</style>
</head>
<body>
<div class="container">
    <h4>"""+cmd+"""</h4>
    <form action="/run" method="get">
        <input type="text" name="cmd" placeholder="Enter command">
        <input type="submit" value="Submit">
    </form>
</div>
</body>
</html>

"""

@app.route("/run")
def runner():
  cmd=flask.request.args.get("cmd")
  global inp
  inp+=cmd
  return flask.redirect(f"/successful?cmd={cmd}")
  #return "Go To <a href='/runoutput'> Output </a>"

"""@app.route("/runoutput")
def runoutput():
  global out
  x=""
  x+=out
  out=""
  return x
"""

@app.route("/torun")
def torun():
  global inp
  x=""
  x+=inp
  inp=""
  return x

"""@app.route("/output")
def output():
  global out
  inputt=flask.request.args.get("str")
  out+=inputt
  return out
"""
#app.run(port=8000, host='0.0.0.0')
waitress.serve(app, port=8000, host='0.0.0.0')
