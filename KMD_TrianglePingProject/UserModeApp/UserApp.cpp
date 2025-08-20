
#include <windows.h>
#include <iostream>
#include <cstdint>
#include <string>

#define IOCTL_PING CTL_CODE(FILE_DEVICE_UNKNOWN, 0x800, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_DRAW_TRIANGLE CTL_CODE(FILE_DEVICE_UNKNOWN, 0x801, METHOD_BUFFERED, FILE_ANY_ACCESS)

struct DrawTrianglePacket {
    uint32_t commandID;
    float vertices[9]; // 3 vertices
    char debugName[32];
};

int main() {
    HANDLE hDevice = CreateFileA(
        "\\\\.\\MyLearningDevice",
        GENERIC_READ | GENERIC_WRITE,
        0, nullptr, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, nullptr
    );

    if (hDevice == INVALID_HANDLE_VALUE) {
        std::cerr << "Failed to open device. Error: " << GetLastError() << std::endl;
        return 1;
    }

    std::cout << "[User] Sending PING..." << std::endl;
    DWORD bytesReturned = 0;
    BOOL success = DeviceIoControl(
        hDevice, IOCTL_PING,
        nullptr, 0,
        nullptr, 0,
        &bytesReturned, nullptr
    );

    if (!success) std::cerr << "[User] Ping failed. Error: " << GetLastError() << std::endl;
    else std::cout << "[User] Ping succeeded." << std::endl;

    std::cout << "\n[User] Sending DrawTrianglePacket..." << std::endl;
    DrawTrianglePacket pkt = {
        1,
        { 0.0f, 0.5f, 0.0f,  -0.5f, -0.5f, 0.0f,  0.5f, -0.5f, 0.0f },
        "DemoTriangle"
    };

    success = DeviceIoControl(
        hDevice, IOCTL_DRAW_TRIANGLE,
        &pkt, sizeof(pkt),
        nullptr, 0,
        &bytesReturned, nullptr
    );

    if (!success) std::cerr << "[User] DrawTriangle failed. Error: " << GetLastError() << std::endl;
    else std::cout << "[User] Triangle draw packet sent." << std::endl;

    CloseHandle(hDevice);
    return 0;
}
