
#include <ntddk.h>
#include <wdf.h>
#include <initguid.h>

#define IOCTL_PING CTL_CODE(FILE_DEVICE_UNKNOWN, 0x800, METHOD_BUFFERED, FILE_ANY_ACCESS)
#define IOCTL_DRAW_TRIANGLE CTL_CODE(FILE_DEVICE_UNKNOWN, 0x801, METHOD_BUFFERED, FILE_ANY_ACCESS)

typedef struct _DrawTrianglePacket {
    UINT32 commandID;
    float vertices[9];
    CHAR debugName[32];
} DrawTrianglePacket;

VOID EvtIoDeviceControl(WDFQUEUE, WDFREQUEST, size_t, size_t, ULONG);
VOID EvtDriverContextCleanup(WDFOBJECT DriverObject) {}

extern "C" DRIVER_INITIALIZE DriverEntry;
NTSTATUS DriverEntry(PDRIVER_OBJECT DriverObject, PUNICODE_STRING RegistryPath) {
    WDF_DRIVER_CONFIG config;
    WDF_DRIVER_CONFIG_INIT(&config, WDF_NO_EVENT_CALLBACK);
    config.EvtDriverUnload = EvtDriverContextCleanup;
    return WdfDriverCreate(DriverObject, RegistryPath, WDF_NO_OBJECT_ATTRIBUTES, &config, WDF_NO_HANDLE);
}

VOID EvtIoDeviceControl(WDFQUEUE Queue, WDFREQUEST Request, size_t InputBufferLength,
                        size_t OutputBufferLength, ULONG IoControlCode) {
    UNREFERENCED_PARAMETER(Queue);
    UNREFERENCED_PARAMETER(OutputBufferLength);

    switch (IoControlCode) {
    case IOCTL_PING:
        KdPrint(("KMD: Received PING IOCTL\n"));
        WdfRequestComplete(Request, STATUS_SUCCESS);
        return;

    case IOCTL_DRAW_TRIANGLE: {
        if (InputBufferLength < sizeof(DrawTrianglePacket)) {
            WdfRequestComplete(Request, STATUS_BUFFER_TOO_SMALL);
            return;
        }

        DrawTrianglePacket* pkt = nullptr;
        NTSTATUS status = WdfRequestRetrieveInputBuffer(Request, sizeof(DrawTrianglePacket), (PVOID*)&pkt, nullptr);
        if (!NT_SUCCESS(status)) {
            WdfRequestComplete(Request, status);
            return;
        }

        KdPrint(("KMD: Drawing Triangle [%s]\n", pkt->debugName));
        for (int i = 0; i < 3; ++i) {
            KdPrint(("  Vertex %d: (%.2f, %.2f, %.2f)\n", i,
                     pkt->vertices[i * 3], pkt->vertices[i * 3 + 1], pkt->vertices[i * 3 + 2]));
        }

        WdfRequestComplete(Request, STATUS_SUCCESS);
        return;
    }

    default:
        WdfRequestComplete(Request, STATUS_INVALID_DEVICE_REQUEST);
        return;
    }
}
