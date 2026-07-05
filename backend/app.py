from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Troubleshooting Agent backend is running!"}
