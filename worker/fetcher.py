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
            "descricao": entry.summary

        })

    return artigos