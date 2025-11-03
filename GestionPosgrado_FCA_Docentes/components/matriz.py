from ..state import ConsultaHorarios
from ..styles.colors import Colors
from ..styles.styles import FontSize
import reflex as rx

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

def show_row(kv):
    # kv[0] es la clave (hora), kv[1] es la tupla con los valores
    def cell_content(valores):
        return rx.cond(
            valores.length() == 0,
            rx.flex(
                rx.vstack(
                    rx.text("LIBRE", color="white", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value]), 
                    background=Colors.SECONDARY_GREEN.value,
                    width="100%", 
                    height="100%",
                    align="center",
                    padding="0",
                    spacing="0"
                    ),
                width=["60px", "100%"], 
                height=["60px","80px"],
                justify="center",
                align="center",
                padding="0"
            ),
            rx.flex(
                rx.vstack(
                    rx.text(valores[1], color="white", font_size=[FontSize.LITTLE.value, FontSize.SMALL.value]),
                    rx.text(f"Grupo: {valores[3]}", color="white", font_size=[FontSize.LITTLE.value, FontSize.SMALL.value]),
                    background=get_bg_color(valores[7]),
                    padding="0",
                    width="100%", 
                    height="100%",
                    spacing="0",
                ),
                width=["60px", "100%"], # PENDIENTE A 100%
                height=["60px","80px"],
                justify="center",
                align="center",
                padding="0"
            )
        )
    return rx.table.row(
        rx.table.row_header_cell(kv[0], justify="center", background=Colors.SECONDARY_ORANGE.value, border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["10px", "40px"]),
        rx.foreach(kv[1], lambda valores: rx.table.cell(cell_content(valores), padding="0", border="2px solid #000000",)),
        align="center"
    )

def horario_table_1():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Hora", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value]),
                rx.table.column_header_cell(ConsultaHorarios.salones_primer_nivel[0], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                rx.table.column_header_cell(ConsultaHorarios.salones_primer_nivel[1], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                rx.table.column_header_cell(ConsultaHorarios.salones_primer_nivel[2], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                rx.table.column_header_cell(ConsultaHorarios.salones_primer_nivel[3], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                rx.table.column_header_cell(ConsultaHorarios.salones_primer_nivel[4], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                rx.table.column_header_cell(ConsultaHorarios.salones_primer_nivel[5], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                background=Colors.SECONDARY_ORANGE.value,
            ),
        ),
        rx.table.body(
            rx.foreach(ConsultaHorarios.horario_dict_1.items(), show_row)
        ),
        on_mount=ConsultaHorarios.informacion_horarios,
        width=["100%", "70%"],
    )

def horario_table_2():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Hora", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value]),
                rx.table.column_header_cell(ConsultaHorarios.salones_segundo_nivel[0], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                rx.table.column_header_cell(ConsultaHorarios.salones_segundo_nivel[1], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                rx.table.column_header_cell(ConsultaHorarios.salones_segundo_nivel[2], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                rx.table.column_header_cell(ConsultaHorarios.salones_segundo_nivel[3], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                rx.table.column_header_cell(ConsultaHorarios.salones_segundo_nivel[4], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                rx.table.column_header_cell(ConsultaHorarios.salones_segundo_nivel[5], justify="center", border="2px solid #000000", font_size=[FontSize.EXTRA_SMALL.value, FontSize.SMALL.value], width=["60px", "150px"]),
                background=Colors.SECONDARY_ORANGE.value
            ),
        ),
        rx.table.body(
            rx.foreach(ConsultaHorarios.horario_dict_2.items(), show_row)
        ),
        width=["100%", "70%"],
    )