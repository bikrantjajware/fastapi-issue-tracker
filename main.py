from fastapi import FastAPI
from app.routes.issues_router import router as issues_router
from app.routes.practice_route import router as practice_router

app = FastAPI()

app.include_router(issues_router, prefix='/api/v1')
app.include_router(practice_router, prefix='/api/v1')




@app.get('/health')
def health_check():
    return {"status": "ok"}
