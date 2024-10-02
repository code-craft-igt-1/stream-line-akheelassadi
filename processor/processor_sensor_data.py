import re
from collections import deque

def process_line(line, temperature_values, pulse_rate_values, spo2_values):
    # Regular expression to extract values
    pattern = r'Temperature:\s*(\d+\.?\d*)\s*PulseRate:\s*(\d+)\s*SPO2:\s*(\d+)'
    match = re.match(pattern, line)

    if match:
        temperature = float(match.group(1))
        pulse_rate = int(match.group(2))
        spo2 = int(match.group(3))

        # Update the deques for moving average
        temperature_values.append(temperature)
        pulse_rate_values.append(pulse_rate)
        spo2_values.append(spo2)

        return True
    else:
        print(f"Invalid input format: {line}")
        return False

def calculate_statistics(temperature_values, pulse_rate_values, spo2_values):
    max_temperature = max(temperature_values) if temperature_values else 0
    min_temperature = min(temperature_values) if temperature_values else 0
    avg_temperature = sum(temperature_values) / len(temperature_values) if temperature_values else 0

    max_pulse_rate = max(pulse_rate_values) if pulse_rate_values else 0
    min_pulse_rate = min(pulse_rate_values) if pulse_rate_values else 0
    avg_pulse_rate = sum(pulse_rate_values) / len(pulse_rate_values) if pulse_rate_values else 0

    max_spo2 = max(spo2_values) if spo2_values else 0
    min_spo2 = min(spo2_values) if spo2_values else 0
    avg_spo2 = sum(spo2_values) / len(spo2_values) if spo2_values else 0

    return {
        "max_temperature": max_temperature,
        "min_temperature": min_temperature,
        "avg_temperature": avg_temperature,
        "max_pulse_rate": max_pulse_rate,
        "min_pulse_rate": min_pulse_rate,
        "avg_pulse_rate": avg_pulse_rate,
        "max_spo2": max_spo2,
        "min_spo2": min_spo2,
        "avg_spo2": avg_spo2,
    }

def main():
    temperature_values = deque(maxlen=5)
    pulse_rate_values = deque(maxlen=5)
    spo2_values = deque(maxlen=5)

    print("Enter 50 values in the format 'Temperature: <value> PulseRate: <value> SPO2: <value>':")

    for _ in range(50):
        line = input()
        valid = process_line(line, temperature_values, pulse_rate_values, spo2_values)

        if valid:
            # Calculate statistics after each valid input
            stats = calculate_statistics(temperature_values, pulse_rate_values, spo2_values)
            print("------------------------------------------------\n")
            
            print(f"Max Temperature: {stats['max_temperature']:.2f}, Min Temperature: {stats['min_temperature']:.2f}, "
                  f"Avg Temperature (last 5): {stats['avg_temperature']:.2f}")
            print(f"Max Pulse Rate: {stats['max_pulse_rate']}, Min Pulse Rate: {stats['min_pulse_rate']}, "
                  f"Avg Pulse Rate (last 5): {stats['avg_pulse_rate']:.2f}")
            print(f"Max SPO2: {stats['max_spo2']}, Min SPO2: {stats['min_spo2']}, "
                  f"Avg SPO2 (last 5): {stats['avg_spo2']:.2f}")
        else:
            print("Exiting due to invalid input.")
            return

if __name__ == "__main__":
    main()

