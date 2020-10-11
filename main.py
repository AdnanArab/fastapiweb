from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/something")
async def get_some_dictionary():
    return {"Adnan": "Arab", "Something Else": "Something Else"}

if __name__ == ("__main__"):
    uvicorn.run(app, host="127.0.0.1", port=9000)