from Sort.Sortable import Sortable
class BubbleSort(Sortable):
    """
    This class implements the Bubble Sort algorithm
    """
    
    def Sort(self):
        n = len(self.elements)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.elements[j] > self.elements[j+1]:
                   self.elements[j], self.elements[j+1] = self.elements[j+1], self.elements[j]
        
        return self.elements


