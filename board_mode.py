import os
import re
import select
import subprocess
import sys
import time


def serial_port():
    result = subprocess.run(
        ["ioreg", "-r", "-n", "Feather RP2040", "-l", "-w0"],
        capture_output=True,
        text=True,
        check=True,
    )
    ports = set(re.findall(r'"IOCalloutDevice" = "([^"]+)"', result.stdout))
    if len(ports) != 1:
        raise RuntimeError(f"Expected one Feather RP2040 serial port, found {len(ports)}")
    return ports.pop()


def wait_for_prompt(fd, timeout):
    output = bytearray()
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        ready, _, _ = select.select([fd], [], [], max(0, deadline - time.monotonic()))
        if ready:
            data = os.read(fd, 4096)
            output.extend(data)
            if b">>> " in output:
                return
    raise RuntimeError("CircuitPython did not enter the REPL")


def set_mode(mode):
    fd = os.open(serial_port(), os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    try:
        for _ in range(3):
            os.write(fd, b"\x03\r")
            try:
                wait_for_prompt(fd, 2)
                break
            except RuntimeError:
                continue
        else:
            raise RuntimeError("Could not interrupt CircuitPython code")

        command = (
            "import microcontroller; "
            f"microcontroller.on_next_reset(microcontroller.RunMode.{mode}); "
            "microcontroller.reset()\r"
        )
        encoded = command.encode()
        while encoded:
            encoded = encoded[os.write(fd, encoded) :]
        time.sleep(0.2)
    finally:
        os.close(fd)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"SAFE_MODE", "NORMAL"}:
        raise SystemExit("Usage: board_mode.py SAFE_MODE|NORMAL")
    set_mode(sys.argv[1])
