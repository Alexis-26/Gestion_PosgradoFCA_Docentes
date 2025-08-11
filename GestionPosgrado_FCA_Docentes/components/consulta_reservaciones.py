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
            rx.hstack(
                eliminar_reservacion(dato[0], dato[4], dato[6]),
                #editar_reservacion()
            )
        )
        #rx.table.cell(rx.button("Ubicacion"))
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
            #width="100%",
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
                        rx.text(dato[3])
                    ),
                    width="100%",
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
                                    rx.hstack(
                                        eliminar_reservacion(dato[0], dato[4], dato[6]),
                                        #editar_reservacion()
                                    )
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

# def mapa_primer_nivel():
#     return rx.container(
#         rx.vstack(
#             rx.text("Primer Nivel (Primer Piso)", font_size=[FontSize.SMALL.value, FontSize.LARGE.value]),
#             rx.hstack(
#                 rx.popover.root(
#                     rx.popover.trigger(
#                         rx.button(
#                             rx.vstack(
#                                 rx.text("101", font_size=["9px", FontSize.SMALL.value]),
#                                 rx.text("Juan Rosas", 
#                                     font_size=["9px", FontSize.SMALL.value],
#                                     max_width=["70px", "150px"],
#                                     white_space="pre-wrap",
#                                     overflow_wrap="break-word"
#                                 ),
#                                 spacing="0",
#                                 align="center",
#                             ),
#                             width=["70px", "150px"],
#                             height=["50px", "80px"]
#                         )
#                     ),
#                     rx.popover.content(
#                         rx.flex(
#                             rx.text("Tu contenido aquí"),
#                             rx.popover.close(
#                                 rx.button("Cerrar")
#                             ),
#                             direction="column",
#                             spacing="3"
#                         )
#                     )
#                 ),
#                 rx.spacer(),
#                 rx.popover.root(
#                     rx.popover.trigger(
#                         rx.button(
#                             rx.vstack(
#                                 rx.text("103", font_size=["9px", FontSize.SMALL.value]),
#                                 rx.text("Juan Rosas", 
#                                     font_size=["9px", FontSize.SMALL.value],
#                                     max_width=["70px", "150px"],
#                                     white_space="pre-wrap",
#                                     overflow_wrap="break-word"
#                                 ),
#                                 spacing="0",
#                                 align="center",
#                             ),
#                             width=["70px", "150px"],
#                             height=["50px", "80px"]
#                         )
#                     ),
#                     rx.popover.content(
#                         rx.flex(
#                             rx.text("Tu contenido aquí"),
#                             rx.popover.close(
#                                 rx.button("Cerrar")
#                             ),
#                             direction="column",
#                             spacing="3"
#                         )
#                     )
#                 ),
#                 background="red",
#                 width=["95%", "80%"],
#                 justify="between"
#             ),
#             rx.hstack(
#                 rx.popover.root(
#                     rx.popover.trigger(
#                         rx.button(
#                             rx.vstack(
#                                 rx.text("102", font_size=["9px", FontSize.SMALL.value]),
#                                 rx.text("Juan Rosas", 
#                                     font_size=["9px", FontSize.SMALL.value],
#                                     max_width=["70px", "150px"],
#                                     white_space="pre-wrap",
#                                     overflow_wrap="break-word"
#                                 ),
#                                 spacing="0",
#                                 align="center",
#                             ),
#                             width=["70px", "150px"],
#                             height=["50px", "80px"]
#                         )
#                     ),
#                     rx.popover.content(
#                         rx.flex(
#                             rx.text("Tu contenido aquí"),
#                             rx.popover.close(
#                                 rx.button("Cerrar")
#                             ),
#                             direction="column",
#                             spacing="3"
#                         )
#                     )
#                 ),
#                 rx.flex(
#                     rx.popover.root(
#                         rx.popover.trigger(
#                             rx.button(
#                                 rx.vstack(
#                                     rx.text("A", font_size=["9px", FontSize.SMALL.value]),
#                                     rx.text("Juan Rosas", 
#                                         font_size=["9px", FontSize.SMALL.value],
#                                         max_width=["70px", "150px"],
#                                         white_space="pre-wrap",
#                                         overflow_wrap="break-word"
#                                     ),
#                                     spacing="0",
#                                     align="center"
#                                 ),
#                                 width=["60px", "150px"],
#                                 height=["100px", "200px"],
#                                 border_bottom_left_radius=["100px", "200px"]
#                             )
#                         ),
#                         rx.popover.content(
#                             rx.flex(
#                                 rx.text("Contenido del popover aquí"),
#                                 rx.popover.close(
#                                     rx.button("Cerrar")
#                                 ),
#                                 direction="column",
#                                 spacing="3"
#                             )
#                         )
#                     ),
#                     rx.popover.root(
#                         rx.popover.trigger(
#                             rx.button(
#                                 rx.vstack(
#                                     rx.text("B", font_size=["9px", FontSize.SMALL.value]),
#                                     rx.text("Juan Rosas", 
#                                         font_size=["9px", FontSize.SMALL.value],
#                                         max_width=["70px", "150px"],
#                                         white_space="pre-wrap",
#                                         overflow_wrap="break-word"
#                                     ),
#                                     spacing="0",
#                                     align="center"
#                                 ),
#                                 width=["60px", "150px"],
#                                 height=["100px", "200px"],
#                                 border_bottom_right_radius=["100px", "200px"]
#                             )
#                         ),
#                         rx.popover.content(
#                             rx.flex(
#                                 rx.text("Contenido del popover aquí"),
#                                 rx.popover.close(
#                                     rx.button("Cerrar")
#                                 ),
#                                 direction="column",
#                                 spacing="3"
#                             )
#                         )
#                     ),
#                     spacing="2"
#                 ),
#                 rx.popover.root(
#                     rx.popover.trigger(
#                         rx.button(
#                             rx.vstack(
#                                 rx.text("104", font_size=["9px", FontSize.SMALL.value]),
#                                 rx.text("Juan Rosas", 
#                                     font_size=["9px", FontSize.SMALL.value],
#                                     max_width=["70px", "150px"],
#                                     white_space="pre-wrap",
#                                     overflow_wrap="break-word"
#                                 ),
#                                 spacing="0",
#                                 align="center",
#                             ),
#                             width=["70px", "150px"],
#                             height=["50px", "80px"]
#                         )
#                     ),
#                     rx.popover.content(
#                         rx.flex(
#                             rx.text("Tu contenido aquí"),
#                             rx.popover.close(
#                                 rx.button("Cerrar")
#                             ),
#                             direction="column",
#                             spacing="3"
#                         )
#                     )
#                 ),
#                 # background="red",
#                 width=["95%", "80%"],
#                 justify="between"
#             ),
#             #background=Colors.PRIMARY_GREEN.value,
#             align="center",
#         ),
#         #size="4",
#         center_content=True,
#         background=Colors.PRIMARY_GREEN.value,
#         padding="0px"
#     )

