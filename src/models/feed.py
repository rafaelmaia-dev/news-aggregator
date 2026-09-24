from datetime import datetime

from sqlalchemy import String, func

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Feed(Base):
    __tablename__ = "feeds"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(500))
    name: Mapped[str] = mapped_column(String(60))
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    articles: Mapped[list["Article"]] = relationship("Article", back_populates="feed")
    


