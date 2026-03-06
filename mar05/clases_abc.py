from abc import ABC, abstractmethod
class Seguro(ABC):
    @abstractmethod
    def calcular_premium(self):
        pass
    @abstractmethod
    def mostrar_detalles(self):
        pass
    
class SeguroMapfre(Seguro):
    def calcular_premium(self):
        return 1000  # Implementación concreta del método calcular_premium, que devuelve un valor fijo de 1000 como ejemplo. En una implementación real, este método podría realizar cálculos más complejos basados en factores como la edad del asegurado, el tipo de cobertura, el historial de reclamaciones, entre otros.

    def mostrar_detalles(self):
        return "Seguro Mapfre: Cobertura completa con asistencia 24/7."  # Implementación concreta del método mostrar_detalles, que devuelve una descripción de los detalles del seguro. En una implementación real, este método podría proporcionar información más detallada sobre las coberturas específicas, los beneficios adicionales, las exclusiones, entre otros aspectos relevantes del seguro.
 
class SeguroAllianz(Seguro):
    def calcular_premium(self):
        return 1200  # Implementación concreta del método calcular_premium para el seguro de Allianz, que devuelve un valor fijo de 1200 como ejemplo. Al igual que en la clase SeguroMapfre, este método podría realizar cálculos más complejos en una implementación real.

    def mostrar_detalles(self):
        return "Seguro Allianz: Cobertura amplia con asistencia internacional."  # Implementación concreta del método mostrar_detalles para el seguro de Allianz, que devuelve una descripción de los detalles del seguro. En una implementación real, este método podría proporcionar información más detallada sobre las coberturas específicas, los beneficios adicionales, las exclusiones, entre otros aspectos relevantes del seguro. 
   
if __name__ == "__main__":
    #seguro = Seguro()  # Intentar crear una instancia de la clase abstracta Seguro resultará en un error, ya que las clases abstractas no pueden ser instanciadas directamente. Para utilizar esta clase, se debe crear una subclase concreta que implemente los métodos abstractos calcular_premium y mostrar_detalles, y luego se puede crear una instancia de esa subclase concreta para utilizar sus funcionalidades.
    seguro_mapfre = SeguroMapfre()  # Crea una instancia de la clase concreta SeguroMapfre, que implementa los métodos abstractos de la clase base Seguro.
    print(seguro_mapfre.calcular_premium())  # Llama al método calcular_premium de la instancia seguro_mapfre, lo cual devuelve el valor fijo de 1000 como se definió en la implementación concreta del método en la clase SeguroMapfre.
    print(seguro_mapfre.mostrar_detalles())  # Llama al método mostrar_detalles de la instancia seguro_mapfre, lo cual devuelve la descripción de los detalles del seguro de Mapfre como se definió en la implementación concreta del método en la clase SeguroMapfre.
    seguro_allianz = SeguroAllianz()  # Crea una instancia de la clase concreta SeguroAllianz, que implementa los métodos abstractos de la clase base Seguro.
    print(seguro_allianz.calcular_premium())  # Llama al método calcular_premium de la instancia seguro_allianz, lo cual devuelve el valor fijo de 1200 como se definió en la implementación concreta del método en la clase SeguroAllianz.
    print(seguro_allianz.mostrar_detalles())  # Llama al método mostrar_detalles de la instancia seguro_allianz, lo cual devuelve la descripción de los detalles del seguro de Allianz como se definió en la implementación concreta del método en la clase SeguroAllianz.
    lista_seguros = [seguro_mapfre, seguro_allianz]  # Crea una lista de seguros que contiene instancias de ambas clases concretas (SeguroMapfre y SeguroAllianz), lo cual demuestra cómo se pueden utilizar polimórficamente las instancias de las clases concretas a través de la clase base abstracta Seguro. Esto permite tratar a ambos tipos de seguros de manera uniforme, ya que ambos implementan los mismos métodos abstractos definidos en la clase base Seguro.