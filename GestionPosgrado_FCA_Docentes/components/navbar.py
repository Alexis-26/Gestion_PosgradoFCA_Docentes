import reflex as rx
from ..styles.colors import Colors
from ..styles.styles import FontSize
from ..styles.utils import Imagenes, Texto_Desktop, Texto_Mobile
from .botones import regresar_inicio, cerrar_sesion, cambio_password, mis_reservaciones_mobile

def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            # Elemento vacío para balancear el lado izquierdo
            #rx.box(width=["60px", "160px"]) ,
            
            # Título centrado con logo
            rx.hstack(
                rx.image(src=Imagenes.LOGO_UABC_FCA.value, width=["60px", "120px"]),
                rx.text("REGISTRO DE HORARIOS", 
                        font_size=[Texto_Mobile.SUBTITULOS.value, Texto_Desktop.TITULO_PRINCIPAL.value],
                        weight="bold", 
                        color=Colors.WHITE.value),
            ) ,
            
            # Botón en el lado derecho
            # rx.hstack(
            #     cambio_password(),
            #     cerrar_sesion(),
            # ),

            justify="center",
            align="center",
            width="100%",
            height="100%",
        ) ,
        width="100%",
        height=["50px", "100px"],
        background=Colors.PRIMARY_GREEN.value,
        padding_left=["10px", "60px"],
        padding_right=["10px", "60px"]
    )

def navbar_reservas() -> rx.Component:
    return rx.box(
        rx.flex(
            # Elemento vacío para balancear el lado izquierdo
            #regresar_inicio(),
            
            # Título centrado con logo
            rx.hstack(
                rx.image(src=Imagenes.LOGO_UABC_FCA.value, width=["60px", "120px"]) ,
                rx.text("MIS RESERVACIONES", 
                        font_size=[Texto_Mobile.SUBTITULOS.value, Texto_Desktop.TITULO_PRINCIPAL.value],
                        weight="bold", 
                        color=Colors.WHITE.value),
            ) ,
            
            # Botón en el lado derecho
            # rx.hstack(
            #     cambio_password(),
            #     cerrar_sesion(),
            # ),
            
            justify="center",
            align="center",
            width="100%",
            height="100%",
        ) ,
        width="100%",
        height=["50px", "100px"],
        background=Colors.PRIMARY_GREEN.value,
        padding_left=["10px", "60px"],
        padding_right=["10px", "60px"]
    )

def botones_navegacion_inicial_desktop() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.hstack(
                cambio_password(),
                cerrar_sesion()
            ),
            justify="end",
            align="center",
            width="100%",
            height="100%"
        ),
        width="100%",
        height=["50px", "60px"],
        #background=Colors.SECONDARY_GREEN.value,
        padding_left=["10px", "60px"],
        padding_right=["10px", "60px"]
    )

def botones_navegacion_misreservas_desktop() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.hstack(
                regresar_inicio()
            ),
            rx.hstack(
                cambio_password(),
                cerrar_sesion()
            ),
            justify="between",
            align="center",
            width="100%",
            height="100%"
        ),
        width="100%",
        height=["50px", "60px"],
        #background=Colors.SECONDARY_GREEN.value,
        padding_left=["10px", "60px"],
        padding_right=["10px", "60px"]
    )

def botones_navegacion_mobile():
    return rx.box(
        rx.flex(
            rx.hstack(
                regresar_inicio(),
                mis_reservaciones_mobile(),
                cambio_password(),
                cerrar_sesion(),
                width="100%",
                justify="between",
            ),
            align="center",
            width="100%",
            height="100%"
        ),
        width="100%",
        height=["60px", "60px"],
        background=Colors.PRIMARY_ORANGE.value,
        position="fixed",
        bottom="0",
        z_index="1000",
        padding_left="40px",
        padding_right="40px",
        #padding_bottom="10px"
    )