from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database import Base, engine
from routers import products, cart, auth, orders
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
images_dir = os.path.join(os.path.dirname(__file__), "images")
app.mount("/images", StaticFiles(directory=images_dir), name="images")

# Routers
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(auth.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "Backend running"}
