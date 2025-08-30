import reflex as rx
import os

config = rx.Config(
    app_name="GestionPosgrado_FCA_Docentes",
    # EL PORT DEBE DE SER EL MISMO QUE LA API PUBLICA
    # Railway te pasa un puerto dinámico en la variable PORT
    backend_port=int(os.environ.get("PORT", 8000)),

    # URL de la base de datos (en Railway la defines en variables)
    db_url=os.getenv("DB_URL", "mysql+pymysql://root:password@localhost:3306/Gestion_PosgradoDB"), # NECESARIO ACTIVAR ANTES DE SUBIR A HOST

    # URL del backend (para API)
    # ESTO DEBE APUNTAR A RAILWAY CUANDO SE EXPORTE EL FRONTED
    api_url=os.getenv("API_URL", "https://gestionposgradofcadocentes-production.up.railway.app"), # NECESARIO ACTIVAR ANTES DE SUBIR A HOST

    # Esto no se sabe si realmente funciona (PROBAR)
    # # Permitir que el frontend en Vercel se conecte vía WebSocket
    allowed_hosts=[
        "gestion-posgrado-fca-docentes.vercel.app" # NECESARIO ACTIVAR ANTES DE SUBIR A HOST
    ],
    show_built_with_reflex=0

    # Descomentar unicamente esta linea para local
    #db_url="mysql+pymysql://root:GWqLlujpGEFqvQnhLspoIldtXyFDlZxm@autorack.proxy.rlwy.net:31857/Gestion_PosgradoDB"
)