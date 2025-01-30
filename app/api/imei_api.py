from flask import Blueprint, request, jsonify
from app.auth.token_auth import token_required
from app.imei.imei_service import check_imei

api = Blueprint('api', __name__)

@api.route('/api/check-imei', methods=['POST'])
@token_required
def check_imei_api():
    data = request.json
    imei = data.get('imei')
    imei_info = check_imei(imei)
    return jsonify(imei_info)
