#include <gtest/gtest.h>
#include "../src/sender.h"
#include <sstream>

// Test that Sender can generate random values
TEST(SenderTest, RandomDataTest) {
    Sender sender;
    testing::internal::CaptureStdout();
    sender.sendReadings();
    std::string output = testing::internal::GetCapturedStdout();

    // Check if output is not empty
    ASSERT_FALSE(output.empty());
}

int main(int argc, char** argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
