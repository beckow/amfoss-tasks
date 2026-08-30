import psutil
import curses


REFRESH_RATE = .5


def get_processes():
    processes = []

    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            info = proc.info
            processes.append({"pid": info["pid"], "name": info["name"] or "Unknown","cpu": info["cpu_percent"] or 0.0,"memory": info["memory_percent"] or 0.0,})

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes


def header(stdscr):
    stdscr.addstr(0, 0, "Straw Hat Process Monitor")
    stdscr.addstr(
        2,0,"PID       NAME              CPU       MEMORY",curses.A_BOLD)

def draw_processes(stdscr,processes,scroll):
    height, width = stdscr.getmaxyx()
    visible = height -3
    visible_processes = processes[scroll:scroll+visible]
    for row, process in enumerate(visible_processes, start=3):
        if row >= height:
            break
        pid = process["pid"]
        name = process["name"][:18]
        cpu = process["cpu"]
        memory = process["memory"]
        line = f"{pid:<10}{name:<18}{cpu:>6.1f}%   {memory:>6.1f}%"
        line=line[:width-1]
        stdscr.addstr(row,0,line)


def main(stdscr):
    stdscr.timeout(int(REFRESH_RATE * 1000))
    scroll =0
    while True:
        processes =get_processes()
        stdscr.clear()
        header(stdscr)
        draw_processes(stdscr,processes,scroll)
        stdscr.refresh()
        key = stdscr.getch()
        if key == ord("q"):
            break
        elif key == curses.KEY_DOWN:
            if scroll < len(processes) - 1:
                scroll += 1

        elif key == curses.KEY_UP:
            if scroll > 0:
                scroll -= 1

curses.wrapper(main)