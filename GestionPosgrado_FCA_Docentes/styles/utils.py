from enum import Enum

class Texto(Enum):
    pass

class Imagenes(Enum):
    LOGO = "/escudo_uabc.png"
    LOGO_UABC_FCA = "/logo_uabc_fca.png"
    FONDO_INICIO_SESION = "/1000108766.png"

class Iconos(Enum):
    REGRESAR = "arrow-left"
    CERRAR_SESION = "power-off"
    CAMBIO_PASSWORD = "arrow-right-left"
    ELIMINAR = "trash-2"
    EDITAR = "pencil-line"