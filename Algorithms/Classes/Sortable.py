class Sortable():
    """Base class for sorting algorithms"""
    
    elements = None

    def __init__(self, *elements):
        self.elements = list(elements)
    
    def Sort(self):
        pass

    def __str__(self):
        return f"{self.elements}"

    def __len__(self):
        return len(self.elements)