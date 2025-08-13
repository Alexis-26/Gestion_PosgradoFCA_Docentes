import reflex as rx
from ..styles.colors import Colors
from ..styles.styles import FontSize
from ..state import ConsultaHorarios, AsignacionHorarios
from .formulario_reserva import form_reservar
from .simbologia import simbologia_colores
from .reservacion import reservar_salon

def get_bg_color(estado):
    return rx.cond(
        estado == "RESERVADO",
        Colors.RED.value,
        rx.cond(
            estado == "FIJO",
            Colors.BLACK.value,
            "white"
        )
    )

def dialog_form_normal(salon:str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.vstack(
                    rx.text(salon, font_size=["9px", FontSize.SMALL.value]),
                    rx.text("LIBRE", font_size=["9px", FontSize.SMALL.value],
                            max_width=["70px", "150px"],
                            white_space="pre-wrap",
                            overflow_wrap="break-word"),
                    spacing="0",
                    align="center",
                    ),
                width=["70px", "150px"],
                height=["50px", "80px"],
                background=Colors.SECONDARY_GREEN.value,
                border="solid",
                border_color="green",
                on_click=lambda:AsignacionHorarios.seleccion_salon(salon)
            )
        ),
        # rx.dialog.content(
        #         rx.box(
        #             form_reservar(),
        #             width="100%",
        #         ),
        #         style={
        #             "background": "transparent",
        #             "box_shadow": "none",
        #             "max_width": "900px",
        #             "width": "100%",
        #         },
        # ),
        # open=AsignacionHorarios.salon_abierto == salon,  # Solo si quieres controlarlo por estado
    )

def dialog_form_izquierda(salon:str):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.vstack(
                    rx.text(salon, 
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
                    border="solid",
                    border_color="green",
                    padding="20px",
                    background=Colors.SECONDARY_GREEN.value,
                    on_click=lambda:AsignacionHorarios.seleccion_salon(salon)
            )
        ),
        # rx.dialog.content(
        #         rx.box(
        #             form_reservar(),
        #             width="100%",
        #         ),
        #         style={
        #             "background": "transparent",
        #             "box_shadow": "none",
        #             "max_width": "900px",
        #             "width": "100%",
        #         },
        # ),
        # open=AsignacionHorarios.salon_abierto == salon,  # Solo si quieres controlarlo por estado
    )

def dialog_form_derecha(salon:str):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.vstack(
                    rx.text(salon, 
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
                    border="solid",
                    border_color="green",
                    padding="20px",
                    background=Colors.SECONDARY_GREEN.value,
                    on_click=lambda:AsignacionHorarios.seleccion_salon(salon)
            )
        ),
        # rx.dialog.content(
        #         rx.box(
        #             form_reservar(),
        #             width="100%",
        #         ),
        #         style={
        #             "background": "transparent",
        #             "box_shadow": "none",
        #             "max_width": "900px",
        #             "width": "100%",
        #         },
        # ),
        # open=AsignacionHorarios.salon_abierto == salon,  # Solo si quieres controlarlo por estado
    )

def salon_normal(info):
    return rx.popover.root(
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
                background=get_bg_color(info[7]) #Colors.PRIMARY_ORANGE.value
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

def salon_especial_izquierda(info):
    return rx.popover.root(
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
                background=get_bg_color(info[7])
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

def salon_especial_derecha(info):
    return rx.popover.root(
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
                background=get_bg_color(info[7])
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

def render_salon(salon_id: str):
    return rx.cond(
        ConsultaHorarios.salones_informacion.get(salon_id, False),
        rx.foreach(
            ConsultaHorarios.lista_horarios,
            lambda info: rx.cond(
                info[0] == salon_id,
                salon_normal(info),
                rx.fragment()
            ),
        ),
        dialog_form_normal(salon_id)
    )


def render_salon_especial_izquierda(salon_id: str):
    return rx.cond(
        ConsultaHorarios.salones_informacion.get(salon_id, False),
        rx.foreach(
            ConsultaHorarios.lista_horarios,
            lambda info: rx.cond(
                info[0] == salon_id,
                salon_especial_izquierda(info),
                rx.fragment()
            ),
        ),
        dialog_form_izquierda(salon_id)
    )

def render_salon_especial_derecha(salon_id: str):
    return rx.cond(
        ConsultaHorarios.salones_informacion.get(salon_id, False),
        rx.foreach(
            ConsultaHorarios.lista_horarios,
            lambda info: rx.cond(
                info[0] == salon_id,
                salon_especial_derecha(info),
                rx.fragment()
            ),
        ),
        dialog_form_derecha(salon_id)
    )

def mapa_primer_nivel():
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.text("Primer Nivel (Primer Piso)", 
                        font_size=[FontSize.SMALL.value, FontSize.LARGE.value]),
                rx.text(f"Reservaciones de las {ConsultaHorarios.select_horas}", 
                        font_size=[FontSize.SMALL.value, FontSize.MEDIUM.value]),
                # Primera fila (101 y 103)
                # rx.hstack(
                #     render_salon("101"),
                #     render_salon("103"),
                #     width=["95%", "80%"],
                #     justify="between"
                # ),
                
                # # Segunda fila (102, A/B, 104)
                # rx.hstack(
                #     render_salon("102"),
                #     rx.flex(
                #         render_salon_especial_izquierda("A"),
                #         render_salon_especial_derecha("B"),
                #         spacing="2"
                #     ),
                #     render_salon("104"),
                #     width=["95%", "80%"],
                #     justify="between"
                # ),
                rx.grid(
                    render_salon("101"),
                    rx.box(),  # vacío
                    rx.box(),  # vacío
                    render_salon("103"),
                    render_salon("102"),
                    render_salon_especial_izquierda("A"),
                    render_salon_especial_derecha("B"),
                    render_salon("104"),
                    columns="4",
                    spacing="4",
                    border="solid",
                    border_color="green",
                    padding="20px"
                ),
                simbologia_colores(),
                align="center",
                spacing="2",
                #background="red",
                width="100%",
            ),
            # center_content=True,
            # padding="0px",
            # padding_bottom="10px",
            # background_image="url('/salones_c.png')",
            # background_size="84%",  # Usa 'contain' o un tamaño específico como '80%'
            # background_position="center",
            # background_repeat="no-repeat",
            # width="100%",
            # height="100%",
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.text("Primer Nivel (Primer Piso)", 
                        font_size=[FontSize.SMALL.value, FontSize.LARGE.value]),
                rx.text(f"Reservaciones de las {ConsultaHorarios.select_horas}", 
                        font_size=[FontSize.SMALL.value, FontSize.MEDIUM.value]),
                # Primera fila (101 y 103)
                rx.grid(
                    render_salon("101"),
                    rx.box(),  # vacío
                    rx.box(),  # vacío
                    render_salon("103"),
                    render_salon("102"),
                    render_salon_especial_izquierda("A"),
                    render_salon_especial_derecha("B"),
                    render_salon("104"),
                    columns="4",
                    spacing="1",
                    border="solid",
                    border_color="green",
                    padding="10px"
                ),
                simbologia_colores(),
                align="center",
                spacing="2",
                width="100%",
            ),
            # center_content=True,
            # padding="0px",
            #padding_bottom="10px",
            #background_image="url('/salones_c.png')",
            #background_size="84%",  # Usa 'contain' o un tamaño específico como '80%'
            #background_position="center",
            #background_repeat="no-repeat",
            # width="100%",
            # height="100%",
        ),
    )


