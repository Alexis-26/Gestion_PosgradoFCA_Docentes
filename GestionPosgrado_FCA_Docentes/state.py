from .model import MYSQLDB
from datetime import datetime
import reflex as rx
import pytz
import bcrypt

tz_bc = pytz.timezone("America/Tijuana")

def encriptado_password(password:str):
    bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash

def validacion_acceso(user_password:str, hash:str):
    user_password = user_password.encode("utf-8")
    password = hash.encode("utf-8")
    resultado = bcrypt.checkpw(user_password, password)
    return resultado

class InicioSesion(rx.State):
    _db:MYSQLDB = MYSQLDB()
    nombre_docente:str = ""
    no_empleado_activo:str = ""
    rol:str = ""
    is_authenticated:bool = False

    def login_form(self, form_data:dict):
        no_empleado = form_data.get("no_empleado")
        password = form_data.get("password")

        if not no_empleado or not password:
            return rx.toast.error("Campos vacíos", position="top-center")
        
        # Verificación en base de datos
        resultado = self._db.verificacion_usuario(no_empleado)
        if not resultado:
            return rx.toast.error("Número de empleado o contraseña incorrecta", position="top-center")
        
        hash, self.nombre_docente = resultado[0]

        if validacion_acceso(password, hash):
            # Autenticación del usuario dentro del sistema Reflex
            self.is_authenticated = True
            self.no_empleado_activo = no_empleado

            return [
                rx.toast.success("Bienvenido", position="top-center"),
                rx.redirect("/horarios")
            ]
            
        return rx.toast.error("Contraseña incorrecta", position="top-center")
    
    def verificacion_login(self):
        if not self.is_authenticated:
            return rx.redirect("/")
        
    def cerrar_sesion(self):
        # Cerrar la sesion Reflex automaticamente
        self.nombre_docente = ""
        self.no_empleado_activo = ""
        self.rol = ""
        self.is_authenticated = False
        return rx.redirect("/")

