from Sort.Sortable import Sortable
class MergeSort(Sortable):
    """The merge sort algorithm"""

    def merge(self, arr, left, middle, right):
        pass

    def mergeSort(self, arr):
       if len(arr) <=1:
           return arr
       
       mid = len(arr)//2
       L = arr[:mid]
       R = arr[mid:]
       L = self.mergeSort(L)
       R = self.mergeSort(R)

       print(f"L: {L}, R: {R}")

       if L[-1] <= R[0]:
           return L + R

       return self.merge(L, R)

    def merge(self, L, R):
        result = []
        while len(L) > 0 and len(R) > 0:
            if L[0] <= R[0]:
                result.append(L[0])
                L.pop(0)
            else:
                result.append(R[0])
                R.pop(0)

        if len(L) > 0:
            result = result + L
        if len(R) > 0:
            result = result + R
        return result

    def Sort(self):
        self.elements = self.mergeSort(self.elements)