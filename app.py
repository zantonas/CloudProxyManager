"""
Run app
"""

if __name__ == '__main__':
    from cloudproxymanager.views import app
    app.run(host='127.0.0.2', port=5000)
