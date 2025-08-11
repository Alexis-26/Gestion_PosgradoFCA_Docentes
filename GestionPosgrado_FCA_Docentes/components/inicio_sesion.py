from ..state import Login
from ..styles.utils import Imagenes
import reflex as rx

def inicion_sesion_desktop():
    return rx.box(
        rx.flex(
            rx.box(
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.image(src=Imagenes.LOGO.value, width="100px",),
                            rx.heading("INICIO DE SESIÓN", color="#FFFFFF"),
                            rx.form(
                                rx.flex(
                                    rx.vstack(
                                        rx.text("Número de empleado", weight="bold", color="#FFFFFF"),
                                        rx.input(
                                            rx.input.slot(rx.icon("user")),
                                            placeholder="Número de empleado",
                                            name="no_empleado",
                                            width="100%",
                                            height="40px"
                                        ),
                                        rx.text("Contraseña", weight="bold", color="#FFFFFF", margin_top="20px"),
                                        rx.input(
                                            rx.input.slot(rx.icon("lock")),
                                            placeholder="Contraseña",
                                            name="password",
                                            type="password",
                                            width="100%",
                                            height="40px"
                                        ),
                                        rx.button("INGRESAR", type="submit", width="100%", background="#DFAC0F", margin_top="20px", size="3"),
                                        # background="red",
                                        width="70%",
                                        height="300px",
                                        spacing="1",
                                        #align="center"
                                    ),
                                    align="center",
                                    justify="center",
                                    width="100%",
                                    height="100%",
                                ),
                                on_submit=Login.login_form
                            ),
                            width="100%",
                            height="100%",
                            align="center",
                            justify="center",
                            spacing="4"
                        ),
                        width="30%",
                        height="90%",
                        background="rgba(0, 114, 63, 0.86)",
                        border_radius="24px",
                        box_shadow="0px 4px 10px rgba(0, 0, 0, 0.1)"
                    ),
                    width="100%",
                    height="100%",
                    justify="center",
                    align="center"
                ),
                background="radial-gradient(circle, rgba(135, 183, 142, 0.7), rgba(0, 114, 63, 0.7))",
                width="90vw",
                height="90vh",
                border_radius="24px"
            ),
            width="100%",
            height="100%",
            justify="center",
            align="center"
        ),
        background=f"url({Imagenes.FONDO_INICIO_SESION.value}) center/cover no-repeat",
        width="100vw",
        height="100vh",
    )

def inicion_sesion_mobile():
    return rx.box(
        rx.flex(
            rx.box(
                rx.flex(
                    rx.box(
                        rx.vstack(
                            rx.image(src=Imagenes.LOGO.value, width="100px", margin_top="40px"),
                            rx.heading("INICIO DE SESION", color="#FFFFFF"),
                            rx.form(
                                rx.flex(
                                    rx.vstack(
                                        rx.text("Número de empleado", weight="bold", color="#FFFFFF"),
                                        rx.input(
                                            placeholder="Número de empleado",
                                            name="no_empleado",
                                            width="100%"
                                        ),
                                        rx.text("Contraseña", weight="bold", color="#FFFFFF", margin_top="20px"),
                                        rx.input(
                                            placeholder="Contraseña",
                                            name="password",
                                            type="password",
                                            width="100%"
                                        ),
                                        rx.button("INGRESAR", type="submit", width="100%", margin_top="40px", background="#DFAC0F"),
                                        # background="red",
                                        width="70%",
                                        height="300px",
                                        spacing="1",
                                        #align="center"
                                    ),
                                    align="center",
                                    justify="center",
                                    width="100%",
                                    height="100%",
                                ),
                                on_submit=Login.login_form
                            ),
                            width="100%",
                            height="100%",
                            align="center",
                            spacing="4"
                        ),
                        width="80%",
                        height="80%",
                        background="rgba(0, 114, 63, 0.86)",
                        border_radius="24px",
                        box_shadow="0px 4px 10px rgba(0, 0, 0, 0.1)"
                    ),
                    width="100%",
                    height="100%",
                    justify="center",
                    align="center"
                ),
                background="radial-gradient(circle, rgba(135, 183, 142, 0.7), rgba(0, 114, 63, 0.7))",
                width="90vw",
                height="90vh",
                border_radius="24px"
            ),
            width="100%",
            height="100%",
            justify="center",
            align="center"
        ),
        background=f"url({Imagenes.FONDO_INICIO_SESION.value}) center/cover no-repeat",
        width="100vw",
        height="100vh",
    )