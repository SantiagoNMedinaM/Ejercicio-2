from claseviajerofrecuente import ViajeroFrecuente
import csv
class Controlador:
    __viajeros=[]
    def __init__(self):
        self.__viajeros = []
    def crearLista(self):
        archivo = open("Viajeros.csv")
        reader = csv.reader (archivo,delimiter=";")
        for fila in reader:
            nro=int(fila[0])
            dni=str(fila[1])
            nom=str(fila[2])
            ape=str(fila[3])
            tmil=int(fila[4])
            viajero=ViajeroFrecuente(nro,dni,nom,ape,tmil)
            self.__viajeros.append(viajero)
    def buscar_viajero(self,n):
        i=0
        viajeroc=None
        while (i<len(self.__viajeros)):
            if self.__viajeros[i].getNum() == n:
                viajeroc=self.__viajeros[i]
            i+=1
        if viajeroc == None:
            print ("El numero de viajero ingresado es invalido")
        return viajeroc
         
