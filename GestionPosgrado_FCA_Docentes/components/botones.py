from ..styles.colors import Colors
from ..styles.styles import FontSize
from ..styles.utils import Iconos
from ..state import Tabla_ConsultaHorarios, InicioSesion, FormCambio
import reflex as rx

def regresar_inicio():
    return rx.tooltip(
        rx.button(
            rx.icon(
                tag=Iconos.REGRESAR.value,
                class_name="w-[30px] h-[30px] md:w-[30px] md:h-[30px]",
                color=Colors.BLACK.value,
            ),
            variant="solid",
            width=["35px", "45px"],
            height=["35px", "45px"],
            background=Colors.WHITE.value,
            radius="full",
            on_click=rx.redirect("/horarios")
        ),
        content="Regresar al inicio",
        placement="top",
        has_arrow=True,
    )

def mis_reservaciones():
    return rx.button(
        rx.text("Mis Reservaciones", 
                color=Colors.BLACK.value, 
                font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value],
                weight="bold"
                ),
        variant="solid",
        background=Colors.SECONDARY_ORANGE.value,
        radius="medium",
        width=["160px", "260px"],
        height=["20px", "40px"],
        on_click=rx.redirect("/horarios/reservaciones")
    )

def mis_reservaciones_mobile():
    return rx.tooltip(
        rx.button(
            rx.icon(tag=Iconos.MISRESERVACIONES.value, 
                    class_name="w-[30px] h-[30px] md:w-[30px] md:h-[30px]",
                    color=Colors.BLACK.value
                    ),
            variant="solid",
            width=["35px", "45px"],
            height=["35px", "45px"],
            background=Colors.WHITE.value,
            radius="full",
            on_click=rx.redirect("/horarios/reservaciones")
        ),
        content="Mis reservaciones",
        placement="top",
        has_arrow=True,
    )


def cerrar_sesion():
    return rx.tooltip(
        rx.button(
            rx.icon(tag=Iconos.CERRAR_SESION.value, 
                    class_name="w-[30px] h-[30px] md:w-[30px] md:h-[30px]", 
                    color=Colors.BLACK.value
                    ),
            variant="solid",
            width=["35px", "45px"],
            height=["35px", "45px"],
            background=Colors.WHITE.value,
            radius="full",
            on_click=[InicioSesion.cerrar_sesion, Tabla_ConsultaHorarios.informacion_horarios]
        ),
        content="Cerrar sesión",
        placement="top",
        has_arrow=True,
    )

def cambio_password():
    return rx.tooltip(
        rx.button(
            rx.icon(tag=Iconos.CAMBIO_PASSWORD.value, 
                    class_name="w-[30px] h-[30px] md:w-[30px] md:h-[30px]", 
                    color=Colors.BLACK.value
                    ),
            variant="solid",
            width=["35px", "45px"],
            height=["35px", "45px"],
            background=Colors.WHITE.value,
            radius="full",
            on_click=FormCambio.abrir_form
        ),
        content="Cambiar contraseña",
        placement="top",
        has_arrow=True,
    )

def eliminar_reservacion(salon:str, fecha:str, hora:str):
    return rx.tooltip(
        rx.button(
            rx.icon(
                tag=Iconos.ELIMINAR.value,
                color=Colors.WHITE.value
            ),
            background=Colors.RED.value,
            on_click=Tabla_ConsultaHorarios.eliminar_reserva(salon, fecha, hora)
        ),
        content="Eliminar reservación",
        placement="top",
        has_arrow=True,
    )

def editar_reservacion():
    return rx.button(
        rx.icon(
            tag=Iconos.EDITAR.value,
            color=Colors.WHITE.value
        ),
        background=Colors.SECONDARY_GREEN.value
    )