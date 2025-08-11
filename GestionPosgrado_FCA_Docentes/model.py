import reflex as rx
from sqlalchemy import text  # Importa la función text esto es porque esta,os consultando de manera cruda

class MYSQLDB(rx.Base):
    def verificacion_usuario(self, no_empleado:str, password:str):
        try:
            with rx.session() as session:
                resultado_no_empleado = session.exec(
                    text("SELECT id, nombre FROM Docente WHERE no_empleado = :no_empleado"),
                    params={"no_empleado":no_empleado}
                ).fetchall()
                resultado_id = session.exec(
                    text("SELECT id_docente FROM Autenticacion WHERE password = :password"),
                    params={"password":password}
                ).fetchall()

                if resultado_no_empleado and resultado_id:
                    return resultado_no_empleado
                else:
                    print("NO EXISTE")
                    return

        except Exception as e:
            print(f"Error al conectar a la base de datos MySQL: {str(e)}")
            
    def add_reserva(self, clave_salon:str, no_empleado:str, clave_materia:str, grupo:str, fecha_inicio:str, fecha_final:str, hora:str, status:str):
        try:
            with rx.session() as session:
                resultado = session.exec(
                    text("CALL sp_InsertarAsignacion(:clave_salon, :no_empleado, :clave_materia, :grupo, :fecha_inicio, :fecha_final, :hora, :status)"),
                    params={"clave_salon":clave_salon, "no_empleado":no_empleado, "clave_materia":clave_materia, 
                            "grupo":grupo, "fecha_inicio":fecha_inicio, "fecha_final":fecha_final, "hora":hora, "status":status}
                )
                session.commit()
        except Exception as e:
            print(f"Error al conectar a la base de datos MySQL: {str(e)}")

    def editar_reserva(self, clave_salon:str, no_empleado:str, clave_materia:str, grupo:str, fecha_inicio:str, fecha_final:str, hora:str,
                     clave_salon_nuevo:str, no_empleado_nuevo:str, clave_materia_nuevo:str, grupo_nuevo:str, fecha_inicio_nuevo:str, fecha_final_nuevo:str, hora_nuevo:str, status_nuevo:str):
        try:
            print(f"Parámetros: clave_salon={clave_salon}, no_empleado={no_empleado}, clave_materia={clave_materia}, grupo={grupo}, fecha_inicio={fecha_inicio}, fecha_final={fecha_final}, hora={hora}, clave_salon_nuevo={clave_salon_nuevo}, no_empleado_nuevo={no_empleado_nuevo}, clave_materia_nuevo={clave_materia_nuevo}, grupo_nuevo={grupo_nuevo}, fecha_inicio_nuevo={fecha_inicio_nuevo}, fecha_final_nuevo={fecha_final_nuevo}, hora_nuevo={hora_nuevo}, status_nuevo={status_nuevo}")
            with rx.session() as session:
                resultado = session.exec(
                    text("CALL sp_ActualizarAsignacion(:clave_salon, :no_empleado, :clave_materia, :grupo, :fecha_inicio, :fecha_final, :hora, :clave_salon_nuevo, :no_empleado_nuevo, :clave_materia_nuevo, :grupo_nuevo, :fecha_inicio_nuevo, :fecha_final_nuevo, :hora_nuevo, :status_nuevo)"),
                    params={"clave_salon":clave_salon, "no_empleado":no_empleado, "clave_materia":clave_materia, 
                            "grupo":grupo, "fecha_inicio":fecha_inicio, "fecha_final":fecha_final, "hora":hora, "clave_salon_nuevo":clave_salon_nuevo, "no_empleado_nuevo":no_empleado_nuevo, "clave_materia_nuevo":clave_materia_nuevo, 
                            "grupo_nuevo":grupo_nuevo, "fecha_inicio_nuevo":fecha_inicio_nuevo, "fecha_final_nuevo":fecha_final_nuevo, "hora_nuevo":hora_nuevo, "status_nuevo":status_nuevo,}
                )
                session.commit()
                print("Actualización exitosa")
        except Exception as e:
            print(f"Error al conectar a la base de datos MySQL: {str(e)}, tipo de error: {type(e)}")

    def eliminar_reserva(self, salon, fecha, hora):
        try:
            with rx.session() as session:
                resultado = session.exec(
                    text("CALL sp_EliminarAsignacion(:salon, :fecha, :hora)"),
                    params={"salon":salon, "fecha":fecha, "hora":hora}
                )
                session.commit()
        except Exception as e:
            print(f"Error al conectar a la base de datos MySQL: {str(e)}")

    def consulta_horarios(self, no_empleado:str):
        try:
            with rx.session() as session:
                resultado = session.exec(
                    text("CALL ConsultarAsigPorEmpleado(:no_empleado)"),
                    params={"no_empleado":no_empleado}
                ).fetchall()
                return resultado
        except Exception as e:
            print(f"Error al conectar a la base de datos MySQL: {str(e)}")

    def consulta_asignacion_fecha(self, fecha:str):
        try:
            with rx.session() as session:
                resultado = session.exec(
                    text("CALL ConsultarAsigFecha(:fecha)"),
                    params={"fecha":fecha}
                ).fetchall()
                return resultado
        except Exception as e:
            print(f"Error al conectar a la base de datos MySQL: {str(e)}")

    def consulta_horarios_ocupados(self, salon:str, fecha:str):
            try:
                with rx.session() as session:
                    resultado = session.exec(
                        text("CALL ConsultarAsigSalonYFecha(:salon, :fecha)"),
                        params={"salon":salon, "fecha":fecha}
                    ).fetchall()
                    return resultado
            except Exception as e:
                print(f"Error al conectar a la base de datos MySQL: {str(e)}")

    def cambio_password(self, no_empleado:str, actual:str, nueva:str):
        try:
            with rx.session() as session:
                print(no_empleado, actual, nueva)
                resultado = session.exec(
                    text("CALL CambiarPasswordDocente(:no_empleado, :actual, :nueva)"),
                    params={"no_empleado":no_empleado, "actual":actual, "nueva":nueva}
                )
                session.commit()
        except Exception as e:
            print(f"Error al conectar a la base de datos MySQL: {str(e)}")