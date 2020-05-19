from tortoise import fields, models
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(models.Model):
    id: int = fields.IntField(pk=True)
    user_name: str = fields.CharField(max_length=100, unique=True, index=True)
    hashed_password: str = fields.CharField(max_length=200, unique=True)
    creator: bool = fields.BooleanField(default=False)

    def user_verification(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.hashed_password)
