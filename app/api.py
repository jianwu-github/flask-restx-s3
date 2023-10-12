from flask_restx import Resource, Namespace

rest_api_ns = Namespace("api")


@rest_api_ns.route("/upload")
class Uploader(Resource):

    def get(self):
        return {"message": "Please use POST to upload image files"}
