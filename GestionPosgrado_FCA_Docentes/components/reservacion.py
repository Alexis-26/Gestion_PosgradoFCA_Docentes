import reflex as rx
#from ..components.reservar_cursos import reservar  # Importa la función que contiene el formulario
from ..state import AsignacionHorarios, Tabla_ConsultaHorarios
#from..components.select_horas import seleccion_horas, si

def reservar_salon():
    return rx.box(
        # Contenedor general
            # Cuadro verde (lado izquierdo)
            rx.box(
                rx.box(
                    rx.text("RESERVANDO", class_name="titulo_reserva"),
                ),
                #rx.text(AsignacionHorarios.salon, class_name="titulo_cuadro_verde"),
                rx.box(
                    rx.text(AsignacionHorarios.salon, class_name="titulo_reserva"),
                ),
                rx.box(
                    rx.image(src="/images/Icono_reservar.png", class_name="icono_form_calendario"), # Pendiente de dar tamaño al icono
                ),
                class_name="cuadro_verde",
            ),
            # Contenedor de inputs (lado derecho)
            rx.box(
                rx.form(
                    rx.box(
                        rx.text("Número de Empleado", class_name="subtitulos_form_apartar"),
                        rx.input(                               # Aqui esta el input de NUMERO DE EMPLEADO
                            placeholder="Número de Empleado",
                            name="numero_empleado",
                            required=True,
                            variant="surface",
                            color_scheme="green",
                        ),
                        class_name="info_num_empleado"
                    ),
                    rx.box(
                        rx.text("Nombre del Docente", class_name="subtitulos_form_apartar"),
                        rx.input(                       # Aqui esta el input de NUMERO DEL MAESTRO
                            placeholder="Nombre del Docente", 
                            name="nombre_maestro",
                            required=True,
                            variant="surface",
                            color_scheme="green"
                        ),
                        class_name="info_docente"
                    ),
                    rx.box(
                        rx.text("Clave Materia", class_name="subtitulos_form_apartar"),
                        rx.input(                        # Aqui esta el input CLAVE MATERIA
                            placeholder="Clave de Materia",
                            name="clave_materia", 
                            required=True,
                            variant="surface",
                            color_scheme="green"
                        ),
                        class_name="info_cve_materia",
                    ),
                    rx.box(
                        rx.text("Nombre de Materia", class_name="subtitulos_form_apartar"),
                        rx.input(                         # Aqui esta el input de NOMBRE DE LA MATERIA 
                            placeholder="Nombre de la materia",
                            name="nombre_materia",
                            required=True,
                            variant="surface",
                            color_scheme="green"
                        ),
                        class_name="info_materia",
                    ),
                    rx.box(
                        rx.text("Grupo", class_name="subtitulos_form_apartar"),
                        rx.input(            # Aqui esta el input de GRUPO
                            placeholder="Grupo",
                            name="grupo",
                            required=True,
                            variant="surface",
                            color_scheme="green"
                        ),
                        class_name="info_grupo",
                    ),
                    rx.box(
                        rx.text("Fecha", class_name="subtitulos_form_apartar"),
                        rx.input(                     # Aqui esta el input DE FECHA DE INICIO 
                            type="date",
                            name="fecha_inicio",
                            required=True,
                            min=AsignacionHorarios.min_date,
                            variant="surface",
                            color_scheme="green",
                            on_change=AsignacionHorarios.toggle_select_horas
                        ),
                         class_name="info_fecha",
                    ),
                    rx.box(
                        rx.text("Selección de Hora(s)", class_name="subtitulos_form_apartar"),
                        rx.menu.root(
                            rx.menu.trigger(
                                rx.button("Horario", color_scheme="gray", variant="outline", high_contrast=True, type="button", disabled=AsignacionHorarios.select_horario, on_click=AsignacionHorarios.component_menu_horas("")),
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
                            open=AsignacionHorarios.menu,  # Controla el estado del menú
                            on_open_change=AsignacionHorarios.component_menu_horas  # Handle open/close state
                        ),
                        class_name="info_horas"
                    ),
                    rx.box(
                        rx.checkbox(text="Horario Fijo", name="horario_fijo", size="3", value="fijo", color_scheme="green", on_change=AsignacionHorarios.toggle_fecha_fin),
                        class_name="info_horario_fijo"
                    ),
                    rx.box(
                        rx.text("Fecha de Finalización", class_name="subtitulos_form_apartar"), 
                        rx.input(                   # Aqui esta el input DE FECHA DE FIN 
                            type="date",
                            disabled=AsignacionHorarios.fecha_fin_habilitado,
                            name="fecha_fin",
                            min=AsignacionHorarios.min_date,
                            variant="surface",
                            color_scheme="green"
                        ),
                        class_name="info_fecha_termino",
                    ),
                    rx.box(
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
                        class_name="info_reserva_botones",
                    ),
                    class_name="form_elementos_reserva",
                    on_submit=AsignacionHorarios.aceptar_reserva
                ),
                class_name="form_reserva_base",
            ),
            class_name="base_form_reserva",
        ),

def reservar_salon_editar():
    return rx.box(
        # Contenedor general
            # Cuadro verde (lado izquierdo)
            rx.box(
                rx.box(
                    rx.text("Editando", class_name="titulo_reserva"),
                ),
                #rx.text(AsignacionHorarios.salon, class_name="titulo_cuadro_verde"),
                rx.box(
                    rx.text(Tabla_ConsultaHorarios.lista_informacion_reserva[0], class_name="titulo_reserva"),
                ),
                rx.box(
                    rx.image(src="/images/Icono_reservar.png", class_name="icono_form_calendario"), # Pendiente de dar tamaño al icono
                ),
                class_name="cuadro_verde",
            ),
            # Contenedor de inputs (lado derecho)
            rx.box(
                rx.form(
                    rx.box(
                        rx.text("Número de Empleado", class_name="subtitulos_form_apartar"),
                        rx.input(                               # Aqui esta el input de NUMERO DE EMPLEADO
                            placeholder="Número de Empleado",
                            name="numero_empleado",
                            default_value=Tabla_ConsultaHorarios.lista_informacion_reserva[1],
                            required=True,
                            variant="surface",
                            color_scheme="green",
                        ),
                        class_name="info_num_empleado"
                    ),
                    rx.box(
                        rx.text("Nombre del Docente", class_name="subtitulos_form_apartar"),
                        rx.input(                       # Aqui esta el input de NUMERO DEL MAESTRO
                            placeholder="Nombre del Docente", 
                            name="nombre_maestro",
                            default_value=Tabla_ConsultaHorarios.lista_informacion_reserva[2],
                            required=True,
                            variant="surface",
                            color_scheme="green"
                        ),
                        class_name="info_docente"
                    ),
                    rx.box(
                        rx.text("Clave Materia", class_name="subtitulos_form_apartar"),
                        rx.input(                        # Aqui esta el input CLAVE MATERIA
                            placeholder="Clave de Materia",
                            name="clave_materia",
                            default_value=Tabla_ConsultaHorarios.lista_informacion_reserva[3], 
                            required=True,
                            variant="surface",
                            color_scheme="green"
                        ),
                        class_name="info_cve_materia",
                    ),
                    rx.box(
                        rx.text("Nombre de Materia", class_name="subtitulos_form_apartar"),
                        rx.input(                         # Aqui esta el input de NOMBRE DE LA MATERIA 
                            placeholder="Nombre de la materia",
                            name="nombre_materia",
                            default_value=Tabla_ConsultaHorarios.lista_informacion_reserva[4],
                            required=True,
                            variant="surface",
                            color_scheme="green"
                        ),
                        class_name="info_materia",
                    ),
                    rx.box(
                        rx.text("Grupo", class_name="subtitulos_form_apartar"),
                        rx.input(            # Aqui esta el input de GRUPO
                            placeholder="Grupo",
                            name="grupo",
                            default_value=Tabla_ConsultaHorarios.lista_informacion_reserva[5],
                            required=True,
                            variant="surface",
                            color_scheme="green"
                        ),
                        class_name="info_grupo",
                    ),
                    rx.box(
                        rx.text("Fecha", class_name="subtitulos_form_apartar"),
                        rx.input(                     # Aqui esta el input DE FECHA DE INICIO 
                            type="date",
                            name="fecha_inicio",
                            default_value=Tabla_ConsultaHorarios.lista_informacion_reserva[6],
                            required=True,
                            min=AsignacionHorarios.min_date,
                            variant="surface",
                            color_scheme="green",
                            auto_focus=True,
                            on_blur=Tabla_ConsultaHorarios.toggle_select_horas
                        ),
                        class_name="info_fecha",
                    ),
                    rx.box(
                        rx.text("Selección de Hora(s)", class_name="subtitulos_form_apartar"),
                        rx.menu.root(
                            rx.menu.trigger(
                                rx.button("Horario", color_scheme="gray", variant="outline", high_contrast=True, type="button", disabled=Tabla_ConsultaHorarios.select_horario, on_click=Tabla_ConsultaHorarios.component_menu_horas("")),
                            ),
                            rx.menu.content(
                                rx.vstack(
                                    rx.foreach(
                                        Tabla_ConsultaHorarios.checkbox_hrs, # Genera un checkbox por cada hora en el diccionario
                                        lambda hora: rx.checkbox(
                                        hora[0], # [0] es la key
                                        checked=hora[1][0], # [1] es el valor
                                        on_change=lambda val: Tabla_ConsultaHorarios.hrs_seleccionadas(val, hora[0]),
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
                            open=Tabla_ConsultaHorarios.menu,  # Controla el estado del menú
                            on_open_change=Tabla_ConsultaHorarios.component_menu_horas  # Handle open/close state
                        ),
                        class_name="info_horas"
                    ),
                    rx.box(
                        rx.checkbox(text="Horario Fijo", name="horario_fijo", size="3", value="fijo", color_scheme="green", checked=Tabla_ConsultaHorarios.hora_fijo_checked, on_change=Tabla_ConsultaHorarios.toggle_fecha_fin),
                        class_name="info_horario_fijo"
                    ),
                    rx.box(
                        rx.text("Fecha de Finalización", class_name="subtitulos_form_apartar"), 
                        rx.input(                   # Aqui esta el input DE FECHA DE FIN 
                            type="date",
                            disabled=Tabla_ConsultaHorarios.fecha_fin_habilitado,
                            name="fecha_fin",
                            default_value=Tabla_ConsultaHorarios.lista_informacion_reserva[7],
                            min=AsignacionHorarios.min_date,
                            variant="surface",
                            color_scheme="green"
                        ),
                        class_name="info_fecha_termino",
                    ),
                    rx.box(
                        rx.button(
                            "CANCELAR",
                            color_scheme="red",
                            variant="solid",
                            on_click=Tabla_ConsultaHorarios.cancelar,
                            type="button",
                        ),
                        rx.button(
                            "ACTUALIZAR",
                            background_color="#00723F", 
                            type="submit",
                        ),
                        class_name="info_reserva_botones",
                    ),
                    class_name="form_elementos_reserva",
                    on_submit=Tabla_ConsultaHorarios.actualizar_reserva
                ),
                class_name="form_reserva_base",
            ),
            class_name="base_form_reserva",
        ),