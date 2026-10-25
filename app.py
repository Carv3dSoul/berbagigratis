from flask import Flask, request, send_from_directory, Response
from pathlib import Path

app = Flask(__name__)
HERE = Path(__file__).parent

# Login is cosmetic only: we never store, log, or forward what's typed.
LOGIN_PAGE = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Gift Portal - Login</title>
  <style>
    body{font-family:sans-serif;background:#111;color:#eee;display:flex;
         height:100vh;align-items:center;justify-content:center;margin:0}
    .card{background:#1d1d1d;padding:32px 40px;border-radius:12px;width:300px;
          box-shadow:0 8px 30px rgba(0,0,0,.5)}
    h2{margin:0 0 4px;text-align:center}
    p{margin:0 0 20px;text-align:center;color:#999;font-size:13px}
    input{width:100%;padding:10px;margin:6px 0;border:0;border-radius:6px;
          box-sizing:border-box;background:#2a2a2a;color:#eee}
    button{width:100%;padding:10px;margin-top:12px;border:0;border-radius:6px;
           background:#e55;color:#fff;font-weight:bold;cursor:pointer}
  </style>
</head>
<body>
  <form class="card" action="/login" method="POST">
    <h2>🎁 Gift Portal</h2>
    <p>Log in to claim your gift</p>
    <input name="username" placeholder="Username" autocomplete="off">
    <input name="password" type="password" placeholder="Password" autocomplete="off">
    <button type="submit">Log in</button>
  </form>
</body>
</html>"""

GIFT_PAGE = """<!doctype html>
<html>
<head><meta charset="utf-8"><title>Your Gift</title>
  <style>body{font-family:sans-serif;background:#111;color:#eee;text-align:center;padding:40px}
         img{max-width:420px;border-radius:12px;margin:20px auto;display:block}
         a{color:#e55}</style>
</head>
<body>
  <h2>🎉 Here is your gift</h2>
  <img src="/gift.jpg" alt="gift">
  <p><a href="/gift.jpg" download>Download gift.jpg</a></p>
  <p><a href="/">Log out</a></p>
</body>
</html>"""


@app.route("/")
def index():
    return LOGIN_PAGE


@app.route("/login", methods=["POST"])
def login():
    # Any credentials "work"; nothing is kept.
    return GIFT_PAGE


@app.route("/gift.jpg")
def gift():
    if not (HERE / "gift.jpg").exists():
        return Response("gift.jpg not found - drop your image in this folder", 404)
    return send_from_directory(HERE, "gift.jpg", mimetype="image/jpeg")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
