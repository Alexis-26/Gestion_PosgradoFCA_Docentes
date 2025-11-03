import reflex as rx
from ..styles.colors import Colors
from ..styles.styles import FontSize
from .botones import eliminar_reservacion, editar_reservacion
from ..state import Tabla_ConsultaHorarios

def get_status_badge(status: rx.Var[str]):
   return rx.badge(
        status,  # Convertir el Var a string
        variant="soft",
        size="2",
        color_scheme=rx.cond(
            status == "FIJO",
            "indigo",
            rx.cond(
                status == "RESERVADO", 
                "red",
                "gray"
            )
        )
    )

def get_color(status: rx.Var[str]):
    return rx.cond(
        status == "FIJO",
        Colors.BLACK.value,
        rx.cond(
            status=="RESERVADO",
            Colors.RED.value,
            "gray"
        )
    )

def get_btn_eliminar(status: rx.Var[str], dato):
    return rx.cond(
        status == "RESERVADO",
        eliminar_reservacion(dato[0], dato[4], dato[6])
    )

def show_row(dato):
    return rx.table.row(
        rx.table.cell(dato[0]),  # Salón
        #rx.table.cell(dato[1]),  # Docente
        rx.table.cell(dato[2]),  # Curso/Materia
        rx.table.cell(dato[3]),  # Grupo
        rx.table.cell(dato[4]),  # Fecha Inicio
        rx.table.cell(dato[5]),  # Fecha Fin
        rx.table.cell(dato[6]),  # Hora
        rx.table.cell(get_status_badge(dato[7])),  # Status
        rx.table.cell(
            get_btn_eliminar(dato[7], dato)
        )
    )

def tabla_horarios() -> rx.Component:
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Salón"),
                    #rx.table.column_header_cell("Docente"), #color=Colors.PRIMARY_GREEN.value),
                    rx.table.column_header_cell("Materia/Curso"),
                    rx.table.column_header_cell("Grupo"),
                    rx.table.column_header_cell("Fecha Inicial"),
                    rx.table.column_header_cell("Fecha Final"),
                    rx.table.column_header_cell("Hora"),
                    rx.table.column_header_cell("Status"),
                    rx.table.column_header_cell("Acción"),
                    color=Colors.WHITE.value,
                    background=Colors.PRIMARY_ORANGE.value,
                ),
            ),
            rx.table.body(
                rx.foreach(
                    Tabla_ConsultaHorarios.lista_horarios,
                    show_row
                )
            ),
            on_mount=Tabla_ConsultaHorarios.informacion_horarios,
            size="2",
            variant="surface",
        )
    )

def show_horarios(dato):
    return rx.popover.root(
            rx.popover.trigger(
                rx.button(
                    rx.hstack(
                        rx.text(dato[6]),
                        rx.text(dato[2]),
                        rx.text(dato[3]),
                        align="center"
                    ),
                    width="100%",
                    height="60px",
                    background=get_color(dato[7])
                )
            ),
            rx.popover.content(
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Información"
                        ),
                        rx.popover.close(
                            rx.button(rx.icon("x"), 
                                      size="1",
                                      background=Colors.PRIMARY_ORANGE.value
                                      ),
                        ),
                        width="100%",
                        justify="between"
                    ),
                    rx.card(
                        rx.data_list.root(
                            rx.data_list.item(
                                rx.data_list.label("Salon"),
                                rx.data_list.value(dato[0]),
                            ),
                            # rx.data_list.item(
                            #     rx.data_list.label("Docente"),
                            #     rx.data_list.value(rx.text(
                            #         dato[1],
                            #         # Controlar el ancho máximo
                            #         max_width="120px",
                            #         # Preservar el formato
                            #         white_space="pre-wrap",
                            #         # Permitir el wrap del texto
                            #         overflow_wrap="break-word"
                            #         )
                            #     ),
                            # ),
                            rx.data_list.item(
                                rx.data_list.label("Materia/Curso"),
                                rx.data_list.value(rx.text(
                                    dato[2],
                                    # Controlar el ancho máximo
                                    max_width="120px",
                                    # Preservar el formato
                                    white_space="pre-wrap",
                                    # Permitir el wrap del texto
                                    overflow_wrap="break-word"
                                    )
                                ),
                            ),
                            rx.data_list.item(
                                rx.data_list.label("Grupo"),
                                rx.data_list.value(dato[3]),
                                align="center",
                            ),
                            rx.data_list.item(
                                rx.data_list.label("Fecha Inicial"),
                                rx.data_list.value(dato[4]),
                                align="center",
                            ),
                            rx.data_list.item(
                                rx.data_list.label("Fecha Final"),
                                rx.data_list.value(dato[5]),
                                align="center",
                            ),
                            rx.data_list.item(
                                rx.data_list.label("Hora"),
                                rx.data_list.value(dato[6]),
                                align="center",
                            ),
                            rx.data_list.item(
                                rx.data_list.label("Status"),
                                rx.data_list.value(get_status_badge(dato[7])),
                                align="center",
                            ),
                            rx.data_list.item(
                                rx.data_list.label("Acción"),
                                rx.data_list.value(
                                    get_btn_eliminar(dato[7], dato)
                                ),
                                align="center",
                            ),
                        ),
                        size="1",
                        width="100%"
                    ),
                ),
                size="1"
            )
        )

def lista_horarios() -> rx.Component:
    return rx.vstack(
        rx.foreach(
            Tabla_ConsultaHorarios.lista_horarios,
            show_horarios
        ),
    )