def mapa_segundo_nivel():
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.text("Segundo Nivel (Segundo Piso)", 
                        font_size=[FontSize.SMALL.value, FontSize.LARGE.value]),
                rx.text(f"Reservaciones de las {ConsultaHorarios.select_horas}", 
                        font_size=[FontSize.SMALL.value, FontSize.MEDIUM.value]),
                # rx.hstack(
                #     render_salon("201"),
                #     rx.spacer(),
                #     render_salon("203"),
                #     width=["95%", "80%"],
                #     justify="between"
                # ),
                # rx.hstack(
                #     render_salon("202"),
                #     rx.flex(
                #         render_salon_especial_izquierda("C"),
                #         render_salon_especial_derecha("D"),
                #         spacing="2"
                #     ),
                #     render_salon("204"),
                #     width=["95%", "80%"],
                #     justify="between"
                # ),
                rx.grid(
                    render_salon("201"),
                    rx.box(),  # vacío
                    rx.box(),  # vacío
                    render_salon("203"),
                    render_salon("202"),
                    render_salon_especial_izquierda("C"),
                    render_salon_especial_derecha("D"),
                    render_salon("204"),
                    columns="4",
                    spacing="4",
                    border="solid",
                    border_color="green",
                    padding="20px",
                ),
                simbologia_colores(),
                align="center",
                spacing="2",
                width="100%",
            ),
            # center_content=True,
            # padding="0px",
            # padding_bottom="10px",
            # background_image="url('/salones_c.png')",
            # background_size="84%",  # Usa 'contain' o un tamaño específico como '80%'
            # background_position="center",
            # background_repeat="no-repeat",
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                rx.text("Segundo Nivel (Segundo Piso)", 
                        font_size=[FontSize.SMALL.value, FontSize.LARGE.value]),
                rx.text(f"Reservaciones de las {ConsultaHorarios.select_horas}", 
                        font_size=[FontSize.SMALL.value, FontSize.MEDIUM.value]),
                # rx.hstack(
                #     render_salon("201"),
                #     rx.spacer(),
                #     render_salon("203"),
                #     width=["95%", "80%"],
                #     justify="between"
                # ),
                # rx.hstack(
                #     render_salon("202"),
                #     rx.flex(
                #         render_salon_especial_izquierda("C"),
                #         render_salon_especial_derecha("D"),
                #         spacing="2"
                #     ),
                #     render_salon("204"),
                #     width=["95%", "80%"],
                #     justify="between"
                # ),
                rx.grid(
                    render_salon("201"),
                    rx.box(),  # vacío
                    rx.box(),  # vacío
                    render_salon("203"),
                    render_salon("202"),
                    render_salon_especial_izquierda("C"),
                    render_salon_especial_derecha("D"),
                    render_salon("204"),
                    columns="4",
                    spacing="1",
                    border="solid",
                    border_color="green",
                    padding="10px",
                    justify="between"
                ),
                simbologia_colores(),
                align="center",
                spacing="2"
            ),
            center_content=True,
            padding="0px",
            # padding_bottom="10px",
            # background_image="url('/salones_c.png')",
            # background_size="84%",  # Usa 'contain' o un tamaño específico como '80%'
            # background_position="center",
            # background_repeat="no-repeat",
        ),
    )