from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import oAuthPasswordBearer


app = FastAPI()

@app.get("/test/")
async def test():
    return{"hello":"world"}