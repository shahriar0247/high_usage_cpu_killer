import psutil
import time
import os


dict_pids = {
    p.info["pid"]: p.info["name"]
    for p in psutil.process_iter(attrs=["pid", "name"])
}

pid_list = []


def cpu_still_high(pid):
    a = 0
    while pid.cpu_percent() > 40:
        time.sleep(2)
        a = a+1
        if a > 10:
            os.system("taskkill /PID " + str(pid))
            print("killed",pid)

for a in range(0,len(dict_pids)):
    if list(dict_pids.values())[a] == "chrome.exe":
        pid_list.append(psutil.Process((list(dict_pids.keys())[a])))
            


while True:
    time.sleep(1)
    for b in range(0, len(pid_list)):
        cpu = pid_list[b].cpu_percent()
        if cpu != 0.0:
            if (cpu) > 40.0:
                time.sleep(2)
                cpu_still_high(pid_list[b])

# p = psutil.Process(PID)
# p.cpu_percent