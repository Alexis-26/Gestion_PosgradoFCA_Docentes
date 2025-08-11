from enum import Enum
import reflex as rx

class FontSize(Enum):
    LITTLE = "9px"
    EXTRA_SMALL = "11px"
    SMALL = "14px",
    MEDIUM = "24px",
    LARGE = "36px",
    EXTRA_LARGE = "48px"

# Los breakpoints por defecto en Reflex son:

# initial: 0px (móvil)
# xs: 30em (móvil grande)
# sm: 48em (tablet)
# md: 62em (desktop pequeño)
# lg: 80em (desktop)
# xl: 96em (pantallas grandes)