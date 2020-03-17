from Classes.Sortable import Sortable
class QuickSort(Sortable):
    """
    This class implements the Quick Sort algorithm
    """

    def partition(self, arr, low, high):
        i=low-1
        pivot=arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i=i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[high], arr[i+1] = arr[i+1], arr[high]

        return i+1

    def quickSort(self, arr, low, high):
        if(low<high):
            partitionIndex = self.partition(arr, low, high)

            self.quickSort(arr, low, partitionIndex-1)
            self.quickSort(arr, partitionIndex+1, high)
            
    def Sort(self):
        self.quickSort(self.elements, 0, len(self)-1)



