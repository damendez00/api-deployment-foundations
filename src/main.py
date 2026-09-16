from fastapi import FastAPI, HTTPException, Request

app = FastAPI(title="Support Triage Helper")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/triage-ticket")
async def triage_ticket(request: Request):
    body = await request.json()
    ticket_text = str(body.get("ticket_text", "")).strip()

    if not ticket_text:
        raise HTTPException(
            status_code=400,
            detail="ticket_text is required"
        )

    lower_text = ticket_text.lower()

    if "damaged" in lower_text:
        category = "damaged_item"
    elif "refund" in lower_text:
        category = "refund_request"
    else:
        category = "general_request"

    return {
        "category": category,
        "summary": ticket_text[:140]
    }