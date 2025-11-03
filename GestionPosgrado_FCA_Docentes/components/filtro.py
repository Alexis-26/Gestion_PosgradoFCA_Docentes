import reflex as rx
from ..styles.colors import Colors
from ..state import ConsultaHorarios, AsignacionHorarios

def calendar() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.vstack(
                rx.text("Filtro de fecha", size="4"),
                rx.input(
                    min=AsignacionHorarios.min_date,
                    default_value=ConsultaHorarios.fecha_hoy,
                    name="filtro_fecha",
                    type="date",
                    color_scheme="green",
                    size="3",
                    on_change=ConsultaHorarios.filter_fecha
                ),
                spacing="0"
            )
        ),
        rx.mobile_only(
            rx.vstack(
                rx.text("Filtro de fecha", size="2"),
                rx.input(
                    min=AsignacionHorarios.min_date,
                    default_value=ConsultaHorarios.fecha_hoy,
                    name="filtro_fecha",
                    type="date",
                    color_scheme="green",
                    size="1",
                    on_change=ConsultaHorarios.filter_fecha
                ),
                spacing="0"
            )
        ),
    )

# NO ESTÁ IMPLEMENTADO
def grupo() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.select(
                ConsultaHorarios.grupos,
                placeholder="Grupo",
                size="3",
                width="150px",
                on_change=ConsultaHorarios.filter_grupo,
            )
        ),
        rx.mobile_only(
            rx.select(
                ConsultaHorarios.grupos,
                placeholder="Grupo",
                size="1",
                width="80px",
                on_change=ConsultaHorarios.filter_grupo,
            )
        )
    )

def hora() -> rx.Component:
    hora = ConsultaHorarios.hora_actual
    return rx.box(
        rx.tablet_and_desktop(
            rx.vstack(
                rx.text("Filtro de hora", size="4"),
                rx.select(
                    ConsultaHorarios.horas,
                    default_value=hora,
                    placeholder="Hora",
                    name="filtro_hora",
                    position="popper",
                    color_scheme="green",
                    size="3",
                    width="150px",
                    on_change=ConsultaHorarios.filter_hora,
                    #on_mount=Tabla_ConsultaHorarios.informacion_horarios
                ),
                spacing="0"
            )
        ),
        rx.mobile_only(
            rx.vstack(
                rx.text("Filtro de hora", size="2"),
                rx.select(
                    ConsultaHorarios.horas,
                    default_value=hora,
                    placeholder="Hora",
                    name="filtro_hora",
                    color_scheme="green",
                    position="popper",
                    size="1",
                    width="80px",
                    on_change=ConsultaHorarios.filter_hora,
                    #on_mount=Tabla_ConsultaHorarios.informacion_horarios
                ),
                spacing="0"
            )
        )
    )

# NO ESTÁ IMPLEMENTADO
def search_docente() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.hstack(
                rx.input(
                    placeholder="Buscar Docente",
                    size="3",
                    width="100%"
                ),
                rx.button(
                    rx.icon("search"),
                    size="3",
                    background=Colors.PRIMARY_ORANGE.value
                ),
                spacing="1",
                #background="blue",
            ),
        ),
        rx.mobile_only(
            rx.hstack(
                rx.input(
                    placeholder="Buscar Docente",
                    size="1",
                    width="100%"
                ),
                rx.button(
                    rx.icon("search", size=20),
                    size="1",
                    background=Colors.PRIMARY_ORANGE.value
                ),
                spacing="1",
                #background="blue",
            ),
        ),
        width=["80%", "30%"]
    )

# NO ESTÁ IMPLEMENTADO
def search_materia() -> rx.Component:
    return rx.box(
        rx.tablet_and_desktop(
            rx.hstack(
                rx.input(
                    placeholder="Buscar Materia",
                    size="3",
                    width="100%",
                ),
                rx.button(
                    rx.icon("search"),
                    size="3",
                    background=Colors.PRIMARY_ORANGE.value
                ),
                spacing="1",
                #background="blue",
            ),
        ),
        rx.mobile_only(
            rx.hstack(
                rx.input(
                    placeholder="Buscar Materia",
                    size="1",
                    width="100%"
                ),
                rx.button(
                    rx.icon("search", size=20),
                    size="1",
                    background=Colors.PRIMARY_ORANGE.value
                ),
                spacing="1",
                #background="blue",
            ),
        ),
        width=["80%", "30%"]
    )