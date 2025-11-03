from ..state import AsignacionHorarios, Tabla_ConsultaHorarios, InicioSesion
from ..styles.colors import Colors
from ..styles.utils import Imagenes
import reflex as rx

def form_reservar():
    return rx.box(
        rx.tablet_and_desktop(
            rx.hstack(
                # Es la parte verde del formulario
                rx.flex(
                    rx.vstack(
                        rx.image(src=Imagenes.LOGO_UABC_FCA.value, width="180px"),
                        rx.heading("RESERVANDO", color="#FFFFFF"),
                        rx.heading(AsignacionHorarios.salon_abierto, color="#FFFFFF"),
                        rx.icon("calendar", size=60, color="#FFFFFF"),
                        align="center"
                    ),
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
                                    value=InicioSesion.no_empleado_activo,
                                    read_only=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="160px"
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Nombre del Docente"),
                                rx.input(                       # Aqui esta el input de NUMERO DEL MAESTRO
                                    placeholder="Nombre del Docente", 
                                    name="nombre_maestro",
                                    required=True,
                                    value=InicioSesion.nombre_docente,
                                    read_only=True,
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
                                rx.select(       
                                    AsignacionHorarios.opciones_clave,                 # Aqui esta el input CLAVE MATERIA
                                    value=AsignacionHorarios.clave_seleccionado,
                                    placeholder="Clave de Materia",
                                    name="clave_materia", 
                                    required=True,
                                    position="popper",
                                    variant="surface",
                                    color_scheme="green",
                                    width="160px",
                                    on_change=AsignacionHorarios.set_clave
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Nombre de Materia"),
                                rx.select(                         # Aqui esta el input de NOMBRE DE LA MATERIA 
                                    AsignacionHorarios.opciones_cursos,
                                    value=AsignacionHorarios.curso_seleccionado,
                                    placeholder="Nombre de la materia",
                                    name="nombre_materia",
                                    required=True,
                                    position="popper",
                                    variant="surface",
                                    color_scheme="green",
                                    width="400px",
                                    on_change=AsignacionHorarios.set_curso
                                ),
                                spacing="0"
                            ),
                            width="100%",
                            margin_top="20px"
                        ),
                        rx.hstack(
                            rx.vstack(
                                rx.text("Grupo"),
                                rx.select(            # Aqui esta el input de GRUPO
                                    AsignacionHorarios.opciones_grupos,
                                    placeholder="Grupo",
                                    name="grupo",
                                    required=True,
                                    variant="surface",
                                    position="popper",
                                    color_scheme="green",
                                    width="160px",
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
                            rx.button(
                                "CANCELAR",
                                color_scheme="red",
                                variant="solid",
                                type="button",
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
                        rx.heading("RESERVANDO", color="#FFFFFF"),
                        rx.heading(AsignacionHorarios.salon_abierto, color="#FFFFFF"),
                        rx.icon("calendar", size=30, color="#FFFFFF"),
                        align="center"
                    ),
                    width="100%",
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
                                    value=InicioSesion.no_empleado_activo,
                                    read_only=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="280px"
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Nombre del Docente"),
                                rx.input(                       # Aqui esta el input de NUMERO DEL MAESTRO
                                    placeholder="Nombre del Docente", 
                                    name="nombre_maestro",
                                    required=True,
                                    value=InicioSesion.nombre_docente,
                                    read_only=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="280px"
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Clave Materia"),
                                rx.select(       
                                    AsignacionHorarios.opciones_clave,                 # Aqui esta el input CLAVE MATERIA
                                    value=AsignacionHorarios.clave_seleccionado,
                                    placeholder="Clave de Materia",
                                    name="clave_materia", 
                                    required=True,
                                    position="popper",
                                    variant="surface",
                                    color_scheme="green",
                                    width="280px",
                                    on_change=AsignacionHorarios.set_clave
                                ),
                                spacing="0"
                            ),
                            rx.vstack(
                                rx.text("Nombre de Materia"),
                                rx.select(                         # Aqui esta el input de NOMBRE DE LA MATERIA 
                                    AsignacionHorarios.opciones_cursos,
                                    value=AsignacionHorarios.curso_seleccionado,
                                    placeholder="Nombre de la materia",
                                    name="nombre_materia",
                                    required=True,
                                    variant="surface",
                                    position="popper",
                                    color_scheme="green",
                                    width="280px",
                                    on_change=AsignacionHorarios.set_curso
                                ),
                                spacing="0"
                            ),
                            rx.hstack(
                                rx.vstack(
                                    rx.text("Grupo"),
                                    rx.select(            # Aqui esta el input de GRUPO
                                        AsignacionHorarios.opciones_grupos,
                                        placeholder="Grupo",
                                        name="grupo",
                                        required=True,
                                        position="popper",
                                        variant="surface",
                                        color_scheme="green",
                                        width="100px",
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
                                                  width="160px" 
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
                                        width="160px"
                                        #modal=False,
                                    ),
                                    open=AsignacionHorarios.menu_mobile,  # Controla el estado del menú
                                    on_open_change=AsignacionHorarios.component_menu_horas_mobile,  # Handle open/close state
                                ),
                                spacing="0",
                                width="100%",
                                align="center"
                            ),
                            rx.hstack(
                                rx.button(
                                    "CANCELAR",
                                    color_scheme="red",
                                    variant="solid",
                                    type="button",
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
                        ),
                        width="100%",
                        padding_left="20px",
                        padding_right="20px",
                        on_submit=AsignacionHorarios.aceptar_reserva
                    ),
                    width="100%",
                    height="550px",
                ),
                width="310px",
                align="center"
            ),
        ),
        background="#FFFFFF",
        width="100%",
        height="100%",
        border_radius="20px"
    )