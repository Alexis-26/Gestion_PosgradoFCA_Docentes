from ..styles.colors import Colors
import reflex as rx

def simbologia_colores():
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.avatar(background=Colors.SECONDARY_GREEN.value),
                    rx.text("Libre"),
                    align="center"
                ),
                rx.hstack(
                    rx.avatar(background=Colors.RED.value),
                    rx.text("Reservado"),
                    align="center"
                ),
                rx.hstack(
                    rx.avatar(background=Colors.BLACK.value),
                    rx.text("Reserva Fija"),
                    align="center"
                ),
            )
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.avatar(background=Colors.SECONDARY_GREEN.value, size="1"),
                    rx.text("Libre"),
                    align="center"
                ),
                rx.hstack(
                    rx.avatar(background=Colors.RED.value, size="1"),
                    rx.text("Reservado"),
                    align="center"
                ),
                rx.hstack(
                    rx.avatar(background=Colors.BLACK.value, size="1"),
                    rx.text("Reserva Fija"),
                    align="center"
                ),
            )
        ),
    )