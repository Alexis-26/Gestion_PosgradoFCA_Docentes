from enum import Enum

class Texto_Desktop(Enum):
    TITULO_PRINCIPAL = "3rem"
    SUBTITULOS = "2rem"
    SECCIONES = "1.5rem"
    TEXTO_NORMAL = "1.125rem"
    TEXTO_CHICO = "1rem"

class Texto_Mobile(Enum):
    TITULO_PRINCIPAL = "1.5rem"   # ~24px
    SUBTITULOS = "1.25rem"       # ~20px
    SECCIONES = "1.125rem"       # ~18px
    TEXTO_NORMAL = "1rem"        # ~16px (ideal para lectura)
    TEXTO_CHICO = "0.875rem"     # ~14px
    TEXTO_EXTRA_CHICO = "0.75rem" # ~12px (etiquetas, notas)

class Imagenes(Enum):
    LOGO = "/escudo_uabc.png"
    LOGO_UABC_FCA = "/logo_uabc_fca.png"
    FONDO_INICIO_SESION = "/1000108766.png"

class Iconos(Enum):
    REGRESAR = "house"
    CERRAR_SESION = "power-off"
    CAMBIO_PASSWORD = "arrow-right-left"
    ELIMINAR = "trash-2"
    MISRESERVACIONES = "calendar-search"