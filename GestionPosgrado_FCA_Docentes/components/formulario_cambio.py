from ..styles.colors import Colors
from ..styles.utils import Imagenes
from ..state import FormCambio
import reflex as rx

def form_cambio():
    return rx.box(
        rx.tablet_and_desktop(
            rx.vstack(
                # Es la parte verde del formulario
                rx.flex(
                    rx.hstack(
                        rx.heading("CAMBIO DE CONTRASEÑA", color="#FFFFFF"),
                        align="center"
                    ),
                    width="100%",
                    height="100px",
                    background=Colors.PRIMARY_GREEN.value,
                    align="center",
                    justify="center",
                    border_radius="20px"
                ),
                # Es la parte del fomulario
                rx.vstack(
                    rx.form(
                        rx.vstack(
                            rx.vstack(
                                rx.text("Nueva Contraseña"),
                                rx.input(                               # Aqui esta el input de NUMERO DE EMPLEADO
                                    placeholder="Nueva Contraseña",
                                    name="nueva_contraseña",
                                    required=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="100%"
                                    
                                ),
                                spacing="0",
                                width="100%"
                            ),
                            rx.vstack(
                                rx.text("Confirmar Contraseña"),
                                rx.input(                       # Aqui esta el input de NUMERO DEL MAESTRO
                                    placeholder="Confirmar Contraseña", 
                                    name="confirmar_contraseña",
                                    required=True,
                                    #disabled=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="100%"
                                ),
                                spacing="0",
                                width="100%"
                            ),
                            width="100%",
                        ),
                        rx.hstack(
                            rx.button(
                                "CANCELAR",
                                color_scheme="red",
                                variant="solid",
                                type="button",
                                on_click=FormCambio.cancelar
                            ),
                            rx.button(
                                "ACEPTAR",
                                background_color="#00723F", 
                                type="submit",
                            ),
                            width="100%",
                            margin_top="40px",
                            justify="center"
                        ),
                        on_submit=FormCambio.aceptar_cambio,
                        width="100%",
                        padding_left="20px",
                        padding_right="20px",
                    ),
                    width="100%",
                    height="240px",
                ),
            ),  
        ),
        rx.mobile_only(
            rx.vstack(
                # Es la parte verde del formulario
                rx.flex(
                    rx.hstack(
                        rx.heading("CAMBIO DE CONTRASEÑA", color="#FFFFFF", font_size="20px"),
                        align="center"
                    ),
                    width="100%",
                    height="100px",
                    background=Colors.PRIMARY_GREEN.value,
                    align="center",
                    justify="center",
                    border_radius="20px"
                ),
                # Es la parte del fomulario
                rx.vstack(
                    rx.form(
                        rx.vstack(
                            rx.vstack(
                                rx.text("Nueva Contraseña"),
                                rx.input(                               # Aqui esta el input de NUMERO DE EMPLEADO
                                    placeholder="Nueva Contraseña",
                                    name="nueva_contraseña",
                                    required=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="100%"
                                    
                                ),
                                spacing="0",
                                width="100%"
                            ),
                            rx.vstack(
                                rx.text("Confirmar Contraseña"),
                                rx.input(                       # Aqui esta el input de NUMERO DEL MAESTRO
                                    placeholder="Confirmar Contraseña", 
                                    name="confirmar_contraseña",
                                    required=True,
                                    variant="surface",
                                    color_scheme="green",
                                    width="100%"
                                ),
                                spacing="0",
                                width="100%"
                            ),
                            width="100%",
                        ),
                        rx.hstack(
                            rx.button(
                                "CANCELAR",
                                color_scheme="red",
                                variant="solid",
                                type="button",
                                on_click=FormCambio.cancelar
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
                        on_submit=FormCambio.aceptar_cambio,
                        width="100%",
                        padding_left="20px",
                        padding_right="20px",
                    ),
                    width="100%",
                    height="300px",
                ),
            ),  
        ),
        
        background="#FFFFFF",
        width="100%",
        height="100%",
        border_radius="20px"
    )