from ..state import ConsultaHorarios
from ..styles.colors import Colors
from ..styles.styles import FontSize
import reflex as rx

# def horario_table():
#     columnas = ["Hora/Salon", "101", "102", "103", "104", "A", "B"]  # La primera vacía para la columna de horarios

#     datos = [
#         ["07:00", "A", "B", "C"],
#         ["08:00", "A", "B", "C"],
#         ["09:00", "D", "E", "F"],
#         ["10:00", "G", "H", "I"],
#         ["11:00", "G", "H", "I"],
#         ["12:00", "G", "H", "I"],
#         ["13:00", "G", "H", "I"],
#         ["14:00", "G", "H", "I"],
#         ["15:00", "G", "H", "I"],
#         ["16:00", "G", "H", "I"],
#         ["17:00", "G", "H", "I"],
#         ["18:00", "G", "H", "I"],
#         ["19:00", "G", "H", "I"],
#         ["20:00", "G", "H", "I"],
#         ["21:00", "G", "H", "I"],
#     ]

#     return rx.table.root(
#         rx.table.header(
#             rx.table.row(
#                 rx.foreach(columnas, lambda col: rx.table.column_header_cell(col))
#             )
#         ),
#         rx.table.body(
#             rx.foreach(
#                 datos,
#                 lambda fila: rx.table.row(
#                     rx.table.row_header_cell(fila[0]),
#                     rx.table.cell(fila[1]),
#                     rx.table.cell(fila[2]),
#                     rx.table.cell(fila[3]),
#                 )
#             )
#         ),
#     )


# def show_row(kv):
#     # kv[0] es la clave (hora), kv[1] es la tupla con los valores
#     return rx.table.row(
#         rx.table.row_header_cell(kv[0]),
#         rx.table.cell(kv[1][0]),
#         rx.table.cell(kv[1][1]),
#         rx.table.cell(kv[1][2]),
#         rx.table.cell(kv[1][3]),
#         rx.table.cell(kv[1][4]),
#         rx.table.cell(kv[1][5]),
#         rx.table.cell(kv[1][6]),
#     )

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
                    # border_width="3px",
                    # border_color=Colors.PRIMARY_GREEN.value,
                    # border_style="solid",
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
                    #rx.text(valores[2], color="white"),
                    rx.text(f"Grupo: {valores[3]}", color="white", font_size=[FontSize.LITTLE.value, FontSize.SMALL.value]),
                    background=get_bg_color(valores[7]),
                    padding="0",
                    width="100%", 
                    height="100%",
                    spacing="0",
                ),
                width=["60px", "150px"], # PENDIENTE A 100%
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
        #padding=["5px", "40px"],
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
        #on_mount=ConsultaHorarios.informacion_horarios,
        width=["100%", "70%"],
        #padding=["5px", "40px"],
    )