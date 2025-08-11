import reflex as rx 
from ..state import AsignacionHorarios

def checkbox(hora:str):
    return rx.flex(
        rx.checkbox(text=hora, size="1"),
        align="center",
        class_name="flex-row",
        )

def reservar() -> rx.Component:
    return rx.form(
        rx.vstack(
            # Employee Information Section
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.text("Número de empleado"),
                        rx.input(                               # Aqui esta el input de NUMERO DE EMPLEADO
                            placeholder="Número del empleado",
                            name="numero_empleado",
                            required=True,
                        ),
                        class_name="formulario_input_un",
                    ),
                    rx.box(
                        rx.text("Nombre del maestro"),
                        rx.input(                       # Aqui esta el input de NUMERO DEL MAESTRO
                            placeholder="Nombre del maestro", 
                            name="nombre_maestro",
                            required=True,
                            class_name="extender_input"
                        ),
                        class_name="formulario_input_un",
                    ),
                ),
            ),
            
            # Course Information Section
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.text("Clave de la materia"),
                        rx.input(                        # Aqui esta el input CLAVE MATERIA
                            placeholder="Clave de la materia",
                            name="clave_materia", 
                            required=True,
                        ),
                        class_name="formulario_input_un",
                    ),
                    rx.box(
                        rx.text("Nombre de la materia"),
                        rx.input(                         # Aqui esta el input de NOMBRE DE LA MATERIA 
                            placeholder="Nombre de la materia",
                            name="nombre_materia",
                            required=True,
                            class_name="extender_input"
                        ),
                        class_name="formulario_input_un",
                    ),
                ),
                rx.hstack(
                    rx.box(
                        rx.text("Grupo"),
                        rx.input(            # Aqui esta el input de GRUPO
                            placeholder="Grupo",
                            name="grupo",
                            required=True,
                        ),
                        class_name="formulario_input_un",
                    ),
                    rx.box(
                        rx.checkbox(text="Horario fijo", name="horario_fijo"),
                        class_name="horario",
                    ),
                    rx.box(
                        rx.accordion.root(
                            rx.accordion.item(
                                header="Seleccionar horario",
                                content=rx.vstack(
                                    rx.checkbox(text="7:00", color_scheme="blue", value="7:00", name="1hora"),
                                    rx.checkbox(text="8:00", color_scheme="blue", value="8:00", name="2hora"), 
                                    rx.checkbox(text="9:00", color_scheme="blue", value="9:00", name="3hora"),
                                    rx.checkbox(text="10:00", color_scheme="blue", value="10:00", name="4hora"),
                                    rx.checkbox(text="11:00", color_scheme="blue", value="11:00", name="5hora"),
                                    rx.checkbox(text="12:00", color_scheme="blue", value="12:00", name="6hora"),
                                    rx.checkbox(text="13:00", color_scheme="blue", value="13:00", name="7hora"),
                                    rx.checkbox(text="14:00", color_scheme="blue", value="14:00", name="8hora"),
                                    rx.checkbox(text="15:00", color_scheme="blue", value="15:00", name="9hora"),
                                    rx.checkbox(text="16:00", color_scheme="blue", value="16:00", name="10hora"),
                                    rx.checkbox(text="17:00", color_scheme="blue", value="17:00", name="11hora"),
                                    rx.checkbox(text="18:00", color_scheme="blue", value="18:00", name="12hora"),
                                    rx.checkbox(text="19:00", color_scheme="blue", value="19:00", name="13hora"),
                                    rx.checkbox(text="20:00", color_scheme="blue", value="20:00", name="14hora"),
                                    rx.checkbox(text="21:00", color_scheme="blue", value="21:00", name="15hora"),
                                    rx.checkbox(text="22:00", color_scheme="blue", value="22:00", name="16hora"),
                                ),
                            ),
                            collapsible=False,
                            color_scheme="grass",
                            class_name="Opcion_1"
                        ),
                        class_name="seleccion_horas"
                    ),
                    spacing="4",
                ),
            ),
            
            # Date Selection Section
            rx.vstack(
                rx.hstack(
                    rx.box(
                        rx.text("Fecha de inicio"),
                        rx.input(                     # Aqui esta el input DE FECHA DE INICIO 
                            type="date",
                            name="fecha_inicio",
                            required=True,
                            class_name="formulario_input_un",
                        ),
                         class_name="formulario_input_un",
                    ),
                    rx.box(
                        rx.text("Fecha de fin"), 
                        rx.input(                   # Aqui esta el input DE FECHA DE FIN 
                            type="date",
                            name="fecha_fin",
                            required=True,
                            class_name="formulario_input_un",
                        ),
                         class_name="formulario_input_un",
                    ),
                    spacing="4",
                ),
            ),


            # Action Buttons Section
            rx.box(
                rx.hstack(
                    rx.button(
                        "CANCELAR",
                        type="reset",
                        class_name="boton_cancelar",
                        on_click=AsignacionHorarios.cancelar
                    ),
                    rx.button(
                        "ACEPTAR", 
                        type="submit",
                        class_name="boton_aceptar"
                    ),
                ),
                class_name="contenedor_botones"
            ),
        ),
        on_submit=AsignacionHorarios.aceptar_reserva
    )

# rx.dialog.root(
#              rx.dialog.content(
#                 rx.box(
#                 reservar_salon(),
#                 width="100%",  # Asegura que el contenido use todo el espacio disponible
#                 ),
#                 style={
#                     "background": "transparent",
#                     "box_shadow": "none",
#                     "max_width": "900px",  # Ajusta este valor según necesites
#                     "width": "100%",  # Usa un porcentaje para responsividad
#                     #"margin": "auto",  # Centra el diálogo
#                 },
#              ),
#              open=AsignacionHorarios.mostrar_formulario,
#          ),