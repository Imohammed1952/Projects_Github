// Build a user-mode test app that:
// Tries to open \\.\FakeDevice

// Checks for errors

// Prepares a struct payload and calls DeviceIoControl

// Handles the "device not found" gracefully

#include <windows.h>
#include <iostream>
#include <string>
#include <cstdint>

#define MY_IOCTL_CODE CTL_CODE(FILE_DEVICE_UNKNOWN, 0x800, METHOD_BUFFERED, FILE_ANY_ACCESS)


struct packet{
    int ID;
    char msg[16];
    double value;
};

int main() {
    std::cout << "=== Week 1: C++ Systems Review Assignment ===" << std::endl;

    // --- You implement TODOs above here ---

    std::cout << "\n[~~~Step 1] Define a struct and fill a raw memory buffer with it." << std::endl;
    void* buffer = malloc(sizeof(packet));
    if(!buffer){
        std::cerr << "Failed to create buffer." << std::endl;
        return 1;
    }
    packet* pkt = reinterpret_cast<packet*>(buffer);
    pkt->ID = 1001;
    strcpy_s(pkt-> msg, "learner pjkt");
    pkt->value = 3.14;

    std::cout << "Packet Id = " << pkt->ID << std::endl;
    std::cout << "Packet msg = " << pkt->msg << std::endl;
    std::cout << "Packet value = " << pkt->value << std::endl;


    std::cout << "\n[~~~Step 2] Attempting to open device: \\\\.\\MyLearningDevice" << std::endl;


    HANDLE hDevice = CreateFileA(
        "\\\\.\\MyLearningDevice", // Device name you'll eventually create
        GENERIC_READ | GENERIC_WRITE,
        0,
        nullptr,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        nullptr
    );

    if (hDevice == INVALID_HANDLE_VALUE) {
        DWORD err = GetLastError();
        std::cerr << "[ERROR] CreateFile failed. Code: " << err << std::endl;

        char* errMsg = nullptr;
        FormatMessageA(
            FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS,
            nullptr,
            err,
            0,
            (LPSTR)&errMsg,
            0,
            nullptr
        );

        if (errMsg) {
            std::cerr << "[ERROR MESSAGE] " << errMsg;
            LocalFree(errMsg);
        }

        free(buffer);
        return 1;
    }

    std::cout << "[SUCCESS] Device opened.\n";

    // Simulate where your DeviceIoControl would go...
    std::cout << "\n[~~~Step 3] TODO: Call DeviceIoControl here." << std::endl;

    DWORD bytesReturned = 0;
    BOOL success = DeviceIoControl(
        hDevice,
        MY_IOCTL_CODE,
        buffer,
        sizeof(packet),
        nullptr,
        0,
        &bytesReturned,
        nullptr
    );


    if (!success) {
        std::cerr << "DeviceIoControl failed. Error: " << GetLastError() << std::endl;
    } else {
        std::cout << "DeviceIoControl succeeded!" << std::endl;
    }


    CloseHandle(hDevice);
    free(buffer);
    return 0;
}