class ConsultaHorarios(rx.State):
    _db:MYSQLDB = MYSQLDB()
    lista_horarios: list[tuple] = []
    horas: list[str] = ["07:00", "08:00", "09:00", "10:00", "11:00",
                        "12:00", "13:00", "14:00", "15:00", "16:00",
                        "17:00", "18:00", "19:00", "20:00", "21:00",
                        ]
    grupos: list[str] = ["700", "710", "720", "721", "730", "731", 
                         "740", "741", "750", "751", "760", "761"]
    
    horario_dict_1: dict[str, list[tuple]] = {
    "07:00": [(), (), (), (), (), ()], "08:00": [(), (), (), (), (), ()], "09:00": [(), (), (), (), (), ()], "10:00": [(), (), (), (), (), ()],
    "11:00": [(), (), (), (), (), ()], "12:00": [(), (), (), (), (), ()], "13:00": [(), (), (), (), (), ()], "14:00": [(), (), (), (), (), ()],
    "15:00": [(), (), (), (), (), ()], "16:00": [(), (), (), (), (), ()], "17:00": [(), (), (), (), (), ()], "18:00": [(), (), (), (), (), ()],
    "19:00": [(), (), (), (), (), ()], "20:00": [(), (), (), (), (), ()], "21:00": [(), (), (), (), (), ()],
    }
    horario_dict_2: dict[str, list[tuple]] = {
    "07:00": [(), (), (), (), (), ()], "08:00": [(), (), (), (), (), ()], "09:00": [(), (), (), (), (), ()], "10:00": [(), (), (), (), (), ()],
    "11:00": [(), (), (), (), (), ()], "12:00": [(), (), (), (), (), ()], "13:00": [(), (), (), (), (), ()], "14:00": [(), (), (), (), (), ()],
    "15:00": [(), (), (), (), (), ()], "16:00": [(), (), (), (), (), ()], "17:00": [(), (), (), (), (), ()], "18:00": [(), (), (), (), (), ()],
    "19:00": [(), (), (), (), (), ()], "20:00": [(), (), (), (), (), ()], "21:00": [(), (), (), (), (), ()],
    }
    
    salones_informacion: dict[str, bool] = {"A":False, "B":False, "C":False, "D":False, "101":False, "102":False, "103":False, "104":False, "201":False, "202":False, "203":False, "204":False,}
    salones_primer_nivel: list[str] = ["A", "B", "101", "102", "103", "104", ]
    salones_segundo_nivel: list[str] = ["C", "D", "201", "202", "203", "204"]

    select_horas:str = ""
    fecha_seleccionada:str = ""
    grupo = ""

    @rx.var
    def fecha_hoy(self) -> str:
        return datetime.now(tz_bc).strftime("%Y-%m-%d")

    @rx.var
    def fecha_hoy_formato(self) -> str:
        return datetime.now(tz_bc).strftime("%d-%m-%Y")

    @rx.var
    def hora_actual(self) -> str:
        return f"{datetime.now(tz_bc).hour:02d}:00"
    
    def filter_fecha(self, fecha:str):
        self.lista_horarios = []
        if not fecha:
            return
        self.fecha_seleccionada = fecha
        self.salones_informacion = {"A":False, "B":False, "C":False, "D":False, "101":False, "102":False, "103":False, "104":False, "201":False, "202":False, "203":False, "204":False, }
        self.informacion_horarios()

    def filter_hora(self, hora:str):
        self.select_horas = hora
        self.salones_informacion = {"A":False, "B":False, "C":False, "D":False, "101":False, "102":False, "103":False, "104":False, "201":False, "202":False, "203":False, "204":False,}
        self.informacion_horarios()

    def filter_grupo(self, grupo:str):
        self.grupo = grupo
        self.informacion_horarios()

    def convertir_a_hora_str(self, td):
        horas = td.seconds // 3600
        minutos = (td.seconds % 3600) // 60
        return f"{horas:02d}:{minutos:02d}"
    
    def informacion_horarios(self):
        if self.fecha_seleccionada == "" and self.select_horas == "":
            self.fecha_seleccionada = self.fecha_hoy
            self.select_horas = self.hora_actual

        resultado = self._db.consulta_asignacion_fecha(self.fecha_seleccionada)
        self.horario_dict_1 = {
            "07:00": [(), (), (), (), (), ()], "08:00": [(), (), (), (), (), ()], "09:00": [(), (), (), (), (), ()], "10:00": [(), (), (), (), (), ()],
            "11:00": [(), (), (), (), (), ()], "12:00": [(), (), (), (), (), ()], "13:00": [(), (), (), (), (), ()], "14:00": [(), (), (), (), (), ()],
            "15:00": [(), (), (), (), (), ()], "16:00": [(), (), (), (), (), ()], "17:00": [(), (), (), (), (), ()], "18:00": [(), (), (), (), (), ()],
            "19:00": [(), (), (), (), (), ()], "20:00": [(), (), (), (), (), ()], "21:00": [(), (), (), (), (), ()],
            }
        self.horario_dict_2 = {
            "07:00": [(), (), (), (), (), ()], "08:00": [(), (), (), (), (), ()], "09:00": [(), (), (), (), (), ()], "10:00": [(), (), (), (), (), ()],
            "11:00": [(), (), (), (), (), ()], "12:00": [(), (), (), (), (), ()], "13:00": [(), (), (), (), (), ()], "14:00": [(), (), (), (), (), ()],
            "15:00": [(), (), (), (), (), ()], "16:00": [(), (), (), (), (), ()], "17:00": [(), (), (), (), (), ()], "18:00": [(), (), (), (), (), ()],
            "19:00": [(), (), (), (), (), ()], "20:00": [(), (), (), (), (), ()], "21:00": [(), (), (), (), (), ()],
            }
                        
        if resultado:
            self.lista_horarios = []
            
            if self.select_horas or self.fecha_seleccionada:
                res = [tuple(row) for row in resultado]
                
                # Procesar cada tupla y modificar el nombre
                horarios_procesados = []
                for r in res:
                    lista_r = list(r)  # Convertir la tupla a lista para modificar

                    nombres = r[1].split()  # Dividir el nombre completo
                    if len(nombres) >= 2:
                        lista_r[1] = f"{nombres[0]} {nombres[1]}"  # Modificar solo el nombre
                    
                    hora_validar = self.convertir_a_hora_str(lista_r[6])

                    
                    if r[0] in self.salones_primer_nivel:
                        idx = self.salones_primer_nivel.index(r[0])
                        if hora_validar not in self.horario_dict_1:
                            self.horario_dict_1[hora_validar] = [() for _ in self.salones_primer_nivel]
                        self.horario_dict_1[hora_validar][idx] = tuple(lista_r)
                    
                    if r[0] in self.salones_segundo_nivel:
                        idx = self.salones_segundo_nivel.index(r[0])
                        if hora_validar not in self.horario_dict_2:
                            self.horario_dict_2[hora_validar] = [() for _ in self.salones_segundo_nivel]
                        self.horario_dict_2[hora_validar][idx] = tuple(lista_r)

                    # Filtrar por hora si coincide
                    if hora_validar == self.select_horas:
                        
                        #Modifica el estado
                        if r[0] in self.salones_informacion:
                            self.salones_informacion[r[0]] = True
                            
                        horarios_procesados.append(tuple(lista_r))  # Convertir de vuelta a tupla
                        
                self.lista_horarios = horarios_procesados

        if not self.lista_horarios:
            self.lista_horarios.append(tuple(["NONE"]))
            
