zclass Queue:
    def __init__(self):
         self.item = []
        
     def is_empty(self):
         return self.items == []
         
     def enqueue(self,item):
          self.items.insert(0,item)
         
     def dequeue(self):
          return self.items.pop()
         
     def print_stack(self):
          print(self,items)                                                            