from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select

from src.models.article import Article


async def article_exists(url: str, session: AsyncSession) -> bool:
    stmt = select(Article.id).where(Article.url == url)
    result = await session.execute(stmt)
    article = result.scalar_one_or_none()
    return article is not None

async def save_article(data: dict, feed_id: int, session: AsyncSession) -> Article:
    article = Article(**data, feed_id=feed_id)
    session.add(article)
    await session.commit()
    await session.refresh(article)
    return article