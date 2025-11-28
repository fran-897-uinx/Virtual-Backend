from waitress import serve
from backend_pro.wsgi import application # Assuming 'app' is your WSGI callable

serve(application, host='0.0.0.0', port=8050)
