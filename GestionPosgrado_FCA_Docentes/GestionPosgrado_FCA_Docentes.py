from .components.navbar import navbar, navbar_reservas, botones_navegacion_inicial_desktop, botones_navegacion_misreservas_desktop, botones_navegacion_mobile
from .components.filtro import calendar, hora
from .components.mapa import mapa_primer_nivel, mapa_segundo_nivel
from .components.inicio_sesion import inicion_sesion_desktop, inicion_sesion_mobile
from .components.matriz import horario_table_1, horario_table_2
from .components.botones import mis_reservaciones
from .components.consulta_reservaciones import tabla_horarios, lista_horarios
from .components.formulario_reserva import form_reservar
from .components.formulario_cambio import form_cambio
from .styles.utils import Texto_Desktop, Texto_Mobile
from .state import ConsultaHorarios, InicioSesion, AsignacionHorarios, FormCambio
import reflex as rx

def inicio_sesion_page() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            inicion_sesion_desktop()
        ),
        rx.mobile_and_tablet(
            inicion_sesion_mobile()
        )
    )

def reservacion_page() -> rx.Component:
    return rx.cond(
        InicioSesion.is_authenticated,
        rx.box(
            rx.desktop_only(
                navbar(),

                # FILTROS
                botones_navegacion_inicial_desktop(),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text("Fecha del dia de hoy:", font_size=Texto_Desktop.SECCIONES.value, weight="bold"),
                            rx.text(rx.moment(ConsultaHorarios.fecha_hoy, format="DD-MM-YYYY"), font_size=Texto_Desktop.SECCIONES.value),
                        ),
                        rx.vstack(
                            rx.hstack(
                                calendar(),
                                hora(),
                                justify="center",
                                align="center",
                                spacing="3",
                                margin_top="10px",
                            ),
                            align="center",
                            spacing="0"
                        ),
                        mis_reservaciones(),
                        align="center",
                        spacing="2"
                    ),
                    padding="10px",
                    position="sticky",
                    top="0",
                    z_index="999",
                    background="#ffffff",
                    box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
                ),

                # INFORMACION DE LAS RESERVACIONES DEL PISO 1
                rx.box(
                    mapa_primer_nivel(),
                    margin_top="20px",
                ),
                rx.flex(
                    horario_table_1(),
                    margin_top="20px",
                    justify="center",
                    width="100%",
                    padding="40px"
                ),

                # INFORMACION DE LAS RESERVACIONES DEL PISO 2
                rx.box(
                    mapa_segundo_nivel(),
                    margin_top="20px",
                ),
                rx.flex(
                    horario_table_2(),
                    margin_top="20px",
                    justify="center",
                    width="100%",
                    padding="40px"
                ),
            ),
            rx.mobile_and_tablet(
                navbar(),
                botones_navegacion_mobile(),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text("Fecha del dia de hoy:", font_size=Texto_Mobile.SUBTITULOS.value, weight="bold"),
                            rx.text(rx.moment(ConsultaHorarios.fecha_hoy, format="DD-MM-YYYY"), font_size=Texto_Mobile.SUBTITULOS.value),
                        ),
                        rx.vstack(
                            rx.hstack(
                                calendar(),
                                hora(),
                                spacing="3"
                            ),
                            spacing="2",
                            align="center",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    padding="10px",
                    position="sticky",
                    top="0",
                    z_index="999",
                    background="#ffffff",
                    box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
                ),

                rx.box(
                    mapa_primer_nivel(),
                    margin_top="10px",
                ),
                rx.flex(
                    horario_table_1(),
                    margin_top="10px",
                    padding="5px",
                    justify="center",
                    width="100%",
                ),
                rx.box(
                    mapa_segundo_nivel(),
                    margin_top="10px",
                ),
                rx.flex(
                    horario_table_2(),
                    margin_top="10px",
                    padding="5px",
                    justify="center",
                    width="100%",
                ),
                padding_bottom="60px"
            ),
            rx.dialog.root(
                rx.dialog.content(
                    rx.dialog.title(
                        "Formulario de Reservación",
                        display="none"
                    ),
                    rx.dialog.description(
                        "Formulario para reservar un salón",
                        display="none"
                    ),
                    rx.flex(
                        form_reservar(),
                        width="100%",
                    ),
                    style={
                        "background": "transparent",
                        "box_shadow": "none",
                        "max_width": "900px",
                        "width": "100%",
                    },
                ),
                open=AsignacionHorarios.mostrar_formulario,
            ),
            rx.dialog.root(
                rx.dialog.content(
                    rx.dialog.title(
                        "Formulario de Cambio de Contraseña",
                        display="none"
                    ),
                    rx.dialog.description(
                        "Formulario para Cambiar la Contraseña",
                        display="none"
                    ),
                    rx.box(
                        form_cambio(),
                        width="100%",
                    ),
                    style={
                        "background": "transparent",
                        "box_shadow": "none",
                        "max_width": "900px",
                        "width": "100%",
                    },
                ),
                open=FormCambio.mostrar_formulario,
            ),
            background_color="#FFFFFF",
            width="100%",
            min_height="100vh",
            margin="0px",
            padding="0px",
            on_mount=AsignacionHorarios.carga_informacion_form
        ),
        proteccion()
    )

def mis_reservaciones_page() -> rx.Component:
    return rx.cond(
        InicioSesion.is_authenticated,
        rx.box(
            rx.desktop_only(
                navbar_reservas(),
                botones_navegacion_misreservas_desktop(),
                rx.box(
                    tabla_horarios(),
                    width="100%",
                    padding="20px"
                )
            ),
            rx.mobile_and_tablet(
                navbar_reservas(),
                botones_navegacion_mobile(),
                rx.box(
                    lista_horarios(),
                    width="100%",
                    padding="20px"
                )
            ),
            rx.dialog.root(
                rx.dialog.content(
                    rx.dialog.title(
                        "Formulario de Cambio de Contraseña",
                        display="none"
                    ),
                    rx.dialog.description(
                        "Formulario para Cambiar la Contraseña",
                        display="none"
                    ),
                    rx.box(
                        form_cambio(),
                        width="100%",
                    ),
                    style={
                        "background": "transparent",
                        "box_shadow": "none",
                        "max_width": "900px",
                        "width": "100%",
                    },
                ),
                open=FormCambio.mostrar_formulario,
            ),
        ),
        proteccion()
    )

def proteccion() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("No tienes acceso.", font_size="3em"),
            rx.text("Si esto es un error contacta al administrador."),
            spacing="4",
            padding="2em",
            border_radius="10px",
            box_shadow="lg",
        ),
        height="100vh",
    )

global_style = {
    "font_family": "Nunito Sans, sans-serif",
    "button": {
        "cursor": "pointer",
    },
}

app = rx.App(
    theme=rx.theme(color_mode="light"),
    stylesheets=[
        'https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,opsz,wght@0,6..12,200..1000;1,6..12,200..1000&display=swap'
    ],
    style=global_style)
app.add_page(inicio_sesion_page, route="/", title="Iniciar sesión")
app.add_page(reservacion_page, route="/horarios", on_load=InicioSesion.verificacion_login, title="Horarios")
app.add_page(mis_reservaciones_page, route="/horarios/reservaciones", on_load=InicioSesion.verificacion_login, title="Reservaciones")
