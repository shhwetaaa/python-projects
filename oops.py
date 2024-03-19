# class Book:
#     def __init__(self,author,year):
#         self.author = author
#         self.year = year
        
        
        
            
#     def full_name(self):
#         return f"{self.year} {self.author}"
        
        
# class DigitalBook(Book):
#     def __init__(self,author,year,award):
#         self.year = year
#         self.award = award
        
# gogo_book = DigitalBook("shwet" , "2024", "the best warrior")                
# print(gogo_book.award)  
# print(gogo_book.author) 
# print(gogo_book.author())      
        
        
        
# new_book = Book("best me" , "2024")
# print(new_book.author)
# print(new_book.full_name())
         
         
#         #  encapsulation
        
# class Book:
#     def __init__(self,author,year):
#         self.__author = author
#         self.year = year
        
        
        
#     def get_author(self):
#         return self.author + "!"
        
            
#     def full_name(self):
#         return f"{self.year} {self.author}"
        
        
# class DigitalBook(Book):
#     def __init__(self,author,year,award):
#         super().__init__(author,year)
#         self.award = award
        
# gogo_book = DigitalBook("shwet" , "2024", "the best warrior")                
# print(gogo_book.award)  
# print(gogo_book.author) 
# print(gogo_book.author())      
        
        
        
# new_book = Book("best me" , "2024")
# print(new_book.author)
# print(new_book.full_name())
          
        
        
        
        
        
        
        
        
        
        
        
        # polymorphism

class Book:
    def __init__(self,author,year):
        self.author = author
        self.year = year
    
    def rating(self):
        return "full"    
        
new_book = Book("me","2023")   
print(new_book.author)


update_book = Book("mee","2023+")   
print(update_book.author)

old_book = Book("you", 2022)
print(old_book.year)
print(old_book.rating())

Book("meee", "2024")



   
                