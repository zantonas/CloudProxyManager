import json


def get_gateway_conf():
    """
    Returns the gateway config.
    """
    with open('conf/gateway.json') as f:
        return json.load(f)


def load_swagger(app):
    """
    Loads the swagger ui.
    """
    from flask_swagger_ui import get_swaggerui_blueprint
    swagger_url = '/swagger'
    api_url = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        swagger_url,
        api_url,
        config={
            'app_name': "Cloud Proxy Gateway"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)

