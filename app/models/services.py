from tortoise import fields, models


class Services(models.Model):
    id: int = fields.IntField(pk=True)
    name: str = fields.CharField(max_length=100, unique=True, index=True)
    url: str = fields.CharField(max_length=500, unique=True)
    country: str = fields.CharField(max_length=100, null=True, index=True)
    method: str = fields.CharField(max_length=25)
    header: dict = fields.JSONField(null=True)
    static_data: dict = fields.JSONField(null=True)
    dynamic_data: dict = fields.JSONField(null=True)

    def get_json_schema(self):
        return {
            'name': self.name,
            "url": self.url,
            "country": self.country,
            "method": self.method,
            "header": self.header,
            "static_data": self.static_data,
            "dynamic_data": self.dynamic_data
        }
