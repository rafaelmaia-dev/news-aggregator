from datetime import datetime

import feedparser

import httpx

async def fetch_feed(url: str) -> list[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    feed = feedparser.parse(response.text)

    artigos = []
    
    for entry in feed.entries:
        artigos.append({
            "titulo": entry.title,
            "url": entry.link,
            "content_full": entry.summary,
            "published_at": datetime(*entry.published_parsed[:6]) if 
        entry.published_parsed else None,

        })

    return artigos