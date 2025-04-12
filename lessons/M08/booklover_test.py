import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        my_book = BookLover("Scott", "scott3141@gmail.com", "History")
        my_book.add_book("GWTW", 5)
        self.assertTrue("GWTW" in my_book.book_list['book_name'].values)
        

    def test_2_add_book(self):
        my_book = BookLover("Scott", "scott3141@gmail.com", "History")
        my_book.add_book("GWTW", 5)
        my_book.add_book("GWTW", 5)
        self.assertEqual(len(my_book.book_list),1)
                
    def test_3_has_read(self): 
        my_book = BookLover("Scott", "scott3141@gmail.com", "History")
        my_book.add_book("GWTW", 5)
        self.assertTrue(my_book.has_read("GWTW"))
        
        
    def test_4_has_read(self): 
        my_book = BookLover("Scott", "scott3141@gmail.com", "History")
        my_book.add_book("GWTW", 5)
        self.assertFalse(my_book.has_read("Great Expectations"))
        
        
    def test_5_num_books_read(self): 
        my_book = BookLover("Scott", "scott3141@gmail.com", "History")
        my_book.add_book("GWTW", 5)
        my_book.add_book("The Godfather", 5)
        my_book.add_book("M*A*S*H", 4)
        my_book.add_book("Midnight in the Garden of Good and Evil", 4)
        self.assertEqual(my_book.num_books, 4)


    def test_6_fav_books(self):
        my_book = BookLover("Scott", "scott3141@gmail.com", "History")
        my_book.add_book("GWTW", 5)
        my_book.add_book("The Godfather", 5)
        my_book.add_book("M*A*S*H", 4)
        my_book.add_book("Midnight in the Garden of Good and Evil", 4)
        for books in my_book.fav_books().values:
            self.assertTrue(books[1] >3)
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
