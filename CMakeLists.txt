cmake_minimum_required(VERSION 3.10)
project(SensorProject)

# C++ standard
set(CMAKE_CXX_STANDARD 11)

# Add source files for the Sender executable
add_executable(SenderExecutable 
    src/sender.cpp 
    src/main.cpp
)

# Enable testing
enable_testing()

# Download and link GoogleTest
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/release-1.12.1.zip
)

# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

FetchContent_MakeAvailable(googletest)

# Add library for the Sender to reuse its functionality in the test
add_library(SenderLib src/sender.cpp)

# Add test executable and link it with SenderLib and GoogleTest
add_executable(test_sender tests/test_sender.cpp)
target_link_libraries(test_sender SenderLib gtest gtest_main)

# Add tests
add_test(NAME SenderTest COMMAND test_sender)
