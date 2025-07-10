# Vee - Go to Market Platform

This repository contains a minimal FastAPI skeleton for **Vee**, an AI‑native platform designed to unify and automate product, marketing and sales execution.

The current implementation provides placeholder endpoints for the main modules:

- **Product Marketing** (`/marketing`)
- **Sales Enablement** (`/sales`)
- **Product Management** (`/product`)

Run the application locally:

```bash
pip install -r requirements.txt
uvicorn vee.main:app --reload
```

Visit `http://localhost:8000` to see the welcome message.

