class DataProcessor:
    def __init__(self ,data : list[int | None]):
        self.data=data

    def mean(self)-> float | None:
        numbers = self.clean_none()
        if not numbers:
            return None
        result = sum(numbers) / len(numbers)
        return result

    def minimum(self) -> int | None:
        numbers = self.clean_none()
        if not numbers:
            return None
        return min(numbers)

    def maximum(self) -> int | None:
            numbers = self.clean_none()
            if not numbers:
                return None
            return max(numbers)
    
    def missing_count(self)-> int:
        count = 0
        for num in self.data:
            if num is None:
                count+=1
        return count
    
    def duplicates (self)->list[int]:
        numbers= self.clean_none()
        seen = set()
        duplicates = []
        for num in numbers:
            if num in seen:
             if num not in duplicates:
                duplicates.append(num)
            else:
                seen.add(num)
        return duplicates

 
    def sorted_data(self)->list[int]:
        clean_data = self.clean_none()
        clean_data.sort()
        return clean_data


    def clean_none(self):
        clean_data = [num for num in self.data if num is not None]
        return clean_data
def process_age(age):
    try:
        int_age = int(age)
        return int_age * 2
    except ValueError:
        raise ValueError("Sayıya çevrilmedi.")
    except TypeError:
         raise TypeError("Yaş None olamaz.")