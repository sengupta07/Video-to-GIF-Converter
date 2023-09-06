import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

clip = None
selected_file_path = ""


def select_file():
    global selected_file_path
    selected_file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    if selected_file_path:
        result_label.config(text="Video selected: " + selected_file_path)


def convert_to_gif():
    global clip
    if not selected_file_path:
        result_label.config(text="Please select a video first.")
        return

    fps_input = fps_entry.get()
    if not fps_input:
        result_label.config(text="Please enter a valid FPS value.")
        return

    try:
        fps = int(fps_input)
    except ValueError:
        result_label.config(text="Invalid FPS value. Please enter a valid integer.")
        return

    clip = VideoFileClip(selected_file_path)
    result_label.config(text="Video loaded.")


def save_gif():
    global clip
    if not clip:
        result_label.config(text="Please load a video first.")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")])
    if not output_file:
        return

    fps_input = fps_entry.get()
    try:
        fps = int(fps_input)
    except ValueError:
        result_label.config(text="Invalid FPS value. Please enter a valid integer.")
        return
    clip = VideoFileClip(selected_file_path).subclip(
        t_start=1,  # time in seconds
        t_end=10
    ).resize(.40)

    clip.write_gif(output_file, fps=fps)
    result_label.config(text="GIF saved successfully!")


root = tk.Tk()
root.title("Video to GIF Converter")


title_image = tk.PhotoImage(file="ihuhand.png")
resized_title_image = title_image.subsample(2, 2)
title_label = tk.Label(root, image=resized_title_image)
title_label.pack()
file_button = tk.Button(root, text="Select Video File", command=select_file)
file_button.pack(pady=10)

fps_label = tk.Label(root, text="Frames Per Second:")
fps_label.pack()
fps_entry = tk.Entry(root)
fps_entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert to GIF", command=convert_to_gif)
convert_button.pack(pady=10)

save_button = tk.Button(root, text="Save GIF", command=save_gif)
save_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

credits_label = tk.Label(root, text="Created by Suman Sengupta")
credits_label.pack(pady=10)


root.mainloop()
