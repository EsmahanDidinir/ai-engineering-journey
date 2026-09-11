class DataProcessor:
    def __init__(self ,data : list[int | None]):
        self.data=data

    def mean(self)-> float | None:
        sayilar = [sayi for sayi in self.data if sayi is not None]
        if not sayilar:
            return None
        sonuc = sum(sayilar)/len(sayilar)
        return sonuc

    def minimum(self) -> int | None:
        sayilar = [sayi for sayi in self.data if sayi is not None]
        if not sayilar:
            return None
        return min(sayilar)

    def maximum(self) -> int | None:
            sayilar = [sayi for sayi in self.data if sayi is not None]
            if not sayilar:
                return None
            return max(sayilar)
    
    def missing_count(self)-> int:
        count = 0
        for sayi in self.data:
            if sayi is None:
                count+=1
        return count
    
    def duplicates (self)->list[int]:
        gorulenler = set()
        duplicates = []
        for sayi in self.data:
            if sayi is not None:
                    if sayi in gorulenler:
                        if sayi not in duplicates:
                            duplicates.append(sayi)
                    else:
                        gorulenler.add(sayi)
        return duplicates

 
    def sorted_data(self)->list[int]:
        temiz_data = []
        for sayi in self.data:
            if sayi is not None:
                temiz_data.append(sayi)
        temiz_data.sort()
        return temiz_data
