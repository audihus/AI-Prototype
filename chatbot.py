import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json
from datetime import datetime
import re

# Data rules (simulasi rules.json)
# Data rules (simulasi rules.json)
with open('data.json', 'r') as file:
    RULES_DATA = json.load(file)
print(f"Data from file: {RULES_DATA[0]['area']}")

# Keyword mapping for topic detection
TOPIC_KEYWORDS = {
    "vape": ["vape", "vaping", "e-cigarette", "rokok elektrik"],
    "thr": ["thr", "holiday pay", "holiday bonus", "tunjangan hari raya", "bonus lebaran"],
    "parking": ["parking", "parkir", "park"],
    "leave": ["leave", "annual leave", "cuti", "vacation"]
}

class LegalChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("🏛️ LegalMate - Your Legal Assistant")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f4f8")
        
        self.current_city = "Yogyakarta"  # Default location
        self.chat_history = []
        
        self.setup_ui()
        self.greet_user()
    
    def setup_ui(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=80)
        header_frame.pack(fill="x", pady=(0, 10))
        header_frame.pack_propagate(False)
        
        # Avatar/Maskot
        avatar_label = tk.Label(
            header_frame, 
            text="👨‍⚖️", 
            font=("Arial", 40),
            bg="#2c3e50"
        )
        avatar_label.pack(side="left", padx=20, pady=10)
        
        # Title and subtitle
        title_frame = tk.Frame(header_frame, bg="#2c3e50")
        title_frame.pack(side="left", fill="both", expand=True, pady=15)
        
        title = tk.Label(
            title_frame,
            text="LegalMate Assistant",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title.pack(anchor="w")
        
        subtitle = tk.Label(
            title_frame,
            text="Your Smart Legal Companion 🇮🇩",
            font=("Arial", 10),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        subtitle.pack(anchor="w")
        
        # Location Frame
        location_frame = tk.Frame(self.root, bg="#f0f4f8")
        location_frame.pack(fill="x", padx=20, pady=(0, 10))
        
        tk.Label(
            location_frame,
            text="📍 Your Location:",
            font=("Arial", 10, "bold"),
            bg="#f0f4f8"
        ).pack(side="left")
        
        self.city_var = tk.StringVar(value=self.current_city)
        city_combo = ttk.Combobox(
            location_frame,
            textvariable=self.city_var,
            values=["Jakarta", "Bandung", "Yogyakarta", "Surabaya", "National"],
            state="readonly",
            width=15
        )
        city_combo.pack(side="left", padx=10)
        city_combo.bind("<<ComboboxSelected>>", self.on_city_change)
        
        # Chat Display
        chat_frame = tk.Frame(self.root, bg="white", relief="solid", borderwidth=1)
        chat_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=("Arial", 10),
            bg="white",
            relief="flat",
            state="disabled"
        )
        self.chat_display.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Configure tags for styling
        self.chat_display.tag_config("bot", foreground="#2c3e50", font=("Arial", 10))
        self.chat_display.tag_config("user", foreground="#27ae60", font=("Arial", 10, "bold"))
        self.chat_display.tag_config("citation", foreground="#e74c3c", font=("Arial", 9, "italic"))
        self.chat_display.tag_config("status", foreground="#3498db", font=("Arial", 9))
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg="#f0f4f8")
        input_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.input_field = tk.Entry(
            input_frame,
            font=("Arial", 11),
            relief="solid",
            borderwidth=1
        )
        self.input_field.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 10))
        self.input_field.bind("<Return>", lambda e: self.send_message())
        
        send_button = tk.Button(
            input_frame,
            text="Send 📨",
            command=self.send_message,
            bg="#3498db",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20
        )
        send_button.pack(side="right")
        
        # Quick buttons
        quick_frame = tk.Frame(self.root, bg="#f0f4f8")
        quick_frame.pack(fill="x", padx=20, pady=(0, 10))
        
        tk.Label(
            quick_frame,
            text="Popular Topics:",
            font=("Arial", 9),
            bg="#f0f4f8"
        ).pack(side="left", padx=(0, 10))
        
        quick_buttons = [
            ("🚬 Vape", "Is vaping allowed here?"),
            ("💰 THR", "When must THR be paid?"),
            ("🅿️ Parking", "What are the parking rules?")
        ]
        
        for label, query in quick_buttons:
            btn = tk.Button(
                quick_frame,
                text=label,
                command=lambda q=query: self.quick_ask(q),
                bg="#ecf0f1",
                relief="flat",
                cursor="hand2",
                font=("Arial", 8),
                padx=10,
                pady=5
            )
            btn.pack(side="left", padx=5)
    
    def greet_user(self):
        greeting = f"👋 Hello! I'm LegalMate Assistant.\n\nI'm ready to help you find legal regulation information in Indonesia.\n\n📍 Your current location: {self.current_city}\n\nFeel free to ask anything about local or national regulations! 😊"
        self.add_message("bot", greeting)
    
    def on_city_change(self, event=None):
        self.current_city = self.city_var.get()
        self.add_message("bot", f"📍 Location changed to: {self.current_city}")
    
    def quick_ask(self, query):
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, query)
        self.send_message()
    
    def send_message(self):
        query = self.input_field.get().strip()
        if not query:
            return
        
        self.add_message("user", query)
        self.input_field.delete(0, tk.END)
        
        # Process query
        response = self.process_query(query)
        self.add_message("bot", response)
    
    def add_message(self, sender, message):
        self.chat_display.config(state="normal")
        
        if sender == "user":
            self.chat_display.insert(tk.END, "\n🙋 You: ", "user")
            self.chat_display.insert(tk.END, f"{message}\n")
        else:
            self.chat_display.insert(tk.END, "\n👨‍⚖️ Assistant: ", "bot")
            
            # Parse citation and status
            lines = message.split("\n")
            for line in lines:
                if line.startswith("📜"):
                    self.chat_display.insert(tk.END, f"{line}\n", "citation")
                elif line.startswith("✅") or line.startswith("📅"):
                    self.chat_display.insert(tk.END, f"{line}\n", "status")
                else:
                    self.chat_display.insert(tk.END, f"{line}\n", "bot")
        
        self.chat_display.config(state="disabled")
        self.chat_display.see(tk.END)
    
    def detect_topic(self, query):
        """Detect topic from query using keywords"""
        query_lower = query.lower()
        
        for topic, keywords in TOPIC_KEYWORDS.items():
            for keyword in keywords:
                if keyword in query_lower:
                    return topic
        return None
    
    def process_query(self, query):
        """Process user query and return response"""
        topic = self.detect_topic(query)
        
        if not topic:
            return "🤔 Sorry, I don't understand your question yet. Try asking about:\n- Vaping/e-cigarettes\n- THR (Holiday Pay)\n- Parking\n- Employee leave"
        
        # Filter rules by topic
        matching_rules = [r for r in RULES_DATA if r["topic"] == topic]
        
        if not matching_rules:
            return f"❌ Sorry, I don't have data about {topic} yet."
        
        # Filter by location (prefer local, fallback to national)
        local_rules = [r for r in matching_rules if r["area"] == self.current_city]
        national_rules = [r for r in matching_rules if r["area"] == "National"]
        
        if local_rules:
            rule = local_rules[0]
            location_note = f"in {self.current_city}"
        elif national_rules:
            rule = national_rules[0]
            location_note = "nationally"
        else:
            return f"❌ No regulations found about {topic} for {self.current_city}. Try changing location or check official sources."
        
        # Compose response
        response = f"💡 Information about {topic.upper()} {location_note}:\n\n"
        response += f"{rule['snippet']}\n\n"
        response += f"📜 Legal Basis: {rule['citation']}\n"
        response += f"✅ Status: {rule['status'].replace('_', ' ').title()}\n"
        response += f"📅 Effective since: {rule['effective_date']}\n"
        response += f"🆔 Document ID: {rule['doc_id']}"
        
        return response

# Run application
if __name__ == "__main__":
    root = tk.Tk()
    app = LegalChatbot(root)
    root.mainloop()