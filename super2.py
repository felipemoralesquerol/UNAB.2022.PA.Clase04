class mysuper_class(object):     
    def super_method(self):
        print("Method of the super class was called!")

class myclass(mysuper_class):
    def mymethod(self):
        super().super_method()
        
a = myclass()
a.mymethod()