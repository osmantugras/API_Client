import tkinter as tk
import requests
import json

class APIClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("API Client")
        master.geometry("800x600")

        # URL Label and Entry
        self.url_label = tk.Label(master, text="API URL")
        self.url_label.pack()
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.pack()

        # Token Label and Entry
        self.token_label = tk.Label(master, text="API Token")
        self.token_label.pack()
        self.token_entry = tk.Entry(master, width=50)
        self.token_entry.pack()

        # JSON Label and Textbox
        self.json_label = tk.Label(master, text="JSON Data")
        self.json_label.pack()
        self.json_text = tk.Text(master, height=10, width=70)
        self.json_text.pack()

        # Method Radiobuttons
        self.method_label = tk.Label(master, text="HTTP Method")
        self.method_label.pack()

        self.method_var = tk.StringVar(value="GET")

        self.get_radiobutton = tk.Radiobutton(master, text="GET", variable=self.method_var, value="GET")
        self.get_radiobutton.pack(anchor=tk.W)

        self.post_radiobutton = tk.Radiobutton(master, text="POST", variable=self.method_var, value="POST")
        self.post_radiobutton.pack(anchor=tk.W)

        # Execute Button
        self.execute_button = tk.Button(master, text="Execute", command=self.execute)
        self.execute_button.pack(pady=10)

        # Result Label and Textbox
        self.result_label = tk.Label(master, text="Result")
        self.result_label.pack()

        self.result_text = tk.Text(master, height=20, width=70)
        self.result_text.pack()

    def execute(self):
        url = self.url_entry.get()
        token = self.token_entry.get()
        method = self.method_var.get()
        headers = {"Authorization": f"Bearer {token}"}
        data = None

        if method == "POST":
            try:
                data = json.loads(self.json_text.get("1.0", tk.END))
            except json.JSONDecodeError as e:
                self.result_text.insert(tk.END, f"Error: Invalid JSON Data - {e}")
                return

        requests.packages.urllib3.disable_warnings()
        response = requests.request(method=method, url=url, headers=headers, json=data, verify=False)

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, f"HTTP Status Code: {response.status_code}\n\n")
        self.result_text.insert(tk.END, response.text)

root = tk.Tk()
my_gui = APIClientGUI(root)
root.mainloop()
