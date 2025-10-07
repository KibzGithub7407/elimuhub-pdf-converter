# Elimuhub PDF Converter (Smallpdf-powered)

Simple Flask app that uploads a file and uses the Smallpdf API (PDF → Word) to convert documents.

## Files
- `app.py` — main Flask application
- `templates/index.html` — upload page
- `requirements.txt` — Python dependencies
- `Procfile` — for Render or similar PaaS

## Setup (Local)
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # mac/linux
   venv\Scripts\activate    # windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Smallpdf API key as an environment variable:
   ```bash
   export SMALLPDF_API_KEY=your_key_here   # mac/linux
   set SMALLPDF_API_KEY=your_key_here      # windows (cmd)
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open http://127.0.0.1:5000 in your browser.

## Deploy to Render.com
1. Push this repo to GitHub.
2. Create a new Web Service on Render and connect your repo.
3. Set **Start Command** to: `gunicorn app:app`
4. Add an Environment Variable `SMALLPDF_API_KEY` with your key.
5. Deploy — Render will provide a public URL.

## Notes & Security
- Keep your API key secret. Use environment variables on the host.
- This example uses streaming to handle large files safely.
- Extend to other endpoints (compress, merge) by changing the Smallpdf API path and UI.
