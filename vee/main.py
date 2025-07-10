from fastapi import FastAPI

app = FastAPI(title="Vee - Go To Market Platform")

@app.get("/")
async def root():
    return {"message": "Welcome to Vee"}

# Placeholder routers for modules

from .modules import product_marketing, sales_enablement, product_management

app.include_router(product_marketing.router, prefix="/marketing", tags=["Product Marketing"])
app.include_router(sales_enablement.router, prefix="/sales", tags=["Sales Enablement"])
app.include_router(product_management.router, prefix="/product", tags=["Product Management"])