# class State(rx.State):
#     # Lista para los salones del primer nivel
#     salon_info: list[tuple] = [
#         ('101', 'RICARDO OSORIO', 'PLANEACIÓN FISCAL', '951'),
#         ('102', 'JUAN PEREZ', 'MATEMÁTICAS', '952'),
#         ('103', 'MARIA LOPEZ', 'ESTADÍSTICA', '953'),
#         ('104', 'PEDRO RAMIREZ', 'CÁLCULO', '954'),
#         ('A', 'ANA GARCIA', 'FÍSICA', '955'),
#         ('B', 'CARLOS RUIZ', 'QUÍMICA', '956')
#     ]

def mapa_primer_nivel():
    return rx.container(
        rx.vstack(
            rx.text("Primer Nivel (Primer Piso)", 
                   font_size=[FontSize.SMALL.value, FontSize.LARGE.value]),
            # Primera fila (101 y 103)
            rx.hstack(
                # Salón 101
                rx.foreach(
                    Tabla_ConsultaHorarios.lista_horarios,
                    lambda info: rx.cond(
                        info[0] == "101",
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.button(
                                    rx.vstack(
                                        rx.text(info[0], 
                                               font_size=["9px", FontSize.SMALL.value]),
                                        rx.text(info[1], 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center",
                                    ),
                                    width=["70px", "150px"],
                                    height=["50px", "80px"],
                                    background=Colors.RED.value #Colors.PRIMARY_ORANGE.value
                                )
                            ),
                            rx.popover.content(
                                rx.vstack(
                                    rx.hstack(
                                        rx.popover.close(
                                            rx.button(rx.icon("x"), size="1"),
                                        ),
                                        width="100%",
                                        justify="end"
                                    ),
                                    rx.card(
                                        rx.data_list.root(
                                            rx.data_list.item(
                                                rx.data_list.label("Salon"),
                                                rx.data_list.value(info[0]),
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Docente"),
                                                rx.data_list.value(rx.text(
                                                    info[1],
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
                                                rx.data_list.label("Materia/Curso"),
                                                rx.data_list.value(rx.text(
                                                    info[2],
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
                                                rx.data_list.value(info[3]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Fecha"),
                                                rx.data_list.value(info[4]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Hora"),
                                                rx.data_list.value(info[6]),
                                                align="center",
                                            ),
                                        ),
                                        size="1",
                                        width="100%"
                                    ),
                                ),
                                size="1"
                            )
                        ),
                        rx.button(
                            rx.vstack(
                                rx.text("101", 
                                        font_size=["9px", FontSize.SMALL.value]),
                                rx.text("LIBRE", 
                                    font_size=["9px", FontSize.SMALL.value],
                                    max_width=["70px", "150px"],
                                    white_space="pre-wrap",
                                    overflow_wrap="break-word"
                                ),
                                spacing="0",
                                align="center",
                            ),
                            width=["70px", "150px"],
                            height=["50px", "80px"],
                            background=Colors.SECONDARY_GREEN.value
                        )
                    )
                ),
                rx.spacer(),
                # Salón 103
                rx.foreach(
                    Tabla_ConsultaHorarios.lista_horarios,
                    lambda info: rx.cond(
                        info[0] == "103",
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.button(
                                    rx.vstack(
                                        rx.text(info[0], 
                                               font_size=["9px", FontSize.SMALL.value]),
                                        rx.text(info[1],#info[1], 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center",
                                    ),
                                    width=["70px", "150px"],
                                    height=["50px", "80px"],
                                    background=Colors.RED.value

                                )
                            ),
                            rx.popover.content(
                                rx.vstack(
                                    rx.hstack(
                                        rx.popover.close(
                                            rx.button(rx.icon("x"), size="1"),
                                        ),
                                        width="100%",
                                        justify="end"
                                    ),
                                    rx.card(
                                        rx.data_list.root(
                                            rx.data_list.item(
                                                rx.data_list.label("Salon"),
                                                rx.data_list.value(info[0]),
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Docente"),
                                                rx.data_list.value(rx.text(
                                                    info[1],
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
                                                rx.data_list.label("Materia/Curso"),
                                                rx.data_list.value(rx.text(
                                                    info[2],
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
                                                rx.data_list.value(info[3]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Fecha"),
                                                rx.data_list.value(info[4]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Hora"),
                                                rx.data_list.value(info[6]),
                                                align="center",
                                            ),
                                        ),
                                        size="1",
                                        width="100%"
                                    ),
                                ),
                                size="1"
                            )
                        ),
                        rx.button(
                            rx.vstack(
                                rx.text("103", 
                                        font_size=["9px", FontSize.SMALL.value]),
                                rx.text("LIBRE", 
                                    font_size=["9px", FontSize.SMALL.value],
                                    max_width=["70px", "150px"],
                                    white_space="pre-wrap",
                                    overflow_wrap="break-word"
                                ),
                                spacing="0",
                                align="center",
                            ),
                            width=["70px", "150px"],
                            height=["50px", "80px"],
                            background=Colors.SECONDARY_GREEN.value
                        )
                    )
                ),
                #background="red",
                width=["95%", "80%"],
                justify="between"
            ),
            # Segunda fila (102, A/B, 104)
            rx.hstack(
                # Salón 102
                rx.foreach(
                    Tabla_ConsultaHorarios.lista_horarios,
                    lambda info: rx.cond(
                        info[0] == "102",
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.button(
                                    rx.vstack(
                                        rx.text(info[0], 
                                               font_size=["9px", FontSize.SMALL.value]),
                                        rx.text(info[1], 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center",
                                    ),
                                    width=["70px", "150px"],
                                    height=["50px", "80px"],
                                    background=Colors.RED.value
                                )
                            ),
                            rx.popover.content(
                                rx.vstack(
                                    rx.hstack(
                                        rx.popover.close(
                                            rx.button(rx.icon("x"), size="1"),
                                        ),
                                        width="100%",
                                        justify="end"
                                    ),
                                    rx.card(
                                        rx.data_list.root(
                                            rx.data_list.item(
                                                rx.data_list.label("Salon"),
                                                rx.data_list.value(info[0]),
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Docente"),
                                                rx.data_list.value(rx.text(
                                                    info[1],
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
                                                rx.data_list.label("Materia/Curso"),
                                                rx.data_list.value(rx.text(
                                                    info[2],
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
                                                rx.data_list.value(info[3]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Fecha"),
                                                rx.data_list.value(info[4]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Hora"),
                                                rx.data_list.value(info[6]),
                                                align="center",
                                            ),
                                        ),
                                        size="1",
                                        width="100%"
                                    ),
                                ),
                                size="1"
                            )
                        ),
                        rx.button(
                            rx.vstack(
                                rx.text("102", 
                                        font_size=["9px", FontSize.SMALL.value]),
                                rx.text("LIBRE", 
                                    font_size=["9px", FontSize.SMALL.value],
                                    max_width=["70px", "150px"],
                                    white_space="pre-wrap",
                                    overflow_wrap="break-word"
                                ),
                                spacing="0",
                                align="center",
                            ),
                            width=["70px", "150px"],
                            height=["50px", "80px"],
                            background=Colors.SECONDARY_GREEN.value
                        )
                    )
                ),
                # Salones A y B
                rx.flex(
                    # Salón A
                    rx.foreach(
                        Tabla_ConsultaHorarios.lista_horarios,
                        lambda info: rx.cond(
                            info[0] == "A",
                            rx.popover.root(
                                rx.popover.trigger(
                                    rx.button(
                                        rx.vstack(
                                            rx.text(info[0], 
                                                   font_size=["9px", FontSize.SMALL.value]),
                                            rx.text(info[1], 
                                                font_size=["9px", FontSize.SMALL.value],
                                                max_width=["70px", "150px"],
                                                white_space="pre-wrap",
                                                overflow_wrap="break-word"
                                            ),
                                            spacing="0",
                                            align="center"
                                        ),
                                        width=["60px", "150px"],
                                        height=["100px", "200px"],
                                        border_bottom_left_radius=["100px", "200px"],
                                        background=Colors.RED.value
                                    )
                                ),
                                rx.popover.content(
                                    rx.vstack(
                                        rx.hstack(
                                            rx.popover.close(
                                                rx.button(rx.icon("x"), size="1"),
                                            ),
                                            width="100%",
                                            justify="end"
                                        ),
                                        rx.card(
                                            rx.data_list.root(
                                                rx.data_list.item(
                                                    rx.data_list.label("Salon"),
                                                    rx.data_list.value(info[0]),
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Docente"),
                                                    rx.data_list.value(rx.text(
                                                        info[1],
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
                                                    rx.data_list.label("Materia/Curso"),
                                                    rx.data_list.value(rx.text(
                                                        info[2],
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
                                                    rx.data_list.value(info[3]),
                                                    align="center",
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Fecha"),
                                                    rx.data_list.value(info[4]),
                                                    align="center",
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Hora"),
                                                    rx.data_list.value(info[6]),
                                                    align="center",
                                                ),
                                            ),
                                            size="1",
                                            width="100%"
                                        ),
                                    ),
                                    size="1"
                                )
                            ),
                            rx.button(
                                rx.vstack(
                                    rx.text("A", 
                                            font_size=["9px", FontSize.SMALL.value]),
                                    rx.text("LIBRE", 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center"
                                    ),
                                    width=["60px", "150px"],
                                    height=["100px", "200px"],
                                    border_bottom_left_radius=["100px", "200px"],
                                    background=Colors.SECONDARY_GREEN.value
                            )
                        )
                    ),
                    # Salón B
                    rx.foreach(
                        Tabla_ConsultaHorarios.lista_horarios,
                        lambda info: rx.cond(
                            info[0] == "B",
                            rx.popover.root(
                                rx.popover.trigger(
                                    rx.button(
                                        rx.vstack(
                                            rx.text(info[0], 
                                                   font_size=["9px", FontSize.SMALL.value]),
                                            rx.text(info[1], 
                                                font_size=["9px", FontSize.SMALL.value],
                                                max_width=["70px", "150px"],
                                                white_space="pre-wrap",
                                                overflow_wrap="break-word"
                                            ),
                                            spacing="0",
                                            align="center"
                                        ),
                                        width=["60px", "150px"],
                                        height=["100px", "200px"],
                                        border_bottom_right_radius=["100px", "200px"],
                                        background=Colors.RED.value
                                    )
                                ),
                                rx.popover.content(
                                    rx.vstack(
                                        rx.hstack(
                                            rx.popover.close(
                                                rx.button(rx.icon("x"), size="1"),
                                            ),
                                            width="100%",
                                            justify="end"
                                        ),
                                        rx.card(
                                            rx.data_list.root(
                                                rx.data_list.item(
                                                    rx.data_list.label("Salon"),
                                                    rx.data_list.value(info[0]),
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Docente"),
                                                    rx.data_list.value(rx.text(
                                                        info[1],
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
                                                    rx.data_list.label("Materia/Curso"),
                                                    rx.data_list.value(rx.text(
                                                        info[2],
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
                                                    rx.data_list.value(info[3]),
                                                    align="center",
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Fecha"),
                                                    rx.data_list.value(info[4]),
                                                    align="center",
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Hora"),
                                                    rx.data_list.value(info[6]),
                                                    align="center",
                                                ),
                                            ),
                                            size="1",
                                            width="100%"
                                        ),
                                    ),
                                    size="1"
                                )
                            ),
                            rx.button(
                                rx.vstack(
                                    rx.text("B", 
                                            font_size=["9px", FontSize.SMALL.value]),
                                    rx.text("LIBRE", 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center"
                                    ),
                                    width=["60px", "150px"],
                                    height=["100px", "200px"],
                                    border_bottom_right_radius=["100px", "200px"],
                                    background=Colors.SECONDARY_GREEN.value
                            )
                        )
                    ),
                    spacing="2"
                ),
                # Salón 104
                rx.foreach(
                    Tabla_ConsultaHorarios.lista_horarios,
                    lambda info: rx.cond(
                        info[0] == "104",
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.button(
                                    rx.vstack(
                                        rx.text(info[0], 
                                               font_size=["9px", FontSize.SMALL.value]),
                                        rx.text(info[1], 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center",
                                    ),
                                    width=["70px", "150px"],
                                    height=["50px", "80px"],
                                    background=Colors.RED.value
                                )
                            ),
                            rx.popover.content(
                                rx.vstack(
                                    rx.hstack(
                                        rx.popover.close(
                                            rx.button(rx.icon("x"), size="1"),
                                        ),
                                        width="100%",
                                        justify="end"
                                    ),
                                    rx.card(
                                        rx.data_list.root(
                                            rx.data_list.item(
                                                rx.data_list.label("Salon"),
                                                rx.data_list.value(info[0]),
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Docente"),
                                                rx.data_list.value(rx.text(
                                                    info[1],
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
                                                rx.data_list.label("Materia/Curso"),
                                                rx.data_list.value(rx.text(
                                                    info[2],
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
                                                rx.data_list.value(info[3]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Fecha"),
                                                rx.data_list.value(info[4]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Hora"),
                                                rx.data_list.value(info[6]),
                                                align="center",
                                            ),
                                        ),
                                        size="1",
                                        width="100%"
                                    ),
                                ),
                                size="1"
                            )
                        ),
                        rx.button(
                            rx.vstack(
                                rx.text("104", 
                                        font_size=["9px", FontSize.SMALL.value]),
                                rx.text("LIBRE", 
                                    font_size=["9px", FontSize.SMALL.value],
                                    max_width=["70px", "150px"],
                                    white_space="pre-wrap",
                                    overflow_wrap="break-word"
                                ),
                                spacing="0",
                                align="center",
                            ),
                            width=["70px", "150px"],
                            height=["50px", "80px"],
                            background=Colors.SECONDARY_GREEN.value
                        )
                    )
                ),
                width=["95%", "80%"],
                justify="between"
            ),
            align="center",
        ),
        center_content=True,
        #background=Colors.PRIMARY_GREEN.value,
        padding="0px",
        #on_mount=Tabla_ConsultaHorarios.informacion_horarios
    )

def mapa_segundo_nivel():
    return rx.container(
        rx.vstack(
            rx.text("Segundo Nivel (Segundo Piso)", 
                   font_size=[FontSize.SMALL.value, FontSize.LARGE.value]),
            # Primera fila (201 y 203)
            rx.hstack(
                # Salón 201
                rx.foreach(
                    Tabla_ConsultaHorarios.lista_horarios,
                    lambda info: rx.cond(
                        info[0] == "201",
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.button(
                                    rx.vstack(
                                        rx.text(info[0], 
                                               font_size=["9px", FontSize.SMALL.value]),
                                        rx.text(info[1], 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center",
                                    ),
                                    width=["70px", "150px"],
                                    height=["50px", "80px"],
                                    background=Colors.RED.value #Colors.PRIMARY_ORANGE.value
                                )
                            ),
                            rx.popover.content(
                                rx.vstack(
                                    rx.hstack(
                                        rx.popover.close(
                                            rx.button(rx.icon("x"), size="1"),
                                        ),
                                        width="100%",
                                        justify="end"
                                    ),
                                    rx.card(
                                        rx.data_list.root(
                                            rx.data_list.item(
                                                rx.data_list.label("Salon"),
                                                rx.data_list.value(info[0]),
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Docente"),
                                                rx.data_list.value(rx.text(
                                                    info[1],
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
                                                rx.data_list.label("Materia/Curso"),
                                                rx.data_list.value(rx.text(
                                                    info[2],
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
                                                rx.data_list.value(info[3]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Fecha"),
                                                rx.data_list.value(info[4]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Hora"),
                                                rx.data_list.value(info[6]),
                                                align="center",
                                            ),
                                        ),
                                        size="1",
                                        width="100%"
                                    ),
                                ),
                                size="1"
                            )
                        ),
                        rx.button(
                            rx.vstack(
                                rx.text("201", 
                                        font_size=["9px", FontSize.SMALL.value]),
                                rx.text("LIBRE", 
                                    font_size=["9px", FontSize.SMALL.value],
                                    max_width=["70px", "150px"],
                                    white_space="pre-wrap",
                                    overflow_wrap="break-word"
                                ),
                                spacing="0",
                                align="center",
                            ),
                            width=["70px", "150px"],
                            height=["50px", "80px"],
                            background=Colors.SECONDARY_GREEN.value
                        )
                    )
                ),
                rx.spacer(),
                # Salón 203
                rx.foreach(
                    Tabla_ConsultaHorarios.lista_horarios,
                    lambda info: rx.cond(
                        info[0] == "203",
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.button(
                                    rx.vstack(
                                        rx.text(info[0], 
                                               font_size=["9px", FontSize.SMALL.value]),
                                        rx.text(info[1],#info[1], 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center",
                                    ),
                                    width=["70px", "150px"],
                                    height=["50px", "80px"],
                                    background=Colors.RED.value

                                )
                            ),
                            rx.popover.content(
                                rx.vstack(
                                    rx.hstack(
                                        rx.popover.close(
                                            rx.button(rx.icon("x"), size="1"),
                                        ),
                                        width="100%",
                                        justify="end"
                                    ),
                                    rx.card(
                                        rx.data_list.root(
                                            rx.data_list.item(
                                                rx.data_list.label("Salon"),
                                                rx.data_list.value(info[0]),
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Docente"),
                                                rx.data_list.value(rx.text(
                                                    info[1],
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
                                                rx.data_list.label("Materia/Curso"),
                                                rx.data_list.value(rx.text(
                                                    info[2],
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
                                                rx.data_list.value(info[3]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Fecha"),
                                                rx.data_list.value(info[4]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Hora"),
                                                rx.data_list.value(info[6]),
                                                align="center",
                                            ),
                                        ),
                                        size="1",
                                        width="100%"
                                    ),
                                ),
                                size="1"
                            )
                        ),
                        rx.button(
                            rx.vstack(
                                rx.text("203", 
                                        font_size=["9px", FontSize.SMALL.value]),
                                rx.text("LIBRE", 
                                    font_size=["9px", FontSize.SMALL.value],
                                    max_width=["70px", "150px"],
                                    white_space="pre-wrap",
                                    overflow_wrap="break-word"
                                ),
                                spacing="0",
                                align="center",
                            ),
                            width=["70px", "150px"],
                            height=["50px", "80px"],
                            background=Colors.SECONDARY_GREEN.value
                        )
                    )
                ),
                #background="red",
                width=["95%", "80%"],
                justify="between"
            ),
            # Segunda fila (202, C/D, 204)
            rx.hstack(
                # Salón 202
                rx.foreach(
                    Tabla_ConsultaHorarios.lista_horarios,
                    lambda info: rx.cond(
                        info[0] == "202",
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.button(
                                    rx.vstack(
                                        rx.text(info[0], 
                                               font_size=["9px", FontSize.SMALL.value]),
                                        rx.text(info[1], 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center",
                                    ),
                                    width=["70px", "150px"],
                                    height=["50px", "80px"],
                                    background=Colors.RED.value
                                )
                            ),
                            rx.popover.content(
                                rx.vstack(
                                    rx.hstack(
                                        rx.popover.close(
                                            rx.button(rx.icon("x"), size="1"),
                                        ),
                                        width="100%",
                                        justify="end"
                                    ),
                                    rx.card(
                                        rx.data_list.root(
                                            rx.data_list.item(
                                                rx.data_list.label("Salon"),
                                                rx.data_list.value(info[0]),
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Docente"),
                                                rx.data_list.value(rx.text(
                                                    info[1],
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
                                                rx.data_list.label("Materia/Curso"),
                                                rx.data_list.value(rx.text(
                                                    info[2],
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
                                                rx.data_list.value(info[3]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Fecha"),
                                                rx.data_list.value(info[4]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Hora"),
                                                rx.data_list.value(info[6]),
                                                align="center",
                                            ),
                                        ),
                                        size="1",
                                        width="100%"
                                    ),
                                ),
                                size="1"
                            )
                        ),
                        rx.button(
                            rx.vstack(
                                rx.text("202", 
                                        font_size=["9px", FontSize.SMALL.value]),
                                rx.text("LIBRE", 
                                    font_size=["9px", FontSize.SMALL.value],
                                    max_width=["70px", "150px"],
                                    white_space="pre-wrap",
                                    overflow_wrap="break-word"
                                ),
                                spacing="0",
                                align="center",
                            ),
                            width=["70px", "150px"],
                            height=["50px", "80px"],
                            background=Colors.SECONDARY_GREEN.value
                        )
                    )
                ),
                # Salones C y D
                rx.flex(
                    # Salón C
                    rx.foreach(
                        Tabla_ConsultaHorarios.lista_horarios,
                        lambda info: rx.cond(
                            info[0] == "C",
                            rx.popover.root(
                                rx.popover.trigger(
                                    rx.button(
                                        rx.vstack(
                                            rx.text(info[0], 
                                                   font_size=["9px", FontSize.SMALL.value]),
                                            rx.text(info[1], 
                                                font_size=["9px", FontSize.SMALL.value],
                                                max_width=["70px", "150px"],
                                                white_space="pre-wrap",
                                                overflow_wrap="break-word"
                                            ),
                                            spacing="0",
                                            align="center"
                                        ),
                                        width=["60px", "150px"],
                                        height=["100px", "200px"],
                                        border_bottom_left_radius=["100px", "200px"],
                                        background=Colors.RED.value
                                    )
                                ),
                                rx.popover.content(
                                    rx.vstack(
                                        rx.hstack(
                                            rx.popover.close(
                                                rx.button(rx.icon("x"), size="1"),
                                            ),
                                            width="100%",
                                            justify="end"
                                        ),
                                        rx.card(
                                            rx.data_list.root(
                                                rx.data_list.item(
                                                    rx.data_list.label("Salon"),
                                                    rx.data_list.value(info[0]),
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Docente"),
                                                    rx.data_list.value(rx.text(
                                                        info[1],
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
                                                    rx.data_list.label("Materia/Curso"),
                                                    rx.data_list.value(rx.text(
                                                        info[2],
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
                                                    rx.data_list.value(info[3]),
                                                    align="center",
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Fecha"),
                                                    rx.data_list.value(info[4]),
                                                    align="center",
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Hora"),
                                                    rx.data_list.value(info[6]),
                                                    align="center",
                                                ),
                                            ),
                                            size="1",
                                            width="100%"
                                        ),
                                    ),
                                    size="1"
                                )
                            ),
                            rx.button(
                                rx.vstack(
                                    rx.text("C", 
                                            font_size=["9px", FontSize.SMALL.value]),
                                    rx.text("LIBRE", 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center"
                                    ),
                                    width=["60px", "150px"],
                                    height=["100px", "200px"],
                                    border_bottom_left_radius=["100px", "200px"],
                                    background=Colors.SECONDARY_GREEN.value
                            )
                        )
                    ),
                    # Salón D
                    rx.foreach(
                        Tabla_ConsultaHorarios.lista_horarios,
                        lambda info: rx.cond(
                            info[0] == "D",
                            rx.popover.root(
                                rx.popover.trigger(
                                    rx.button(
                                        rx.vstack(
                                            rx.text(info[0], 
                                                   font_size=["9px", FontSize.SMALL.value]),
                                            rx.text(info[1], 
                                                font_size=["9px", FontSize.SMALL.value],
                                                max_width=["70px", "150px"],
                                                white_space="pre-wrap",
                                                overflow_wrap="break-word"
                                            ),
                                            spacing="0",
                                            align="center"
                                        ),
                                        width=["60px", "150px"],
                                        height=["100px", "200px"],
                                        border_bottom_right_radius=["100px", "200px"],
                                        background=Colors.RED.value
                                    )
                                ),
                                rx.popover.content(
                                    rx.vstack(
                                        rx.hstack(
                                            rx.popover.close(
                                                rx.button(rx.icon("x"), size="1"),
                                            ),
                                            width="100%",
                                            justify="end"
                                        ),
                                        rx.card(
                                            rx.data_list.root(
                                                rx.data_list.item(
                                                    rx.data_list.label("Salon"),
                                                    rx.data_list.value(info[0]),
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Docente"),
                                                    rx.data_list.value(rx.text(
                                                        info[1],
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
                                                    rx.data_list.label("Materia/Curso"),
                                                    rx.data_list.value(rx.text(
                                                        info[2],
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
                                                    rx.data_list.value(info[3]),
                                                    align="center",
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Fecha"),
                                                    rx.data_list.value(info[4]),
                                                    align="center",
                                                ),
                                                rx.data_list.item(
                                                    rx.data_list.label("Hora"),
                                                    rx.data_list.value(info[6]),
                                                    align="center",
                                                ),
                                            ),
                                            size="1",
                                            width="100%"
                                        ),
                                    ),
                                    size="1"
                                )
                            ),
                            rx.button(
                                rx.vstack(
                                    rx.text("D", 
                                            font_size=["9px", FontSize.SMALL.value]),
                                    rx.text("LIBRE", 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center"
                                    ),
                                    width=["60px", "150px"],
                                    height=["100px", "200px"],
                                    border_bottom_right_radius=["100px", "200px"],
                                    background=Colors.SECONDARY_GREEN.value
                            )
                        )
                    ),
                    spacing="2"
                ),
                # Salón 204
                rx.foreach(
                    Tabla_ConsultaHorarios.lista_horarios,
                    lambda info: rx.cond(
                        info[0] == "204",
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.button(
                                    rx.vstack(
                                        rx.text(info[0], 
                                               font_size=["9px", FontSize.SMALL.value]),
                                        rx.text(info[1], 
                                            font_size=["9px", FontSize.SMALL.value],
                                            max_width=["70px", "150px"],
                                            white_space="pre-wrap",
                                            overflow_wrap="break-word"
                                        ),
                                        spacing="0",
                                        align="center",
                                    ),
                                    width=["70px", "150px"],
                                    height=["50px", "80px"],
                                    background=Colors.RED.value
                                )
                            ),
                            rx.popover.content(
                                rx.vstack(
                                    rx.hstack(
                                        rx.popover.close(
                                            rx.button(rx.icon("x"), size="1"),
                                        ),
                                        width="100%",
                                        justify="end"
                                    ),
                                    rx.card(
                                        rx.data_list.root(
                                            rx.data_list.item(
                                                rx.data_list.label("Salon"),
                                                rx.data_list.value(info[0]),
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Docente"),
                                                rx.data_list.value(rx.text(
                                                    info[1],
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
                                                rx.data_list.label("Materia/Curso"),
                                                rx.data_list.value(rx.text(
                                                    info[2],
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
                                                rx.data_list.value(info[3]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Fecha"),
                                                rx.data_list.value(info[4]),
                                                align="center",
                                            ),
                                            rx.data_list.item(
                                                rx.data_list.label("Hora"),
                                                rx.data_list.value(info[6]),
                                                align="center",
                                            ),
                                        ),
                                        size="1",
                                        width="100%"
                                    ),
                                ),
                                size="1"
                            )
                        ),
                        rx.button(
                            rx.vstack(
                                rx.text("204", 
                                        font_size=["9px", FontSize.SMALL.value]),
                                rx.text("LIBRE", 
                                    font_size=["9px", FontSize.SMALL.value],
                                    max_width=["70px", "150px"],
                                    white_space="pre-wrap",
                                    overflow_wrap="break-word"
                                ),
                                spacing="0",
                                align="center",
                            ),
                            width=["70px", "150px"],
                            height=["50px", "80px"],
                            background=Colors.SECONDARY_GREEN.value
                        )
                    )
                ),
                width=["95%", "80%"],
                justify="between"
            ),
            align="center",
        ),
        center_content=True,
        #background=Colors.PRIMARY_GREEN.value,
        padding="0px",
        on_mount=Tabla_ConsultaHorarios.informacion_horarios
    )

# def mapa_segundo_nivel():
#     return rx.container(
#         rx.vstack(
#             rx.text("Segundo Nivel (Segundo Piso)", font_size=[FontSize.SMALL.value, FontSize.LARGE.value]),
#             rx.hstack(
#                 rx.button("201", width=["70px", "150px"], height=["50px", "80px"]),
#                 rx.button("203", width=["70px", "150px"], height=["50px", "80px"]),
#                 background="red",
#                 width=["95%", "80%"],
#                 justify="between"
#             ),
#             rx.hstack(
#                 rx.button("202", width=["70px", "150px"], height=["50px", "80px"]),
#                 rx.button("C", width=["60px", "150px"], height=["100px", "200px"], border_bottom_left_radius=["100px", "200px"]),
#                 rx.button("D", width=["60px", "150px"], height=["100px", "200px"], border_bottom_right_radius=["100px", "200px"]),
#                 rx.button("204", width=["70px", "150px"], height=["50px", "80px"]),
#                 # background=Colors.PRIMARY_GREEN.value,
#                 width=["95%", "80%"],
#                 justify="between"
#             ),
#             #background=Colors.PRIMARY_GREEN.value,
#             align="center",
#         ),
#         center_content=True,
#         #background=Colors.PRIMARY_GREEN.value,
#         padding="0px"
#     )

# def mapa_primer_nivel() -> rx.Component:
#     return rx.box(
#         rx.foreach(
#             Tabla_ConsultaHorarios.lista_horarios,
#             datos_primer_nivel
#         ),
#         on_mount=Tabla_ConsultaHorarios.informacion_horarios
#     )

# def mapa_segundo_nivel() -> rx.Component:
#     return rx.box(

#     )
# def matriz_horarios() -> rx.Component:
#     pass