from fastapi import FastAPI
from database import engine
import models
from routers import posts, users, auth, likes
from pydantic import BaseSettings
from config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(likes.router)

@app.get("/")
def root():
    return {"message": "Welcome"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"status": posts}







