from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# https://github.com/ollama/ollama/blob/main/docs/api.md
# https://www.postman.com/postman-student-programs/ollama-api/documentation/suc47x8/ollama-rest-api

# POST /api/chat
@app.get("/api/version")
def chat():
    return {"version": "0.4.3"}

# GET /api/tags
@app.get("/api/tags")
def tags():
    with open('tags.json') as json_file:
        data = json.load(json_file)
    return data

# GET /api/ps
@app.get("/api/ps")
def ps():
    with open('ps.json') as json_file:
        data = json.load(json_file)
    return data

# POST /api/generate
@app.post("/api/generate")
def generate():
    with open('generate.json') as json_file:
        data = json.load(json_file)
    return data

# POST /api/chat
@app.post("/api/chat")
def chat():
    with open('chat.json') as json_file:
        data = json.load(json_file)
    return data

# POST /api/show
@app.post("/api/show")
def show():
    with open('show.json') as json_file:
        data = json.load(json_file)
    return data






# @app.get("/status")
# def check_status():
#     return {"status": "ok"}

# @app.post("/generate")
# def generate(input: dict):
#     # Add logic to process input and generate output
#     output = f"Processed: {input['input']}"
#     return {"output": output}

# @app.get("/models")
# def list_models():
#     # Example model list
#     models = ["model1", "model2", "model3"]
#     return {"models": models}

# @app.post("/load_model")
# def load_model(model_name: str):
#     # Logic to load a model
#     return {"status": "loaded", "model_name": model_name}

# @app.delete("/unload_model")
# def unload_model(model_name: str):
#     # Logic to unload a model
#     return {"status": "unloaded", "model_name": model_name}
