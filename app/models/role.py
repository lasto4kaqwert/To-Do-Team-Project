from __future__ import annotations
from typing_extensions import TYPE_CHECKING

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.user import User

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(), nullable=False)

    users: Mapped[list["User"]] = relationship("User")
