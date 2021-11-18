from rest_flask.flask import ma
from rest_flask.models.user import Users

class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "birth_year")
        model = Users

post_schema = PostSchema()
posts_schema = PostSchema(many=True)