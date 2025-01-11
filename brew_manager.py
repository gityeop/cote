import os
import subprocess
import shutil
from operator import itemgetter
import curses


def get_package_size(package_path):
    try:
        size = 0
        for root, dirs, files in os.walk(package_path):
            for file in files:
                filepath = os.path.join(root, file)
                size += os.path.getsize(filepath)
        return size
    except Exception as e:
        return 0


def list_brew_packages_sorted_by_size():
    try:
        cellar_path = (
            subprocess.check_output(["brew", "--cellar"]).decode("utf-8").strip()
        )
        packages = []
        for package in os.listdir(cellar_path):
            package_path = os.path.join(cellar_path, package)
            if os.path.isdir(package_path):
                size = get_package_size(package_path)
                packages.append((package, size))
        return sorted(packages, key=itemgetter(1), reverse=True)
    except Exception as e:
        print("Error listing brew packages:", e)
        return []


def navigate_packages(stdscr, packages):
    index = 0
    curses.curs_set(0)  # Hide cursor

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Render packages list
        stdscr.addstr(0, 0, "Brew Packages (sorted by size):")
        for i, (package, size) in enumerate(packages):
            if i >= height - 3:
                break  # Prevent overflow
            arrow = "->" if i == index else "  "
            line = f"{arrow} {package} ({size / (1024 * 1024):.2f} MB)"
            stdscr.addstr(i + 1, 0, line[: width - 1])  # Truncate if necessary

        # Render commands
        commands = "Commands: [Up/Down Arrow] Navigate, [Enter] Delete, [q] Quit"
        stdscr.addstr(height - 2, 0, commands[: width - 1])  # Truncate if necessary

        key = stdscr.getch()

        if key == ord("q"):
            break
        elif key == curses.KEY_UP:
            index = (index - 1) % len(packages)
        elif key == curses.KEY_DOWN:
            index = (index + 1) % len(packages)
        elif key == ord("\n"):  # Enter key
            package, _ = packages[index]
            confirm_msg = f"Are you sure you want to delete {package}? (y/n): "
            stdscr.addstr(height - 1, 0, confirm_msg[: width - 1])
            stdscr.refresh()
            confirm = stdscr.getch()
            if confirm == ord("y"):
                try:
                    subprocess.run(["brew", "uninstall", package], check=True)
                    packages.pop(index)
                    if index >= len(packages):
                        index = max(0, len(packages) - 1)
                except subprocess.CalledProcessError as e:
                    error_msg = f"Error deleting {package}: {e}"
                    stdscr.addstr(height - 1, 0, error_msg[: width - 1])
                    stdscr.refresh()
                    stdscr.getch()
        stdscr.refresh()


def main(stdscr):
    packages = list_brew_packages_sorted_by_size()
    if not packages:
        stdscr.addstr("No Brew packages found.\n")
        stdscr.refresh()
        stdscr.getch()
        return
    navigate_packages(stdscr, packages)


if __name__ == "__main__":
    curses.wrapper(main)
