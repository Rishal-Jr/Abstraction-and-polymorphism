from abc import ABC,abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value",x)

    @abstractmethod
    def task(self):
        print("We are inside the abstract methord")

class test_class(Absclass):
     def task(self):
        print("We are inside the abstract methord")

task_onj=test_class()
task_onj.task()
task_onj.print(100)        


