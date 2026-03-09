**1. The core components of Linux (kernel, user space, init/systemd)**
=> In Linux architecture, the system is mainly divided into three core components: Kernel, User Space, Init System (init / systemd)
**1. Kernel (Core of the OS)**
The Linux kernel is the heart of the operating system. It directly interacts with the hardware.
**Main Responsibilities :** Process management,Memory management,Device management,File system management,Networking.
**Example :** When you run a command like:
cat file.txt

**Flow:**
User Command → Shell → Kernel → Disk → Kernel → Output

The kernel reads the file from disk and returns it to the terminal.

**Kernel Subsystems**
**Important parts of the kernel include:**
Process scheduler – decides which process runs
Memory manager – handles RAM
VFS (Virtual File System) – manages file systems
Device drivers – communicate with hardware
Networking stack – handles network packets

**2. User Space**
User space is where applications and user programs run.
These programs cannot directly access hardware; they must go through the kernel using system calls.
**Examples of User Space Programs**
Shell (bash)
Text editors (vim, nano)
Web servers (nginx, apache)
Databases (mysql)
CLI tools (ls, cp, grep)

**Example command:**
ls

**Flow:**
User Command → Shell executes program → Program requests file list from kernel → Kernel reads filesystem → Output shown to user.

**3. Init System (init / systemd)**
The init system is the first user-space process that starts after the kernel boots.
**Process ID:**
PID 1

**Responsibilities**
Start system services
Manage background services (daemons)
Handle system startup
Control service dependencies

**Example services started by systemd:**
ssh
networking
cron
docker

+----------------------------+
|        User Space          |
|----------------------------|
| Applications (nginx, vim)  |
| Shell (bash)               |
| Libraries (glibc)          |
+----------------------------+
|        Init System         |
|        systemd (PID 1)     |
+----------------------------+
|           Kernel           |
| Process | Memory | Drivers |
| Filesystem | Network       |
+----------------------------+
|           Hardware         |
| CPU | RAM | Disk | NIC     |
+----------------------------+

| Component      | Role                                 |
| -------------- | ------------------------------------ |
| Kernel         | Talks to/controls hardware           |
| User Space     | Runs applications/programs           |
| Init / systemd | Starts and manages system services   |

**2. How processes are created and managed in linux**
In Linux, process creation and management is handled mainly by the Linux kernel. A process is simply a running instance of a program.
**Example:**
When you run vim, nginx, or ls, Linux creates a process for that program.

     **1. What is a Process in Linux?**
**A process contains:**
Program code
Process ID (PID)
Memory allocation
Open files
CPU state
Environment variables

**Example:**
ps aux

Shows all running processes in the system.
**Example output:**

**USER   PID  CPU  MEM  COMMAND**
root     1  0.0  0.1  systemd
rahul  2450 0.1  0.3  bash
rahul  3021 0.0  0.1  vim

       **2. How Processes Are Created**
Processes are usually created using two main system calls:
1️⃣ fork()
fork() creates a child process by copying the parent process.
**Example flow:**
Parent Process (bash)
        │
        └── fork()
              │
              └── Child Process
**Example:**
When you run:
ls

**Steps:**
Shell (bash) runs
bash calls fork()
Child process created
Child runs ls

**3. What systemd does and why it matters**
systemd is the init system and service manager used by most modern Linux distributions.
It is the first process started after the kernel boots and it runs with PID 1.
It manages system startup, services, and background processes (daemons).
