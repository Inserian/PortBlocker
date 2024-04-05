import socket
import tkinter as tk
from tkinter import ttk

class PortBlocker:
    def __init__(self, master):
        self.master = master
        self.master.title("Port Blocker")
        self.master.geometry("600x400")

        # Using ttk for a more modern look
        self.ports_label = ttk.Label(self.master, text="Enter ports to check, block, or unblock, separated by commas:")
        self.ports_label.pack(pady=10)

        self.ports_entry = ttk.Entry(self.master, width=50)
        self.ports_entry.pack(pady=5)

        self.buttons_frame = ttk.Frame(self.master)
        self.buttons_frame.pack(pady=10)

        self.check_button = ttk.Button(self.buttons_frame, text="Check Ports", command=self.check_ports)
        self.check_button.pack(side=tk.LEFT, padx=5)

        self.block_button = ttk.Button(self.buttons_frame, text="Block Ports", command=self.block_ports)
        self.block_button.pack(side=tk.LEFT, padx=5)

        self.unblock_button = ttk.Button(self.buttons_frame, text="Unblock Ports", command=self.unblock_ports)
        self.unblock_button.pack(side=tk.LEFT, padx=5)

        self.status_label = ttk.Label(self.master, text="")
        self.status_label.pack(pady=5)

        self.output_frame = ttk.Frame(self.master)
        self.output_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.output_text = tk.Text(self.output_frame, height=10)
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.output_frame, orient="vertical", command=self.output_text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.configure(yscrollcommand=self.scrollbar.set)

    def check_ports(self):
        ports = self.ports_entry.get().split(',')
        self.output_text.delete('1.0', tk.END)
        for port_str in ports:
            port_str = port_str.strip()
            if not port_str.isdigit():
                self.output_text.insert(tk.END, f"'{port_str}' is not a valid port number.\n")
                continue
            port = int(port_str)
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(1)
                    result = sock.connect_ex(('localhost', port))
                    if result == 0:
                        self.output_text.insert(tk.END, f"Port {port} is open.\n")
                    else:
                        self.output_text.insert(tk.END, f"Port {port} is closed or not responding.\n")
            except Exception as e:
                self.output_text.insert(tk.END, f"Error checking port {port}: {e}\n")

    def block_ports(self):
        self.status_label.config(text="Blocking ports functionality not implemented.")

    def unblock_ports(self):
        self.status_label.config(text="Unblocking ports functionality not implemented.")

def main():
    root = tk.Tk()
    app = PortBlocker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
