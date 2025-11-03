from enum import Enum

class Texto_Desktop(Enum):
    TITULO_PRINCIPAL = "3rem"
    SUBTITULOS = "2rem"
    SECCIONES = "1.5rem"
    TEXTO_NORMAL = "1.125rem"
    TEXTO_CHICO = "1rem"

class Texto_Mobile(Enum):
    TITULO_PRINCIPAL = "1.5rem"
    SUBTITULOS = "1.25rem"
    SECCIONES = "1.125rem"
    TEXTO_NORMAL = "1rem"
    TEXTO_CHICO = "0.875rem"
    TEXTO_EXTRA_CHICO = "0.75rem"

class Imagenes(Enum):
    LOGO = "/escudo_uabc.png"
    LOGO_UABC_FCA = "/logo_uabc_fca.png"
    FONDO_INICIO_SESION = "/1000108766.png"

class Iconos(Enum):
    REGRESAR = "house"
    CERRAR_SESION = "power"
    CAMBIO_PASSWORD = "arrow-right-left"
    ELIMINAR = "trash-2"
    MISRESERVACIONES = "calendar-search"