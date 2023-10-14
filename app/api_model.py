from flask_restx import fields

from .extensions import rest_api

image_model = rest_api.model("Image", {
    "name": fields.String,
    "type": fields.String,
    "owner": fields.String,
})