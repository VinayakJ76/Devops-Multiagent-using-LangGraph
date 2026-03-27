from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

from graph.graph_builder import build_graph
from knowledge.loaders import load_pdf, load_url
from knowledge.ingest import ingest_documents

app = FastAPI()
graph = build_graph()

class Query(BaseModel):
    query: str

@app.post("/ask")
async def ask(q: Query):
    result = graph.invoke({
        "query": q.query,
        "agent_type": "",
        "context": "",
        "reasoning": "",
        "plan": [],
        "result": ""
    })
    return result


@app.post("/upload/pdf")
async def upload_pdf(file: UploadFile):

    path = f"/tmp/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    docs = load_pdf(path)
    return {"status": ingest_documents(docs)}


class URLReq(BaseModel):
    url: str

@app.post("/upload/url")
async def upload_url(req: URLReq):

    docs = load_url(req.url)
    return {"status": ingest_documents(docs)}

@app.get("/health")
def health():
    return {"status": "ok"}