import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os
import shutil

ctk.set_appearance_mode("dark")


app = ctk.CTk()
app.title("Game Profile Selector")
app.geometry("500x520")
app.iconbitmap("E:/Python/Game Profile Selector/hitman.ico")

def start_game(user_name):
    log_file_path = "C:\\ProgramData\\Steam\\last_user.log"
    
    if os.path.exists(log_file_path) and os.path.getsize(log_file_path) > 0:
        with open(log_file_path, "r") as file:
            last_user = file.read().strip()  
    else:
        last_user = ""  

    
    if last_user == user_name:
        loading_label.configure(text=f"Launching game for {user_name}...")
        os.startfile("F:/Games/Hitman Absolution Professional Edition/HMA.exe")
    else:
        loading_label.configure(text=f"Switching profiles... Moving files...")
        
        current_save_file = "C:\\ProgramData\\Steam\\RLD!\\203140\\storage\\HM5"  
        if user_name == "JP":
            
            shutil.move(current_save_file, "C:\\ProgramData\\Steam\\GS\\HM5")
            
            shutil.move("C:\\ProgramData\\Steam\\JP\\HM5", "C:\\ProgramData\\Steam\\RLD!\\203140\\storage\\HM5")
        else:  
            
            shutil.move(current_save_file, "C:\\ProgramData\\Steam\\JP\\HM5")
            
            shutil.move("C:\\ProgramData\\Steam\\GS\\HM5", "C:\\ProgramData\\Steam\\RLD!\\203140\\storage\\HM5")
        

    loading_label.configure(text=f"Files are loaded for {user_name}...")
    progress_bar.start()  
    app.after(1015, lambda: show_success(user_name))  
    
    
    with open(log_file_path, "w") as file:
        file.write(user_name)

def show_success(user_name):
    progress_bar.stop()
    loading_label.configure(text=f"Enjoy your game, {user_name}!")
    os.startfile("F:/Games/Hitman Absolution Professional Edition/HMA.exe")  


def confirm_exit():
    if messagebox.askokcancel("Quit", "Do you really want to exit?"):
        app.quit()


game_image_pil = Image.open("E:/Python/Game Profile Selector/Hitman.jpg")  
profile_1_image_pil = Image.open("E:/Python/Game Profile Selector/Jp.png")  
profile_2_image_pil = Image.open("E:/Python/Game Profile Selector/Gs.png")  


game_image_pil = game_image_pil.resize((200, 400))  
profile_1_image_pil = profile_1_image_pil.resize((200, 200))  
profile_2_image_pil = profile_2_image_pil.resize((200, 200))


game_image_ctk = ctk.CTkImage(light_image=game_image_pil, size=(300, 400))
profile_1_image_ctk = ctk.CTkImage(light_image=profile_1_image_pil, size=(100, 100))
profile_2_image_ctk = ctk.CTkImage(light_image=profile_2_image_pil, size=(100, 100))


game_image_frame = ctk.CTkFrame(app, width=200, height=400)
game_image_frame.grid(row=0, column=0, rowspan=2, sticky="nsw", padx=10, pady=10)

game_image_label = ctk.CTkLabel(game_image_frame, image=game_image_ctk, text="")
game_image_label.pack(expand=True)


profile_1_frame = ctk.CTkFrame(app, width=200, height=150)
profile_1_frame.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="nsew")

profile_1_image_label = ctk.CTkLabel(profile_1_frame, image=profile_1_image_ctk, text="")
profile_1_image_label.pack(pady=5)

profile_1_name = ctk.CTkLabel(profile_1_frame, text="JP's Profile")
profile_1_name.pack(pady=5)

start_button_1 = ctk.CTkButton(profile_1_frame, text="Start JP's Game", command=lambda: start_game("JP"), fg_color="red", hover_color="dark red")
start_button_1.pack(pady=5)


profile_2_frame = ctk.CTkFrame(app, width=200, height=150)
profile_2_frame.grid(row=1, column=1, padx=10, pady=(5, 10), sticky="nsew")

profile_2_image_label = ctk.CTkLabel(profile_2_frame, image=profile_2_image_ctk, text="")
profile_2_image_label.pack(pady=5)

profile_2_name = ctk.CTkLabel(profile_2_frame, text="GS's Profile")
profile_2_name.pack(pady=5)

start_button_2 = ctk.CTkButton(profile_2_frame, text="Start GS's Game", command=lambda: start_game("GS"), fg_color="red", hover_color="dark red")
start_button_2.pack(pady=5)


exit_button = ctk.CTkButton(app, text="Exit", command=confirm_exit, fg_color="red", hover_color="dark red")

exit_button.grid(row=2, column=0, pady=10, padx=10, sticky="w")

loading_label = ctk.CTkLabel(app, text="Status")
loading_label.grid(row=2, column=0, columnspan=2, pady=5)

progress_bar = ctk.CTkProgressBar(app, mode="determinate", progress_color="green")
progress_bar.set(0)  
progress_bar.grid(row=3, column=0, columnspan=2, pady=5)

Dev_label = ctk.CTkLabel(app, text="Made With❤️")
Dev_label.grid(row=4, column=0, columnspan=2, pady=5)

app.mainloop()
