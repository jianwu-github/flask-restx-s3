from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

rest_api = Api(
    title="REST API to upload and annotate images with AWS S3 Buckets",
    doc="/swagger/"
)

db = SQLAlchemy()
