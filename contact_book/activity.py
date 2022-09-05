class Activity:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_finalizacion, estatus):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.estatus = estatus

    #getter and setter id
    @property
    def id(self):
        return self._id

    id.setter
    def id(self,new_id:str):
        self._id=new_id

    #getter and setter nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,new_nombre:str):
        self._nombre=new_nombre

    #getter and setter descripcion
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self,new_descripcion:str):
        self._descripcion=new_descripcion

    #getter and setter fecha_inicio
    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self,new_fecha_inicio:str):
        self._fecha_inicio=new_fecha_inicio

    #getter and setter fecha_finalizacion
    @property
    def fecha_finalizacion(self):
        return self._fecha_finalizacion

    @fecha_finalizacion.setter
    def fecha_finalizacion(self,new_fecha_finalizacion:str):
        self._fecha_finalizacion=new_fecha_finalizacion

    #getter and setter estatus
    @property
    def estatus(self):
        return self._estatus

    @estatus.setter
    def estatus(self,new_estatus:str):
        self._estatus=new_estatus

