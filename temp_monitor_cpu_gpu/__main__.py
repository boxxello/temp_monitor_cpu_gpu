import time
import clr # the pythonnet module.


from temp_monitor_cpu_gpu.utils_files import resolve_path


def get_cpu_temp():
    for hardware in c.Hardware:
        if hardware.HardwareType == OpenHardwareMonitor.Hardware.HardwareType.CPU:
            hardware.Update()
            for sensor in hardware.Sensors:
                if sensor.SensorType == OpenHardwareMonitor.Hardware.SensorType.Temperature:
                    return sensor.Value
def get_gpu_temp():
    for hardware in c.Hardware:
        if hardware.HardwareType == OpenHardwareMonitor.Hardware.HardwareType.GpuNvidia:
            hardware.Update()
            for sensor in hardware.Sensors:
                if sensor.SensorType == OpenHardwareMonitor.Hardware.SensorType.Temperature:
                    return sensor.Value
def main():
    while True:
        print(f"CPU: {get_cpu_temp()} GPU: {get_gpu_temp()}")
        time.sleep(5)

if __name__ == '__main__':
    #here we do reference the OpenHardware dll which is going to allow us to monitor
    #the temps
    clr.AddReference(rf"{resolve_path('./needed_dlls/OpenHardwareMonitorLib')}")
    import OpenHardwareMonitor
    from OpenHardwareMonitor.Hardware import Computer
    c = Computer()
    c.CPUEnabled = True  # get the info about CPU
    c.GPUEnabled = True  # get the info about GPU
    c.Open()
    main()
