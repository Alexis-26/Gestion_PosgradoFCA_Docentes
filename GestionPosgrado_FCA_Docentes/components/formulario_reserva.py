from ..state import AsignacionHorarios, Tabla_ConsultaHorarios
from ..styles.colors import Colors
import reflex as rx

def form_reservar():
    return rx.box(
        rx.tablet_and_desktop(
            rx.hstack(
                # Es la parte verde del formulario
                rx.flex(
                    rx.vstack(
                        rx.image(src="/escudo_uabc.png", width="100px"),
                        rx.heading("RESERVANDO", color="#FFFFFF"),
                        rx.heading(AsignacionHorarios.salon_abierto, color="#FFFFFF"),
                        rx.icon("calendar", size=60, color="#FFFFFF"),
                        align="center"
                    ),
                    # width="100%",
                    # height="100%",
                    width="200px",
                    height="500px",
                    background=Colors.PRIMARY_GREEN.value,
                    align="center",
                    justify="center",
                    border_radius="20px"
                ),
                # Es la parte del fomulario
                rx.vstack(
                    rx.form(
                        rx.hstack(
                            rx.vstack(
                                rx.text("Numero de Empleado"),
                                rx.input(                               # Aqui esta el input de NUMERO DE EMPLEADO
                                    placeholder="Número de Empleado",
                                    name="numero_empleado",
                                    required=True,
                                    disabled=True,
                                    variant="surface",
                                    color_scheme="green",
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Nombre del Docente"),
                                rx.input(                       # Aqui esta el input de NUMERO DEL MAESTRO
                                    placeholder="Nombre del Docente", 
                                    name="nombre_maestro",
                                    required=True,
                                    disabled=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="400px"
                                ),
                                spacing="0"
                            ),
                            width="100%",
                            margin_top="20px"
                        ),
                        rx.hstack(
                            rx.vstack(
                                rx.text("Clave Materia"),
                                rx.input(                        # Aqui esta el input CLAVE MATERIA
                                    placeholder="Clave de Materia",
                                    name="clave_materia", 
                                    required=True,
                                    variant="surface",
                                    color_scheme="green"
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Nombre de Materia"),
                                rx.input(                         # Aqui esta el input de NOMBRE DE LA MATERIA 
                                    placeholder="Nombre de la materia",
                                    name="nombre_materia",
                                    required=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="400px"
                                ),
                                spacing="0"
                            ),
                            width="100%",
                            margin_top="20px"
                        ),
                        rx.hstack(
                            rx.vstack(
                                rx.text("Grupo"),
                                rx.input(            # Aqui esta el input de GRUPO
                                    placeholder="Grupo",
                                    name="grupo",
                                    required=True,
                                    variant="surface",
                                    color_scheme="green"
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Fecha"),
                                rx.input(                     # Aqui esta el input DE FECHA DE INICIO 
                                    type="date",
                                    name="fecha_inicio",
                                    required=True,
                                    min=AsignacionHorarios.min_date,
                                    variant="surface",
                                    color_scheme="green",
                                    on_change=AsignacionHorarios.toggle_select_horas
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Selección de Hora(s)"),
                                rx.menu.root(
                                    rx.menu.trigger(
                                        rx.button("Horario", 
                                                  color_scheme="gray", 
                                                  variant="outline", 
                                                  high_contrast=True, 
                                                  type="button", 
                                                  #disabled=AsignacionHorarios.select_horario, 
                                                  #on_click=AsignacionHorarios.component_menu_horas("")
                                                  ),
                                    ),
                                    rx.menu.content(
                                        rx.vstack(
                                            rx.foreach(
                                                AsignacionHorarios.checkbox_hrs, # Genera un checkbox por cada hora en el diccionario
                                                lambda hora: rx.checkbox(
                                                hora[0], # [0] es la key
                                                checked=hora[1][0], # [1] es el valor
                                                on_change=lambda val: AsignacionHorarios.hrs_seleccionadas(val, hora[0]),
                                                color_scheme="green",
                                                disabled=hora[1][1] # [1] es el valor
                                                )
                                            ),
                                            overflow_y="auto",
                                            max_height="210px"
                                        ),
                                        side="bottom",
                                        size="1",
                                        #modal=False,
                                    ),
                                    open=AsignacionHorarios.menu_desktop,  # Controla el estado del menú
                                    on_open_change=AsignacionHorarios.component_menu_horas_desktop  # Handle open/close state
                                ),
                                spacing="0"
                            ),
                            width="100%",
                            margin_top="20px"
                        ),
                        rx.hstack(
                            rx.vstack(
                                rx.checkbox(text="Horario Fijo", name="horario_fijo", size="3", value="fijo", color_scheme="green", on_change=AsignacionHorarios.toggle_fecha_fin),
                            ),
                            rx.vstack(
                                rx.text("Fecha de Finalización"), 
                                rx.input(                   # Aqui esta el input DE FECHA DE FIN 
                                    type="date",
                                    disabled=AsignacionHorarios.fecha_fin_habilitado,
                                    name="fecha_fin",
                                    min=AsignacionHorarios.min_date,
                                    variant="surface",
                                    color_scheme="green"
                                ),
                                spacing="0",
                                margin_left="10px"
                            ),
                            width="100%",
                            margin_top="20px",
                            spacing="9"
                        ),
                        rx.hstack(
                            rx.button(
                                "CANCELAR",
                                color_scheme="red",
                                variant="solid",
                                on_click=AsignacionHorarios.cancelar
                            ),
                            rx.button(
                                "ACEPTAR",
                                background_color="#00723F", 
                                type="submit",
                            ),
                            width="100%",
                            margin_top="80px",
                            justify="center"
                        ),
                        on_submit=AsignacionHorarios.aceptar_reserva
                    ),
                    #background="red",
                    width="70%",
                    height="500px",
                ),
            ),  
        ),
        rx.mobile_only(
            rx.vstack(
                # Es la parte verde del formulario
                rx.flex(
                    rx.hstack(
                        rx.image(src="/escudo_uabc.png", width="50px"),
                        rx.heading("RESERVANDO", color="#FFFFFF"),
                        rx.heading(AsignacionHorarios.salon_abierto, color="#FFFFFF"),
                        rx.icon("calendar", size=30, color="#FFFFFF"),
                        align="center"
                    ),
                    width="100%",
                    # height="100%",
                    height="100px",
                    background=Colors.PRIMARY_GREEN.value,
                    align="center",
                    justify="center",
                    border_radius="20px"
                ),
                rx.vstack(
                    rx.form(
                        rx.vstack(
                            rx.vstack(
                                rx.text("Numero de Empleado"),
                                rx.input(                               # Aqui esta el input de NUMERO DE EMPLEADO
                                    placeholder="Número de Empleado",
                                    name="numero_empleado",
                                    required=True,
                                    disabled=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="300px"
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Nombre del Docente"),
                                rx.input(                       # Aqui esta el input de NUMERO DEL MAESTRO
                                    placeholder="Nombre del Docente", 
                                    name="nombre_maestro",
                                    required=True,
                                    disabled=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="300px"
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Clave Materia"),
                                rx.input(                        # Aqui esta el input CLAVE MATERIA
                                    placeholder="Clave de Materia",
                                    name="clave_materia", 
                                    required=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="300px"
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Nombre de Materia"),
                                rx.input(                         # Aqui esta el input de NOMBRE DE LA MATERIA 
                                    placeholder="Nombre de la materia",
                                    name="nombre_materia",
                                    required=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="300px"
                                ),
                                spacing="0"
                            ),
                            rx.hstack(
                                rx.vstack(
                                    rx.text("Grupo"),
                                    rx.input(            # Aqui esta el input de GRUPO
                                        placeholder="Grupo",
                                        name="grupo",
                                        required=True,
                                        variant="surface",
                                        color_scheme="green"
                                    ),
                                    spacing="0"
                                ),
                                rx.vstack(
                                    rx.text("Fecha"),
                                    rx.input(                     # Aqui esta el input DE FECHA DE INICIO 
                                        type="date",
                                        name="fecha_inicio",
                                        required=True,
                                        min=AsignacionHorarios.min_date,
                                        variant="surface",
                                        color_scheme="green",
                                        on_change=AsignacionHorarios.toggle_select_horas
                                    ),
                                    spacing="0"
                                ),
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Selección de Hora(s)"),
                                rx.menu.root(
                                    rx.menu.trigger(
                                        rx.button("Horario", 
                                                  color_scheme="gray", 
                                                  variant="outline", 
                                                  high_contrast=True, 
                                                  type="button", 
                                                  #disabled=AsignacionHorarios.select_horario, 
                                                  #on_click=AsignacionHorarios.component_menu_horas(False), width="300px"
                                                ),
                                    ),
                                    rx.menu.content(
                                        rx.vstack(
                                            rx.foreach(
                                                AsignacionHorarios.checkbox_hrs, # Genera un checkbox por cada hora en el diccionario
                                                lambda hora: rx.checkbox(
                                                hora[0], # [0] es la key
                                                checked=hora[1][0], # [1] es el valor
                                                on_change=lambda val: AsignacionHorarios.hrs_seleccionadas(val, hora[0]),
                                                color_scheme="green",
                                                disabled=hora[1][1] # [1] es el valor
                                                )
                                            ),
                                            overflow_y="auto",
                                            max_height="210px",
                                        ),
                                        side="top",
                                        size="1",
                                        width="300px"
                                        #modal=False,
                                    ),
                                    open=AsignacionHorarios.menu_mobile,  # Controla el estado del menú
                                    on_open_change=AsignacionHorarios.component_menu_horas_mobile,  # Handle open/close state
                                ),
                                spacing="0"
                            ),
                            rx.hstack(
                                rx.vstack(
                                    rx.checkbox(text="Horario Fijo", name="horario_fijo", size="3", value="fijo", color_scheme="green", on_change=AsignacionHorarios.toggle_fecha_fin),
                                ),
                                rx.vstack(
                                    rx.text("Fecha de Finalización"), 
                                    rx.input(                   # Aqui esta el input DE FECHA DE FIN 
                                        type="date",
                                        disabled=AsignacionHorarios.fecha_fin_habilitado,
                                        name="fecha_fin",
                                        min=AsignacionHorarios.min_date,
                                        variant="surface",
                                        color_scheme="green"
                                    ),
                                    spacing="0",
                                    margin_left="10px"
                                ),
                                width="100%",
                                #margin_top="20px",
                                spacing="9"
                            ),
                            rx.hstack(
                                rx.button(
                                    "CANCELAR",
                                    color_scheme="red",
                                    variant="solid",
                                    on_click=AsignacionHorarios.cancelar
                                ),
                                rx.button(
                                    "ACEPTAR",
                                    background_color="#00723F", 
                                    type="submit",
                                ),
                                width="100%",
                                margin_top="20px",
                                justify="center"
                            ),
                            width="100%",
                            #margin_top="20px"
                        ),
                        width="100%",
                        padding_left="20px",
                        padding_right="20px",
                    ),
                    #background="red",
                    width="100%",
                    height="550px",
                ),
                width="350px",
            ),
        ),
        background="#FFFFFF",
        width="100%",
        height="100%",
        border_radius="20px"
    )