#ifndef SENDER_H
#define SENDER_H

struct SensorData {
    float temperature;
    int pulseRate;
    int spo2;
};

class Sender {
public:
    Sender();
    // Function to generate and send sensor readings
    void sendReadings();

private:
    // Helper function to generate random sensor data
    SensorData generateRandomData();
};

#endif // SENDER_H
