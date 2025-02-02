# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Telefon:
    def __init__(self,model:str,year_release:int,cost:[int,float],aval:bool):
        if not isinstance(model, str):
            raise TypeError
        self.model=model
        if not isinstance(year_release, int ):
            raise TypeError
        if year_release>2025:
            raise ValueError
        self.year_release=year_release
        if not isinstance(cost, (int, float)):
            raise TypeError
        if cost < 0:
            raise ValueError
        self.cost=cost
        if not isinstance(aval,  bool):
            raise TypeError
        self.aval=aval
        """Класс Телефон атрибуты :модель тип только строка 
        год выпуска целое число год должен быть до 2025,ведь он не создан в будущем 
        цена целое иди дробное не должна быть отрицательна 
        атрибут aval наличие в магазине  если есть то True если не то False
        """
    def costNow(self,cost_new):
        """ МЕТОД НОВАЯ ЦЕНА если цена на рынке изменилась то нужно задать новую цену товара
        в этом методе передает пользователь новую цену ее нужно проверить чтобы она была нужного нам типа
        и не отрицательная цена
        после присваиваем атрибуту self.coast новую цену
        """
        if not isinstance(cost_new, (int, float)):
            raise TypeError
        if cost_new < 0:
            raise ValueError
        self.cost=cost_new
    def Availability(self,aval_new):
        """МЕТОД НАЛИЧИЕ чтобы пользователь мок поменть наличие товара в магазине
        если новая поставка или этот телефон продан """
        if not isinstance(aval_new, bool):
            raise TypeError
        self.aval = aval_new

class Vector:
    def __init__(self,x:[int,float],y:[int,float]):
        if not isinstance(x, (int,float)):
          raise TypeError
        self.X=x
        if not isinstance(y, (int,float)):
          raise TypeError
        self.Y=y
        """класс вектор у него есть 2 координаты x и y
            координаты должны быть цулыми или дробными 
        """
    def Long(self)->[int,float]:
        """метод который ищет длинну нашего верктора """
    def COS(self,othervector):
        """метод который ищет угол между двумя векторами на вход другой вектор """

class Squar:
    def __init__(self,long: [int,float],width:[int,float]):
        if not isinstance(long, (int, float)):
            raise TypeError
        if long < 0:
            raise ValueError
        self.long=long
        if not isinstance(width, (int, float)):
            raise TypeError
        if width < 0:
            raise ValueError
        self.width=width
        """Класс Квадрат 
        у него есть атрибут длинна и ширина эти величины должны быть положительны
        пример squa1=Squar(5,6)
        """
    def square(self)->(int,float):#метод который находит площадь нашего квадрата
        S=self.long*self.width
        return S
    def perimetr(self)->(int,float):#метод который находит периметр
        P=self.long+self.width
        return P
sqar1=Squar(5,10)
print(sqar1.width,sqar1.long)
print(sqar1.square())
if __name__ == "__main__":
    if __name__ == "__main__":
        doctest.testmod()
        # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

