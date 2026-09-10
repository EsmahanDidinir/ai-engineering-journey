class DataProcessor:
    def __init__(self ,data : list[int | None]):
        self.data=data

    def mean(self):
        if not self.data:
            return None 
        int_sayilar = []
        for sayi in self.data:
            if sayi is not None:
                int_sayilar.append(sayi)
        if not int_sayilar:
            return None
        sonuc = sum(int_sayilar)/len(int_sayilar)
        return sonuc

    def minimum(self):
        if not self.data:
            return None
        min_sayi = None
        for sayi in self.data:
            if sayi is not None:            
                if min_sayi is None:
                    min_sayi = sayi
                if sayi< min_sayi : 
                    min_sayi=sayi
        return min_sayi

    def maximum(self):
        if not self.data:
            return None
        max_sayi=None
        for sayi in self.data:
            if sayi is not None : 
                if max_sayi is None:
                    max_sayi = sayi
                if sayi > max_sayi:
                    max_sayi = sayi
        return max_sayi
    
    def missing_count(self):
        count = 0
        for sayi in self.data:
            if sayi is None:
                count+=1
        return count
    
    def duplicates (self):
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

 
    def sorted_data(self):
        temiz_data = []
        for sayi in self.data:
            if sayi is not None:
                temiz_data.append(sayi)
        temiz_data.sort()
        return temiz_data
