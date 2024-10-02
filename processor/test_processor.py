import unittest
from io import StringIO
import sys
from collections import deque

# Import the functions from the main script
from processor_sensor_data import process_line, calculate_statistics

class TestHealthMonitor(unittest.TestCase):

    def setUp(self):
        # Prepare deques for testing
        self.temperature_values = deque(maxlen=5)
        self.pulse_rate_values = deque(maxlen=5)
        self.spo2_values = deque(maxlen=5)

    def test_process_line_valid(self):
        line = "Temperature: 36.6 PulseRate: 75 SPO2: 98"
        valid = process_line(line, self.temperature_values, self.pulse_rate_values, self.spo2_values)
        
        self.assertTrue(valid)
        self.assertEqual(len(self.temperature_values), 1)
        self.assertEqual(self.temperature_values[0], 36.6)
        self.assertEqual(len(self.pulse_rate_values), 1)
        self.assertEqual(self.pulse_rate_values[0], 75)
        self.assertEqual(len(self.spo2_values), 1)
        self.assertEqual(self.spo2_values[0], 98)

    def test_process_line_invalid(self):
        line = "Invalid input"
        valid = process_line(line, self.temperature_values, self.pulse_rate_values, self.spo2_values)
        
        self.assertFalse(valid)
        self.assertEqual(len(self.temperature_values), 0)
        self.assertEqual(len(self.pulse_rate_values), 0)
        self.assertEqual(len(self.spo2_values), 0)

    def test_calculate_statistics(self):
        # Simulate valid inputs
        self.temperature_values.extend([36.5, 37.0, 36.8, 37.2, 36.9])
        self.pulse_rate_values.extend([70, 75, 80, 78, 72])
        self.spo2_values.extend([95, 96, 97, 98, 99])

        stats = calculate_statistics(self.temperature_values, self.pulse_rate_values, self.spo2_values)

        self.assertEqual(stats['max_temperature'], 37.2)
        self.assertEqual(stats['min_temperature'], 36.5)
        self.assertAlmostEqual(stats['avg_temperature'], 36.88, places=2)

        self.assertEqual(stats['max_pulse_rate'], 80)
        self.assertEqual(stats['min_pulse_rate'], 70)
        self.assertAlmostEqual(stats['avg_pulse_rate'], 75.0, places=2)

        self.assertEqual(stats['max_spo2'], 99)
        self.assertEqual(stats['min_spo2'], 95)
        self.assertAlmostEqual(stats['avg_spo2'], 97.0, places=2)

if __name__ == '__main__':
    unittest.main()
