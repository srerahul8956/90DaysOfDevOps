1. The core components of Linux (kernel, user space, init/systemd)
=> In Linux architecture, the system is mainly divided into three core components: Kernel, User Space, Init System (init / systemd)
The Linux kernel is the heart of the operating system. It directly interacts with the hardware.
**Main Responsibilities :** Process management,Memory management,Device management,File system management,Networking.
**Example :** When you run a command like:
cat file.txt

**Flow:**
User Command → Shell → Kernel → Disk → Kernel → Output

The kernel reads the file from disk and returns it to the terminal.