class Tabla_ConsultaHorarios(rx.State):
    _db:MYSQLDB = MYSQLDB()
    lista_horarios: list[tuple] = []
    no_empleado = ""

    async def informacion_horarios(self):
        self.lista_horarios = [] # Reinicia la lista
        self.no_empleado = await self.get_var_value(InicioSesion.no_empleado_activo)
        resultado = self._db.consulta_horarios(self.no_empleado)
        # Convierte el resultado en una lista de tuplas
        self.lista_horarios = [tuple(row) for row in resultado]

    def actualizar_horarios(self):
        self.lista_horarios = [] # Reinicia la lista
        resultado = self._db.consulta_horarios(self.no_empleado)
        # Convierte el resultado en una lista de tuplas
        self.lista_horarios = [tuple(row) for row in resultado]

    def eliminar_reserva(self, salon:str, fecha:str, hora:str):        
        disponibilidad = self._db.verificacion_disponibilidad(self.no_empleado)
        cant_disponible = disponibilidad[0][0]
        if cant_disponible == 4:
            query = self._db.eliminar_reserva(salon, fecha, hora)
            self.actualizar_horarios()
            return rx.toast.success("Reservación eliminado correctamente.")
        else:
            query = self._db.eliminar_reserva(salon, fecha, hora)
            query = self._db.sumar_reservacion(self.no_empleado)
            self.actualizar_horarios()
            return rx.toast.success("Reservación eliminado correctamente.")

