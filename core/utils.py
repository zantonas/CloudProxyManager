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
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Cloud Proxy Gateway"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

