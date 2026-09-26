from sqlalchemy.ext.asyncio import AsyncSession

from src.models.article import Article


async def save_article(data: dict, feed_id: int, session: AsyncSession) -> Article:
    article = Article(**data, feed_id=feed_id)
    session.add(article)
    await session.commit()
    await session.refresh(article)
    return article