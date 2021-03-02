# Есть список отрезков
# long_list = [(10, 25), (6, 420), (7, 18), ..., (1, 142)]
# и класс А:
# class A:
#    def __init__(long_list):
#        self.long_list = long_list
#    def intersect_with(x: Tuple[int, int]) -> List[Tuple[int, int]]:
# функция intersect_with должна вернуть те отрезки из long_list, которые пересекаются с x

class A:

    def __init__(long_list):
        self.long_list = long_list

    def intersect_with(x: Tuple[int, int]) -> List[Tuple[int, int]]:
        # Возвращает те отрезки из long_list, которые пересекаются с x
        
        res = []
        
        for i in long_list:
            if x[1] < i[0] or x[0] > i[1]:
                continue
            else:
                res.append(i)
                
        return res
