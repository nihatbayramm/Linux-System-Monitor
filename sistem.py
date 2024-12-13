import psutil
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rcParams.update({
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.figsize': (10, 8),
    'lines.linewidth': 3,
    'font.size': 12,
    'font.family': 'serif'
})

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_network_usage():
    net = psutil.net_io_counters()
    return net.bytes_sent / (1024 * 1024), net.bytes_recv / (1024 * 1024)

fig, ax = plt.subplots(4, 1, figsize=(10, 8))
ax[0].set_title("CPU Kullanımı (%)")
ax[1].set_title("Bellek Kullanımı (%)")
ax[2].set_title("Disk Kullanımı (%)")
ax[3].set_title("Ağ Kullanımı (MB)")

cpu_line, = ax[0].plot([], [], label="CPU", color='tab:red')
mem_line, = ax[1].plot([], [], label="Bellek", color='tab:red')
disk_line, = ax[2].plot([], [], label="Disk", color='tab:red')
net_line, = ax[3].plot([], [], label="Ağ", color='tab:red')

for a in ax:
    a.set_xlim(0, 50)
    a.set_ylim(0, 100)
    a.grid(True)

def update(i, cpu_data, mem_data, disk_data, net_data, cpu_line, mem_line, disk_line, net_line):
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    net_sent, net_recv = get_network_usage()

    cpu_data.append(cpu)
    mem_data.append(memory)
    disk_data.append(disk)
    net_data.append(net_sent + net_recv)

    if len(cpu_data) > 50:
        cpu_data.pop(0)
        mem_data.pop(0)
        disk_data.pop(0)
        net_data.pop(0)

    cpu_line.set_data(range(len(cpu_data)), cpu_data)
    mem_line.set_data(range(len(mem_data)), mem_data)
    disk_line.set_data(range(len(disk_data)), disk_data)
    net_line.set_data(range(len(net_data)), net_data)

    ax[0].text(0.95, 0.9, f'{cpu:.1f}%', ha='right', va='top', transform=ax[0].transAxes, color='red', fontsize=14, fontweight='bold')
    ax[1].text(0.95, 0.9, f'{memory:.1f}%', ha='right', va='top', transform=ax[1].transAxes, color='red', fontsize=14, fontweight='bold')
    ax[2].text(0.95, 0.9, f'{disk:.1f}%', ha='right', va='top', transform=ax[2].transAxes, color='red', fontsize=14, fontweight='bold')
    ax[3].text(0.95, 0.9, f'{net_sent + net_recv:.1f} MB', ha='right', va='top', transform=ax[3].transAxes, color='red', fontsize=14, fontweight='bold')

    return cpu_line, mem_line, disk_line, net_line

cpu_data = []
mem_data = []
disk_data = []
net_data = []

ani = animation.FuncAnimation(fig, update, fargs=(cpu_data, mem_data, disk_data, net_data, cpu_line, mem_line, disk_line, net_line),
                              interval=1000, blit=False)

plt.tight_layout()
plt.show()
