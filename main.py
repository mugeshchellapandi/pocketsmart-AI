from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html><head><title>PocketSmart AI</title></head>
    <body style="background:#6a11cb;color:white;text-align:center;padding:50px;font-family:sans-serif">
    <h1 style="font-size:40px">💰 PocketSmart AI WORKING DA! 🔥</h1>
    <h2>Budget Advisor</h2>
    <form action="/get-recommendation" method="post" style="background:white;padding:20px;border-radius:15px;max-width:400px;margin:auto">
        <input name="budget" placeholder="Budget ex: 50000" style="width:100%;padding:10px;margin:5px"><br>
        <input name="category" placeholder="Category ex: Mobile" style="width:100%;padding:10px;margin:5px"><br>
        <input name="need" placeholder="Need ex: Gaming" style="width:100%;padding:10px;margin:5px"><br>
        <button style="background:purple;color:white;padding:10px 20px;border:none;border-radius:10px;margin-top:10px">Get Best Options</button>
    </form>
    </body></html>
    """

@app.post("/get-recommendation", response_class=HTMLResponse)
def recommend(budget: str = Form(...), category: str = Form(...), need: str = Form(...)):
    return f"""
    <html><body style="background:#6a11cb;color:white;text-align:center;padding:50px;font-family:sans-serif">
    <h1>Best Option for You!</h1>
    <div style="background:white;color:black;padding:20px;border-radius:15px;max-width:400px;margin:auto">
    <h2>Budget: {budget}</h2>
    <h2>Category: {category}</h2>
    <h2>Need: {need}</h2>
    <h3>Recommended: POCO X6 Pro - Best for Gaming Under {budget}!</h3>
    <p>Reason: 8GB RAM, Dimensity 8300 - Super Gaming Performance!</p>
    <a href="/">Go Back</a>
    </div></body></html>
    """