from .components.navbar import navbar, navbar_reservas
from .components.filtro import calendar, search_docente, search_materia, grupo, hora
from .components.mapa import mapa_primer_nivel, mapa_segundo_nivel
from .components.inicio_sesion import inicion_sesion_desktop, inicion_sesion_mobile
from .components.matriz import horario_table_1, horario_table_2
from .components.botones import mis_reservaciones
from .components.consulta_reservaciones import tabla_horarios, lista_horarios
from .components.formulario_reserva import form_reservar
from .components.formulario_cambio import form_cambio
from .state import ConsultaHorarios, Login, AsignacionHorarios, FormCambio
import reflex as rx

def inicio_sesion_page() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            inicion_sesion_desktop()
        ),
        rx.mobile_only(
            inicion_sesion_mobile()
        )
    )

def reservacion_page() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            navbar(),
            # rx.button(
            #     f"ESTADO DISABLED: {AsignacionHorarios.select_horario}",
            #     disabled=AsignacionHorarios.select_horario
            # ),
            # FILTROS
            rx.box(
                # rx.hstack(
                #     #search_docente(),
                #     #search_materia(),
                #     justify="center",
                #     spacing="3"
                # ),
                rx.vstack(
                    rx.hstack(
                        calendar(),
                        hora(),
                        # grupo(),
                        justify="center",
                        spacing="3",
                        margin_top="10px",
                    ),
                    mis_reservaciones(),
                    align="center"
                ),
                margin_top="10px",
                padding="10px",
            ),

            # INFORMACION DE LAS RESERVACIONES DEL PISO 1
            rx.box(
                #tabla_horarios(),
                rx.hstack(
                    rx.box(
                        mapa_primer_nivel(),
                        position="sticky",
                        top="0",
                        width="100%"
                    ),
                    horario_table_1(),
                    #background="red",
                    spacing="0"
                ),
                #background="pink",
                margin_top="20px",
                # margin_left="20px",
                # margin_right="20px",
                # padding="20px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),

            # INFORMACION DE LAS RESERVACIONES DEL PISO 2
            rx.box(
                #tabla_horarios(),
                rx.hstack(
                    rx.box(
                        mapa_segundo_nivel(),
                        position="sticky",
                        top="0",
                        width="100%"
                    ),
                    horario_table_2(),
                    #background="red",
                    spacing="0"
                ),
                # background="#f2f3f7",
                margin_top="20px",
                # margin_left="20px",
                # margin_right="20px",
                # padding="20px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
        ),
        rx.mobile_and_tablet(
            navbar(),
            rx.box(
                rx.vstack(
                    #search_docente(),
                    #search_materia(),
                    rx.hstack(
                        calendar(),
                        hora(),
                        # grupo(),
                        spacing="3"
                    ),
                    mis_reservaciones(),
                    spacing="3",
                    align="center",
                ),
                # background="#f2f3f7",
                margin_top="10px",
                # margin_left="20px",
                # margin_right="20px",
                # padding="5px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
                #width="80%",
            ),
            rx.box(
                mapa_primer_nivel(),
                # background="#f2f3f7",
                margin_top="10px",
                # margin_left="10px",
                # margin_right="10px",
                # padding="10px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.box(
                horario_table_1(),
                # background="#f2f3f7",
                margin_top="10px",
                # margin_left="10px",
                # margin_right="10px",
                # padding="10px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.box(
                mapa_segundo_nivel(),
                # background="#f2f3f7",
                margin_top="10px",
                # margin_left="10px",
                # margin_right="10px",
                # padding="10px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
            rx.box(
                horario_table_2(),
                # background="#f2f3f7",
                margin_top="10px",
                # margin_left="10px",
                # margin_right="10px",
                # padding="10px",
                # border_radius="10px",
                # box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            ),
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
                rx.box(
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
    )

def mis_reservaciones_page() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            navbar_reservas(),
            rx.box(
                tabla_horarios(),
                width="100%",
                padding="20px"
            )
                #rx.redirect("/")
                
            # rx.box(
            #     # rx.hstack(
            #     #     #search_docente(),
            #     #     #search_materia(),
            #     #     justify="center",
            #     #     spacing="3"
            #     # ),
            #     rx.vstack(
            #         rx.hstack(
            #             calendar(),
            #             hora(),
            #             grupo(),
            #             justify="center",
            #             spacing="3",
            #             margin_top="10px",
            #         ),
            #         mis_reservaciones(),
            #         align="center"
            #     ),
            #     background="#f2f3f7",
            #     margin_top="10px",
            #     margin_left="20px",
            #     margin_right="20px",
            #     padding="5px",
            #     border_radius="10px",
            #     box_shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
            #     #width="80%", Modificacion pendiente
            # ),
        ),
        rx.mobile_only(
            navbar_reservas(),
            rx.box(
                lista_horarios(),
                width="100%",
                padding="20px"
            )
        )
    )

global_style = {
    "font_family": "Nunito Sans, sans-serif",
}

app = rx.App(
    theme=rx.theme(color_mode="light"),
    stylesheets=[
        'https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,opsz,wght@0,6..12,200..1000;1,6..12,200..1000&display=swap'
    ],
    style=global_style)
app.add_page(inicio_sesion_page, route="/")
app.add_page(reservacion_page, route="/horarios", on_load=Login.verificacion_login)#on_load=ConsultaHorarios.informacion_horarios)
app.add_page(mis_reservaciones_page, route="/horarios/reservaciones", on_load=Login.verificacion_login)
