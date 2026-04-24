# Run PyGame through WSL2 in 3 Steps

> **Prerequisite:** WSL2 must be installed. If you haven't set it up yet, follow the [official installation guide](https://docs.microsoft.com/en-us/windows/wsl/install).

## Background

When you run a GUI application on Linux, it doesn't draw pixels directly to the screen. Instead, it talks to an **X Window System (X11) server** — a separate process responsible for managing windows and rendering graphics. The application (the "client") sends drawing commands to the server, and the server handles displaying them.

WSL2 runs Linux inside a lightweight virtual machine, which means it has no display of its own. To show GUI windows on your Windows desktop, you need to run an X server *on the Windows side* and tell WSL2 to send its display output there.

**VcXsrv** is a free, open-source X Window server for Windows. It runs in the background and accepts display connections from WSL2, acting as the bridge that makes Linux GUI apps like PyGame appear as normal windows on your desktop.

---

## Step 1: Install VcXsrv

1. [Download and install VcXsrv](https://sourceforge.net/projects/vcxsrv/)
2. After installation, open the **Start Menu** and launch **XLaunch**
3. Follow the configuration screens:

   | Screen | Setting |
   |--------|---------|
   | Display settings | Select **Multiple windows** and set display number to **-1** |
   | Client startup | Select **Start no client** |
   | Extra settings | Check **Disable access control** |

4. Click **Finish**. A new icon will appear in the system tray.

### Reading the System Tray Indicator

You'll see something like `DESKTOP-E5TN54K:0.0 - 0 clients`. Here's what it means:

| Part | Meaning |
|------|---------|
| `DESKTOP-E5TN54K` | Your computer's hostname |
| `:` | "at" |
| `0.0` | `<display>.<screen>` — display 0, screen 0 |
| `0 clients` | Number of clients connected (0 when idle) |

---

## Step 2: Configure `~/.bashrc`

WSL2 needs to know the IP address of the Windows host in order to reach the X Window server.

> **Why not just use `:0.0`?**  
> In WSL1, Linux and Windows shared the same IP, so `localhost:0.0` worked fine. In WSL2, they have **separate IP addresses**, so you must point `DISPLAY` at the Windows host IP explicitly.

### Find the Windows Host IP

Run this command inside WSL2:

```bash
ip route show | grep default | awk '{print $3}'
```

This prints the IP address of your Windows machine (e.g., `172.31.160.1`).

### Add to `~/.bashrc`

Open the file in nano:

```bash
nano ~/.bashrc
```

Scroll to the very bottom using the arrow keys and add this line:

```bash
export DISPLAY=$(ip route show | grep default | awk '{print $3}'):0.0
```

Save and exit by pressing `Ctrl+O` then `Enter` to confirm, then `Ctrl+X` to close nano.

This is equivalent to writing `export DISPLAY=172.31.160.1:0.0` (with your actual IP). The format is `[host]:<display>.<screen>`.

### Apply the Changes

After saving the file, reload your shell configuration so the new variable takes effect in your current session:

```bash
source ~/.bashrc
```

> Without this step, the `DISPLAY` variable won't be set until you open a new terminal window.

---

## Step 3: Test and Run

Install the X11 test apps:

```bash
sudo apt update
sudo apt install x11-apps
```

Test your setup by running:

```bash
xeyes
```

If a window with animated eyes appears, your X Window connection is working correctly.

You can now run your PyGame application:

```bash
python your_pygame_app.py
```

---

## References

- [Run Graphical Linux Desktop Applications from Windows 10 Bash Shell](https://techcommunity.microsoft.com/t5/windows-dev-appconsult/running-wsl-gui-apps-on-windows-10/ba-p/1493242)
- [PyGame Documentation](https://www.pygame.org/docs/)
- [WSL2 Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
