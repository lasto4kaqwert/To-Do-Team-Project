import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

from app.models.role import Role

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(), nullable=False)
    login: Mapped[str] = mapped_column(sa.String(), nullable=False)
    password: Mapped[str] = mapped_column(sa.String(), nullable=False)
    role_id: Mapped[int] = mapped_column(sa.ForeignKey("roles.id"), nullable=False)

    role: Mapped[Role] = relationship(Role)
