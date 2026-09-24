from datetime import datetime

from sqlalchemy import ForeignKey, func

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Delivery(Base):
    __tablename__ = "deliveries"

    id: Mapped[int] = mapped_column(primary_key=True)
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"))
    telegram_message_id: Mapped[int | None] = mapped_column(unique=True, nullable=True)
    success: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    article: Mapped["Article"] = relationship("Article", back_populates="delivery")