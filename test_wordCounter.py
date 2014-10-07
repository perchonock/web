from unittest import TestCase
from count_words import *

__author__ = 'YKolotolova'


class TestWordCounter(TestCase):
    def test_count_words1(self):
        file = open("test1.txt", "r")
        counter = WordCounter()
        number_of_words = counter.count_words(file)
        self.assertTrue(number_of_words == 6, "The number is not correct")
        file.close()

    def test_count_words2(self):
        file = open("test2.txt", "r")
        counter = WordCounter()
        number_of_words = counter.count_words(file)
        self.assertTrue(number_of_words == 0, "The number is not correct")
        file.close()

    def test_count_words3(self):
        file = open("test3.txt", "r")
        counter = WordCounter()
        number_of_words = counter.count_words(file)
        self.assertTrue(number_of_words == 1, "The number is not correct")
        file.close()

    def test_count_words4(self):
        file = open("test4.txt", "r")
        counter = WordCounter()
        number_of_words = counter.count_words(file)
        self.assertTrue(number_of_words == 0, "The number is not correct")
        file.close()

    def test_count_words5(self):
        file = open("test5.txt", "r")
        counter = WordCounter()
        number_of_words = counter.count_words(file)
        self.assertTrue(number_of_words == 6, "The number is not correct")
        file.close()