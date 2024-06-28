from fastapi import FastAPI, HTTPException
import math
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, nfactorial!"}


@app.post("/meaning-of-life")
def post_meaning_of_life():
    return {"meaning": 42}


@app.get("/{num}")
def get_factorial(num: int):
    if num < 0:
        raise HTTPException(status_code=400, detail="Number must be non-negative")
    factorial = math.factorial(num)
    return {"nfactorial": factorial}
