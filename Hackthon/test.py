import tkinter as tk
from datetime import datetime

class AnxietyCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("焦慮次數追蹤器")
        
        self.count = 0
        
        # 嘗試從文件加載計數
        try:
            with open("anxiety_count.txt", "r") as f:
                self.count = int(f.read())
        except:
            pass
        
        # 創建界面
        self.label = tk.Label(root, text=f"焦慮次數: {self.count}", font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.button = tk.Button(
            root, 
            text="我現在感到焦慮", 
            command=self.increment_count,
            bg="#ff6b6b",
            fg="white",
            font=("Arial", 16),
            padx=20,
            pady=10
        )
        self.button.pack()
        
        # 記錄歷史
        self.log_text = tk.Text(root, height=10, width=40)
        self.log_text.pack(pady=20)
        
        # 加載歷史記錄
        try:
            with open("anxiety_log.txt", "r") as f:
                self.log_text.insert(tk.END, f.read())
        except:
            pass
    
    def increment_count(self):
        self.count += 1
        self.label.config(text=f"焦慮次數: {self.count}")
        
        # 記錄時間
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_text.insert(tk.END, f"{now}\n")
        self.log_text.see(tk.END)
        
        # 保存到文件
        with open("anxiety_count.txt", "w") as f:
            f.write(str(self.count))
            
        with open("anxiety_log.txt", "a") as f:
            f.write(f"{now}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnxietyCounter(root)
    root.mainloop()