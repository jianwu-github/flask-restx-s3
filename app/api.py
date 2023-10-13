import os
from flask_restx import Resource, Namespace, reqparse
from werkzeug.datastructures import FileStorage

rest_api_ns = Namespace("api")


@rest_api_ns.route("/upload")
class Uploader(Resource):

    def get(self):
        return {"msg": "Please use POST to upload image files"}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', location='files', type=FileStorage, required=True)

        args = parser.parse_args()
        file = args['file']

        if file:
            file_name = file.filename
            cached_file = os.path.join(os.getenv('UPLOAD_FOLDER'), file_name)
            print(f'uploaded file {file_name} will be saved at {cached_file}')

            file.save(cached_file)

            return {
                'msg': 'success',
                'status': 'file uploaded and cached',
            }
        else:
            return {
                'msg': 'failure',
                'status': 'file upload failure'
            }