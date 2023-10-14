import json
import os
from flask_restx import Resource, Namespace, reqparse
from werkzeug.datastructures import FileStorage

from .api_model import image_model

img_store = [
    {
        "name": "snowflake.jpg",
        "type": "jpeg",
        "owner": "wikipedia.org"
    }
]

rest_api_ns = Namespace("api")

upload_api_parser = reqparse.RequestParser()
upload_api_parser.add_argument('imginfo', location='files', type=FileStorage, required=True)
upload_api_parser.add_argument('imgfile', location='files', type=FileStorage, required=True)


@rest_api_ns.route("/imgstore")
class ImageStore(Resource):

    @rest_api_ns.marshal_list_with(image_model)
    def get(self):
        return img_store


@rest_api_ns.route("/upload")
class Uploader(Resource):

    def get(self):
        return {"msg": "Please use POST to upload image files"}

    # @rest_api_ns.expect(upload_api_parser) did not work with RequestParser.
    # So, we need use doc decorator and parse the payload using parser
    @rest_api_ns.doc(parser=upload_api_parser)
    def post(self):
        args = upload_api_parser.parse_args()
        img_info = args['imginfo']
        img_file = args['imgfile']

        if img_info and img_file:
            img_meta = json.load(img_info)
            file_name = img_file.filename
            cached_file = os.path.join(os.getenv('UPLOAD_FOLDER'), file_name)
            print(f'image meta info: {img_meta}')
            print(f'uploaded file {file_name} will be saved at {cached_file}')

            img_file.save(cached_file)

            return {
                'msg': 'success',
                'status': 'file uploaded and cached',
            }
        else:
            return {
                'msg': 'failure',
                'status': 'file upload failure'
            }
