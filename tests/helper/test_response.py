from app.helper.response import JsonResponse, MetaResponse


def test_meta_response_default_value():
    response = MetaResponse()
    assert response.limit is None
    assert response.offset is None
    assert response.total_data == 0

def test_json_response():
    response = JsonResponse(data=None, message="success get all data", success=True, meta=None, status_code=200)
    assert response.data is None
    assert response.message == "success get all data"
    assert response.success == True
    assert response.meta is None
    assert response.status_code == 200
