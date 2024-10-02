#include "sender.h"
#include <iostream>
#include <cstdlib>
#include <ctime>

Sender::Sender() {
    srand(static_cast<unsigned int>(time(0))); // Seed random number generator
}

SensorData Sender::generateRandomData() {
    SensorData data;
    data.temperature = 36.0f + static_cast<float>(rand()) / (static_cast<float>(RAND_MAX / (37.5f - 36.0f)));
    data.pulseRate = 60 + rand() % 41;  // Random between 60 and 100
    data.spo2 = 95 + rand() % 6;        // Random between 95 and 100
    return data;
}

void Sender::sendReadings() {
    for (int i = 0; i < 50; ++i) {
        SensorData data = generateRandomData();

        std::cout << "Temperature: " << data.temperature
            << " PulseRate: " << data.pulseRate
            << " SPO2: " << data.spo2 << std::endl;
    }
}
