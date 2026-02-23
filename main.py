from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os

app = FastAPI(title="Papelaria API")

# ==========================
# CORS CONFIG
# ==========================
origins = [
    "http://localhost:3000",  # frontend local
    "https://SEU_FRONTEND.vercel.app",  # troque depois
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # pode restringir depois
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# MOCK DATABASE
# ==========================
products = [
    {
        "id": 1,
        "slug": "caderno-floral",
        "title": "Caderno Floral",
        "description": "Caderno delicado com capa floral.",
        "price": 49.90,
        "image": "https://via.placeholder.com/400"
    },
    {
        "id": 2,
        "slug": "planner-minimalista",
        "title": "Planner Minimalista",
        "description": "Planner moderno e elegante.",
        "price": 59.90,
        "image": "https://via.placeholder.com/400"
    },
    {
        "id": 3,
        "slug": "kit-canetas-pastel",
        "title": "Kit Canetas Pastel",
        "description": "Kit com 10 cores suaves.",
        "price": 29.90,
        "image": "https://via.placeholder.com/400"
    }
]

# ==========================
# ROUTES
# ==========================

@app.get("/")
def root():
    return {"message": "API Papelaria funcionando 🚀"}

@app.get("/products")
def get_products():
    return products

@app.get("/products/{slug}")
def get_product(slug: str):
    product = next((p for p in products if p["slug"] == slug), None)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return product

@app.get("/search")
def search_products(q: str):
    results = [
        p for p in products
        if q.lower() in p["title"].lower()
    ]
    return results

# ==========================
# RENDER COMPATIBILITY
# ==========================

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)