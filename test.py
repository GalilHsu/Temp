#-*- coding: utf-8 -*-
import unittest

from data_verification import *

class TestDataVerification(unittest.TestCase):

    def test_01_column_miss(self):
        """測試模擬場景，資料有遺漏值"""
        test_data = {
            "ad_network": "FOO",
            "date": "2019-06-05",
            "app_name": "LINETV",
            "unit_id": "55665201314",
            "request": "100", 
            "imp": "23"
        }
        verification = app_data_verification(test_data)["verification"]
        self.assertEqual(verification, 0)

    def test_02_error_date(self):
        """測試模擬場景，資料日期錯誤"""
        test_data = {
            "ad_network": "FOO",
            "date": "2019/06/05",
            "app_name": "LINETV",
            "unit_id": "55665201314",
            "request": "100", 
            "revenue": 0.00365325, 
            "imp": "23"
        }
        verification = app_data_verification(test_data)["verification"]
        self.assertEqual(verification, 0)

    def test_03_error_type(self):
        """測試模擬場景，資料型態錯誤"""
        test_data = {
            "ad_network": "FOO",
            "date": "2019-06-05",
            "app_name": "LINETV",
            "unit_id": "55665201314",
            "request": 100, 
            "revenue": 0.00365325, 
            "imp": "23"
        }
        verification = app_data_verification(test_data)["verification"]
        self.assertEqual(verification, 0)

    def test_04_error_value(self):
        """測試模擬場景，資料值為空值或是None"""
        test_data = {
            "ad_network": None,
            "date": "2019-06-05",
            "app_name": "LINETV",
            "unit_id": "55665201314",
            "request": "100", 
            "revenue": 0.00365325, 
            "imp": "23"
        }
        verification = app_data_verification(test_data)["verification"]
        self.assertEqual(verification, 0)

if __name__ == '__main__':
    unittest.main()