from sqlalchemy import ForeignKey, String, Text, func

from datetime import datetime

from src.database import Base

from sqlalchemy.orm import Mapped, mapped_column

class Articles(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(2048), unique=True)
    content_full: Mapped[str] = mapped_column(Text())
    summary: Mapped[str | None] = mapped_column(String(2000), nullable=True)
    feed_id: Mapped[int] = mapped_column(ForeignKey("feeds.id"))
    title: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    published_at: Mapped[datetime | None] = mapped_column(nullable=True)

