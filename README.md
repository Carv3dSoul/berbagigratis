# Gift Portal

Simple login page that serves `gift.jpg`.

## Run

1. Put your `gift.jpg` in this folder (next to `app.py`).
2. Install Flask:
   ```
   pip install -r requirements.txt
   ```
3. Start it:
   ```
   python app.py
   ```
4. Open http://127.0.0.1:5000 — log in with anything, the gift shows up.

To serve on the network instead of localhost, change the last line of
`app.py` to `app.run(host="0.0.0.0", port=5000)`.