class AsignacionHorarios(rx.State):
    _db:MYSQLDB = MYSQLDB()
    salon_abierto: str = ""  # o None por defecto
    nivel:str = ""
    mostrar_formulario:bool = False
    salon:str = ""

    #Informacion para hacer reserva con información predeterminada
    curso_seleccionado:str = ""
    opciones_cursos: list[str] = []
    clave_seleccionado:str = ""
    opciones_clave: list[str] = []

    opciones_grupos: list[str] = ["700", "710", "720", "721", "730", "731", 
                         "740", "741", "750", "751", "760", "761"]

    menu_desktop:bool = False
    menu_mobile:bool = False
    min_date: str = datetime.today().strftime("%Y-%m-%d")
    select_horario:bool = True
    fecha_seleccionada:str = ""
    fecha_fin_habilitado: bool = True
    checkbox_hrs:dict[str, list[bool, bool]] = {"7:00":[False, False], "8:00":[False, False], "9:00":[False, False], "10:00":[False, False], "11:00":[False, False],
                    "12:00": [False, False], "13:00":[False, False], "14:00":[False, False], "15:00": [False, False], "16:00":[False, False], "17:00": [False, False],
                    "18:00": [False, False], "19:00":[False, False], "20:00":[False, False], "21:00":[False, False]}
    
    def carga_informacion_form(self):
        resultado = self._db.consulta_cursos()
        # Convierte el resultado en una lista de tuplas
        datos_db = [tuple(row) for row in resultado]
        self.opciones_clave = [i[0] for i in datos_db] # Obtiene los valores que se encuentran el la db para ser usado como opciones
        self.opciones_cursos = [i[1] for i in datos_db] # Obtiene los valores que se encuentran el la db para ser usado como opciones

        self.clave_seleccionado = ""
        self.curso_seleccionado = ""

    def set_clave(self, value:str):
        index = self.opciones_clave.index(value)
        self.clave_seleccionado = value
        self.curso_seleccionado = self.opciones_cursos[index]

    def set_curso(self, value:str):
        index = self.opciones_cursos.index(value) # Obtiene el index en donde se encuentra el valor
        self.curso_seleccionado = value # Se agrega el valor en el buscador (input)
        self.clave_seleccionado = self.opciones_clave[index] # Se agrega automaticamente si lo encuntra en el input (Funciona como un autocompletado)

    def seleccion_salon(self, salon):
        #self.mostrar_formulario = True
        # Esto sirve para validar en los dialog, en el open se realiza un condicion para saber si es True o False.
        # Si el salon abierto es igual al salon que se presiona entonces es True.
        self.salon_abierto = salon
        #self.salon = salon # Este solo es para visualizar texto en el formulario.
        self.mostrar_formulario = True

    def component_menu_horas_desktop(self, value):
        # Solo permite abrir el menú si select_horario es False
        if not self.select_horario:
            self.menu_desktop = value
        else:
            self.menu_desktop = False

    def component_menu_horas_mobile(self, value):
        # Solo permite abrir el menú si select_horario es False
        if not self.select_horario:
            self.menu_mobile = value
        else:
            self.menu_mobile = False

    def hrs_seleccionadas(self, value, hora):
        # Cambia el estado del checkbox de la hora seleccionada para mantener el estado en el formulario
        self.checkbox_hrs[hora][0] = value

    def cancelar(self):
        self.mostrar_formulario = False
        #self.menu = False
        self.menu_desktop = False
        self.menu_mobile = False
        self.salon_abierto = ""
        self.fecha_fin_habilitado= True
        self.select_horario = True
        self.checkbox_hrs:dict[str, list[bool, bool]] = {"7:00":[False, False], "8:00":[False, False], "9:00":[False, False], "10:00":[False, False], "11:00":[False, False],
                    "12:00": [False, False], "13:00":[False, False], "14:00":[False, False], "15:00": [False, False], "16:00":[False, False], "17:00": [False, False],
                    "18:00": [False, False], "19:00":[False, False], "20:00":[False, False], "21:00":[False, False]}

        self.clave_seleccionado = ""
        self.curso_seleccionado = ""

    def toggle_fecha_fin(self):
        self.fecha_fin_habilitado = not self.fecha_fin_habilitado

    # Esta funcion es para filtrar los horarios disponibles en el salon seleccionado con la fecha seleccionada en el formulario
    def filtro_horarios(self, salon:str, fecha:str):
        if salon and fecha:
            lista_registros = []
            self.checkbox_hrs:dict[str, list[bool, bool]] = {"7:00":[False, False], "8:00":[False, False], "9:00":[False, False], "10:00":[False, False], "11:00":[False, False],
                    "12:00": [False, False], "13:00":[False, False], "14:00":[False, False], "15:00": [False, False], "16:00":[False, False], "17:00": [False, False],
                    "18:00": [False, False], "19:00":[False, False], "20:00":[False, False], "21:00":[False, False]}
            # NOTA PREGUNTAR CON JUAN QUE PASA CON LA CONSULTA YA QUE LA CONSULTA TRAE TODOS LOS DATOS DE LA TABLA 
            resultados = self._db.consulta_horarios_ocupados(salon, fecha)
            # Convierte el resultado en una lista de tuplas
            for row in resultados:
                hora = (datetime.min + row[6]).strftime("%H:%M")  # Formato HH:MM
                hora = hora.lstrip("0") if hora.startswith("0") else hora  # Elimina el cero solo si está al inicio
                lista_registros.append(hora)

            for key, value in self.checkbox_hrs.items():
                for i in lista_registros:
                    if i == key:
                        self.checkbox_hrs[key][1] = True

            lista_registros = []  

    # Esta funcion habilita el select de horarios cuando existe una fecha seleccionada en el input del formulario
    def toggle_select_horas(self, fecha):
        if fecha != "":
            self.fecha_seleccionada = fecha
            self.filtro_horarios(self.salon_abierto, fecha)
            self.select_horario = False
        else:
            self.select_horario = True

    def aceptar_reserva(self, form_data:dict):
        salon = self.salon_abierto
        no_empleado = form_data.get("numero_empleado")
        nombre_docente = form_data.get("nombre_maestro")
        clave_materia = form_data.get("clave_materia")
        nombre_materia = form_data.get("nombre_materia")
        grupo = form_data.get("grupo")
        fecha_inicio = form_data.get("fecha_inicio")

        disponibilidad = self._db.verificacion_disponibilidad(no_empleado)
        cant_disponible = disponibilidad[0][0]

        if cant_disponible > 0:
            # Sección de horas reservadas
            # Nota: Es el unico que no se extrae del formulario ya que el componente es creado, no de reflex
            horas_reservadas = []

            for key, value in self.checkbox_hrs.items():
                if value[0]: # [0] es el valor booleano del checkbox para saber si esta seleccionado
                    horas_reservadas.append(key)

            if len(horas_reservadas) == 0:
                return rx.window_alert("Falta seleccionar las horas para la reservación.")
            
            if len(horas_reservadas) > cant_disponible:
                return rx.window_alert("No tienes disponibilidad de horas para reservar.")

            for hora in horas_reservadas:
                query = self._db.add_reserva(salon, no_empleado, clave_materia, grupo, fecha_inicio, None, hora, status="RESERVADO")
                query = self._db.restar_reservacion(no_empleado)

            yield ConsultaHorarios.informacion_horarios

            self.menu_desktop = False
            self.menu_mobile = False
            self.mostrar_formulario = False
            self.clave_seleccionado = ""
            self.curso_seleccionado = ""
            self.salon = ""
            self.salon_abierto = ""
            self.fecha_fin_habilitado= True
            self.select_horario = True
            self.checkbox_hrs:dict[str, list[bool, bool]] = {"7:00":[False, False], "8:00":[False, False], "9:00":[False, False], "10:00":[False, False], "11:00":[False, False],
                        "12:00": [False, False], "13:00":[False, False], "14:00":[False, False], "15:00": [False, False], "16:00":[False, False], "17:00": [False, False],
                        "18:00": [False, False], "19:00":[False, False], "20:00":[False, False], "21:00":[False, False]}
            
            return rx.toast.success("Reservación agregado correctamente.")
        else:
            return rx.window_alert("No tienes disponibilidad de horas para reservar.")

class FormCambio(rx.State):
    _db:MYSQLDB = MYSQLDB()
    mostrar_formulario:bool = False

    def abrir_form(self):
        self.mostrar_formulario = True

    def cancelar(self):
        self.mostrar_formulario = False
    
    async def aceptar_cambio(self, form_data:dict):
        if form_data.get("nueva_contraseña") and form_data.get("confirmar_contraseña"):
            nueva = form_data["nueva_contraseña"]
            confirmacion = form_data["confirmar_contraseña"]

            if nueva == confirmacion:
                hash = encriptado_password(confirmacion)
                no_empleado = await self.get_var_value(InicioSesion.no_empleado_activo)


                # Actualizando la contraseña
                self._db.cambio_password(no_empleado, hash)
                self.mostrar_formulario = False
                yield rx.toast.success("Contraseña cambiada correctamente.")
            else:
                yield rx.window_alert("Las constraseñas no coinciden.")
