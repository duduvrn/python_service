#!/usr/bin/env python3
"""A simple command-line interface to fetch weather information using wttr.in.
"""
from fastapi import FastAPI
import uvicorn
import httpx

app = FastAPI()


@app.get("/")
async def read_root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Welcome to the Weather API!"}


@app.get("/weather/{location}")
async def get_weather(location: str):
    """Fetch weather information for a given location using wttr.in."""
    url = f"https://wttr.in/{location}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return {"location": location, "weather": response.text}
        return {"error": "Could not fetch weather information"}, 500

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
