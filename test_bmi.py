import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import os

class TestBMICalculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:5000')  # Update with your website URL
        self.results = []

    def tearDown(self):
        self.driver.quit()
        # Save results to file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f'test_results_{timestamp}.txt', 'w') as f:
            f.write("BMI Calculator Test Results\n")
            f.write("=" * 50 + "\n")
            f.write(f"Test Run Date: {datetime.datetime.now()}\n\n")
            for result in self.results:
                f.write(f"Test Case: {result['case']}\n")
                f.write(f"Input: Height={result['height']}{result['height_unit']}, "
                       f"Weight={result['weight']}{result['weight_unit']}\n")
                f.write(f"Expected: {result['expected']}\n")
                f.write(f"Result: {'PASS' if result['passed'] else 'FAIL'}\n")
                f.write("-" * 50 + "\n")

    def test_bmi_calculations(self):
        test_cases = [
            # height_unit, height/feet, inches, weight_unit, weight, expected_category
            ('cm', '170', '0', 'kg', '70', 'Normal weight'),
            ('cm', '160', '0', 'kg', '85', 'Obese Class I'),
            ('ft_in', '5', '9', 'lbs', '150', 'Normal weight'),
            ('ft_in', '5', '6', 'lbs', '200', 'Obese Class I'),
        ]

        for height_unit, height, inches, weight_unit, weight, expected_category in test_cases:
            print(f"\nTesting: Height={height}{height_unit}, Weight={weight}{weight_unit}")
            
            # Select height unit
            height_select = Select(self.driver.find_element(By.NAME, 'height_unit'))
            height_select.select_by_value(height_unit)

            # Enter height
            if height_unit == 'cm':
                self.driver.find_element(By.NAME, 'height').send_keys(height)
                height_display = f"{height}cm"
            else:
                self.driver.find_element(By.NAME, 'feet').send_keys(height)
                self.driver.find_element(By.NAME, 'inches').send_keys(inches)
                height_display = f"{height}ft {inches}in"

            # Select weight unit and enter weight
            weight_select = Select(self.driver.find_element(By.NAME, 'weight_unit'))
            weight_select.select_by_value(weight_unit)
            self.driver.find_element(By.NAME, 'weight').send_keys(weight)

            # Submit form
            self.driver.find_element(By.TAG_NAME, 'form').submit()

            # Check result
            result = self.driver.find_element(By.ID, 'bmi-result-section')
            passed = expected_category in result.text
            
            # Store result
            self.results.append({
                'case': len(self.results) + 1,
                'height': height_display,
                'height_unit': height_unit,
                'weight': weight,
                'weight_unit': weight_unit,
                'expected': expected_category,
                'passed': passed
            })

            print(f"Expected: {expected_category}")
            print(f"Result: {'PASS' if passed else 'FAIL'}")

            # Clear form for next test
            self.driver.refresh()

if __name__ == '__main__':
    unittest.main(verbosity=2)