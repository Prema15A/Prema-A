class dept:
   def __init__(self):
         self.list1=[]
 
   def push(self,data):
      self.list1.append(data) 
   def pop(self,data):
      self.list1.remove(data)   
s=dept()
s.push("it")
s.push("ece")
s.push("cse")
print(s.list1)
s.pop("ece") 
print(s.list1)
s.peek("")
