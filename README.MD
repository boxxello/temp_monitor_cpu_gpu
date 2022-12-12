# Temp Monitor
This project is a simple temperature monitor for Windows OS.
The scope for this project is to make IETS 500 run at lower speeds when the GPU/CPU temps are low.


## Installation
1. Install Python 3.6 or higher
2. Install the following package:
    * `pip install pythonnet`

## Usage
1. Activate the virtual environment
2. Open a terminal with admin rights (we don't actually need it for GPU temps, but we do for CPU temps as of 22H2)
3. Run the `main.py` file or the module with the following command:
    * `python -m temp_monitor_cpu_gpu`


## Documentation about the dll
You can either use the dll I am including in this project or you can download the dll from the following [link](https://openhardwaremonitor.org/downloads/):
and extract the dll from the zip file and put it into the needed_dlls dir.

This is the link for the GitHub repo of the project: [link](https://github.com/openhardwaremonitor/openhardwaremonitor).


## Contributing
Pull requests are welcome. 
There's an active discussion on this [link](https://www.reddit.com/r/GamingLaptops/comments/zjjsoo/iets_500_automatic_controlling_fans/)