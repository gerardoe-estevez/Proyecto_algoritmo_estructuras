#Python 3.6
"""
Una empresa de desarrollo de software requiere una agenda de contactos
para uno de sus clientes y te ha contratado a ti para programarla.
Esta agenda de contactos debe almacenar el nombre, apellido, correo
electrónico, lugar de trabajo y total de actividades a realizar. Esta agenda debe
cumplir con los siguientes módulos:
1. Crear un nuevo contacto, cada contacto debe ser único.
2. Modificar un contacto
3. Listar los contactos existentes y generar los siguientes resultados: Contacto
con más actividades, contacto con menos actividades, promedio de
actividades.
4. Eliminar un contacto
5. Consultar los datos de un determinado contacto
"""
class Contact:
    def __init__(
        self,
        first_name:str,
        last_name:str,
        email:str,
        work_place:str,
        total_activities:int
        ):

        self._first_name=first_name
        self._last_name=last_name
        self._email=email
        self._work_place=work_place
        self._total_activities=total_activities

    #getter and setter first_name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,new_first_name:str):
        self._first_name=new_first_name

    #getter and setter last_name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self,new_last_name:str):
        self._last_name=new_last_name

    #getter and setter email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,new_email:str):
        self._email=new_email

    #getter and setter work_place
    @property
    def work_place(self):
        return self._work_place

    @work_place.setter
    def work_place(self,new_work_place:str):
        self._work_place=new_work_place

    #getter and setter work_place
    @property
    def total_activities(self):
        return self._total_activities

    @total_activities.setter
    def total_activities(self,total_activities:int):
        self._total_activities=total_activities

    def __str__(self):
        string="("+str(self._first_name)+","+str(self._last_name)+")"
        return string