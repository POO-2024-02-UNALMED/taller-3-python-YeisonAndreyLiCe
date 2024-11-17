class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV.numTV += 1

    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca

    def getCanal(self):
        return self._canal
    
    def setCanal(self, canal):
        self._canal = canal

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio):
        self._precio = precio

    def getEstado(self):
        return self._estado
    
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, volumen):
        self._volumen = volumen

    def getControl(self):
        return self._control
    
    def setControl(self, control):
        self._control = control

    @classmethod
    def getNumTV(cls):
        return cls.numTV
    
    @classmethod
    def setNumTV(cls, numTV):
        cls.numTV = numTV

    def canalUp(self):
        if self._estado and self._canal < 120:
            self._canal += 1

    def canalDown(self):
        if self._estado and self._canal > 1:
            self._canal -= 1

    def volumenUp(self):
        if self._estado and self._volumen < 7:
            self._volumen += 1

    def volumenDown(self):
        if self._estado and self._volumen > 0:
            self._volumen -= 1
