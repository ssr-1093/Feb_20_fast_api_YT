from fastapi import FastAPI
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World from Sumedha !! Now add '/test' to test the API further"}

@app.get("/test")
async def root():
    return {"message":"this is test! I'm Hosting this on AWS EC2 instance"}
    
