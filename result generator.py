class ITdep:
    def __init__(self,python,java,C):
        self.p=python
        self.j=java
        self.c=C
        
    def ITtmarks(self):
        totalmarks=(self.p+self.j+self.c)/3
        print("Total Marks: ",totalmarks,"%")
        
    
class CHEMdep:
    def __init__(self,organic,inorganic,physical):
        self.o=organic
        self.i=inorganic
        self.p=physical
        
    def CHEMtmarks(self):
        totalmarks=(self.i+self.o+self.p)/3
        print("total marks",totalmarks,"%")
        
        
class Results(ITdep,CHEMdep):
    def __init__(self,option,name,rollno):
        self.name=name
        self.rollno=rollno
        if option==1:
            python=int(input("Python: "))
            java=int(input("Java: "))
            C=int(input("C: "))
            ITdep.__init__(self, python, java, C)
            print(f"Name: {self.name} Roll No: {self.rollno}")
            self.ITtmarks()
            
        elif option==2:
            organic=int(input("Organic: "))
            inorganic=int(input("Inorganic: "))
            physical=int(input("Physical: "))
            CHEMdep.__init__(self, organic, inorganic, physical)
            print(f"Name: {self.name} Roll No: {self.rollno}")
            self.CHEMtmarks()
            
option=int(input("which department do you want 1.IT Department 2.Chemistry Department: "))
name=input("enter student name: ")
rollno=int(input("enter student roll no: "))
r=Results(option,name,rollno)