from fastapi import FastAPI, Response, status

app = FastAPI(title="Teapot API", version="1.0")

@app.get("/teapot", status_code=status.HTTP_418_IM_A_TEAPOT)
def get_teapot():
    return {"message": "I'm a teapot 🫖"}
