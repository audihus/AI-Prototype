import tkinter as tk
import random

class IntelligentAgent:
    """
    Represents an "Intelligent Agent" that can perceive its environment
    and act upon it.
    
    In this case, it perceives rain and decides whether to use gear.
    """
    # BENAR: Menggunakan __init__ (double underscore)
    def __init__(self, canvas, x_pos):
        self.canvas = canvas
        self.x_start = x_pos # Posisi awal
        self.x = x_pos     # Posisi saat ini
        self.y = 300       # Base Y-position on the street
        
        # Atribut untuk gerakan
        self.speed = 1
        self.direction = 1 # 1 = ke kanan, -1 = ke kiri
        self.move_range = 30 # Seberapa jauh dia bergerak dari titik awal
        
        # The agent's "belief" or "state"
        self.is_using_gear = False
        
        # Store colors
        self.color_skin = "#F0C090"
        self.color_shirt = "#0077B6"
        self.color_raincoat = "#F8D442"
        self.color_umbrella = "#C91F37"
        self.color_cap = "#2A9D8F"

    def perceive_and_act(self, is_raining):
        """
        This is the core "intelligence" of the agent.
        It perceives the world state (is_raining) and updates its own state.
        """
        if is_raining:
            self.is_using_gear = True
        else:
            self.is_using_gear = False
            
        # This will show the agent's "decision" in the console
        print(f"Agent at {self.x_start}: Perceives rain: {is_raining}. --> Action: Use gear? {self.is_using_gear}")

    def move(self):
        """Updates the agent's x position to make it walk back and forth."""
        # Perbarui posisi x
        self.x += self.speed * self.direction
        
        # Cek batas gerak
        if self.x > self.x_start + self.move_range:
            self.direction = -1 # Balik arah ke kiri
        elif self.x < self.x_start - self.move_range:
            self.direction = 1 # Balik arah ke kanan

    def draw(self):
        """Draws the agent on the canvas based on its current state."""
        
        # --- Draw the basic body ---
        # Head
        self.canvas.create_oval(self.x - 10, self.y - 50, self.x + 10, self.y - 30, 
                                fill=self.color_skin, outline="black")
        
        # Body Color (changes if wearing raincoat)
        body_color = self.color_raincoat if self.is_using_gear else self.color_shirt
        body_width = 6 if self.is_using_gear else 4 # Raincoat is thicker
        
        # Body
        self.canvas.create_line(self.x, self.y - 30, self.x, self.y - 10, 
                                fill=body_color, width=body_width)
        # Legs
        self.canvas.create_line(self.x, self.y - 10, self.x - 8, self.y, 
                                fill="black", width=3)
        self.canvas.create_line(self.x, self.y - 10, self.x + 8, self.y, 
                                fill="black", width=3)
        # Arms
        self.canvas.create_line(self.x, self.y - 25, self.x - 10, self.y - 15, 
                                fill=body_color, width=body_width - 1)
        self.canvas.create_line(self.x, self.y - 25, self.x + 10, self.y - 15, 
                                fill=body_color, width=body_width - 1)

        # --- Draw Gear if state is 'is_using_gear' ---
        if self.is_using_gear:
            # Draw Cap
            self.canvas.create_rectangle(self.x - 10, self.y - 52, self.x + 10, self.y - 45,
                                         fill=self.color_cap, outline="")
            self.canvas.create_line(self.x + 10, self.y - 48, self.x + 15, self.y - 48,
                                      fill=self.color_cap, width=4)
            
            # Draw Umbrella
            # Handle (held in right hand)
            umbrella_x = self.x + 10
            umbrella_y = self.y - 15
            self.canvas.create_line(umbrella_x, umbrella_y, umbrella_x, umbrella_y - 35, 
                                      fill="black", width=2)
            # Canopy
            self.canvas.create_arc(umbrella_x - 30, umbrella_y - 65, umbrella_x + 30, umbrella_y - 25,
                                     start=0, extent=180, fill=self.color_umbrella, outline="")


class StreetSceneApp:
    """
    The main application class that holds the window, canvas,
    and controls the environment (the rain).
    """
    # BENAR: Menggunakan __init__ (double underscore)
    def __init__(self, root):
        self.root = root
        self.root.title("Intelligent Agent Street Scene")

        # --- Environment State ---
        self.is_raining = False

        # --- Create GUI Elements ---
        self.canvas = tk.Canvas(root, width=600, height=400, bg="#DDEEFF") # Light blue sky
        self.canvas.pack()

        # The button to control the rain
        self.rain_button = tk.Button(root, text="Make it Rain", 
                                     command=self.toggle_rain, 
                                     font=("Arial", 14), 
                                     bg="#4CAF50", fg="white", 
                                     padx=10, pady=5)
        self.rain_button.pack(pady=10)

        # --- Create Agents ---
        self.agent1 = IntelligentAgent(self.canvas, x_pos=150)
        self.agent2 = IntelligentAgent(self.canvas, x_pos=450)

        # --- Initial Perception ---
        # Beri tahu agen status awal sebelum loop dimulai
        self.agent1.perceive_and_act(self.is_raining)
        self.agent2.perceive_and_act(self.is_raining)
        
        # --- Mulai Animation Loop ---
        self.animation_loop()

    def toggle_rain(self):
        """Flips the environment state between raining and not raining."""
        self.is_raining = not self.is_raining
        
        # Update button appearance
        if self.is_raining:
            self.rain_button.config(text="Stop Rain", bg="#F44336")
            print("\n--- ENVIRONMENT: It is now RAINING ---")
        else:
            self.rain_button.config(text="Make it Rain", bg="#4CAF50")
            print("\n--- ENVIRONMENT: The rain has STOPPED ---")
            
        # --- PERCEPTION ---
        # Perintahkan agen untuk "berpikir" HANYA saat cuaca berubah
        self.agent1.perceive_and_act(self.is_raining)
        self.agent2.perceive_and_act(self.is_raining)
        
        # Kita tidak perlu memanggil draw_scene() di sini,
        # karena animation_loop() akan melakukannya secara otomatis.

    def draw_scene(self):
        """Clears and redraws the entire scene based on the current state."""
        self.canvas.delete("all")

        # Draw the "street" (a simple gray rectangle)
        self.canvas.create_rectangle(0, 310, 600, 400, fill="#666666", outline="")

        # Draw the rain if it's raining
        if self.is_raining:
            self.draw_rain()

        # Tell agents to draw themselves
        # (Mereka sudah tahu state-nya dari perceive_and_act)
        self.agent1.draw()
        self.agent2.draw()

    def animation_loop(self):
        """The main loop for movement and drawing."""
        # --- UPDATE LOGIC ---
        # Perintahkan agen untuk bergerak
        self.agent1.move()
        self.agent2.move()

        # --- DRAW ---
        # Gambar ulang seluruh scene
        self.draw_scene()
        
        # --- SCHEDULE NEXT FRAME ---
        # Panggil fungsi ini lagi setelah ~33ms (sekitar 30 FPS)
        self.root.after(33, self.animation_loop)

    def draw_rain(self):
        """Draws 100 random raindrop lines on the canvas."""
        for _ in range(100):
            x1 = random.randint(0, 600)
            y1 = random.randint(0, 310) # Only in the sky
            x2 = x1 + 2
            y2 = y1 + 10
            self.canvas.create_line(x1, y1, x2, y2, fill="#003366") # Dark blue rain

# --- Main execution ---
if __name__ == "__main__":
    main_window = tk.Tk()
    app = StreetSceneApp(main_window)
    main_window.mainloop()