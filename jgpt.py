import subprocess
import tkinter as tk

def run_tgpt(input_text):
    # Execute the tgpt command with the input text as argument
    process = subprocess.Popen(['tgpt', '-q', input_text], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode('utf-8')

def on_submit(event=None):
    # Get the input text from the input field
    input_text = input_entry.get()
    # Add the new question to the output_textbox
    output_textbox.config(state=tk.NORMAL)
    output_textbox.insert(tk.END, f"\n\nQuestion: {input_text}\n\n")
    # Run tgpt with the input text and display the output in the text box
    output_text = run_tgpt(input_text)
    output_textbox.insert(tk.END, output_text)
    output_textbox.config(state=tk.DISABLED)
    # Clear the input field
    input_entry.delete(0, tk.END)

# Create a TKinter window
root = tk.Tk()
root.title("JGPT v0.1")

# Set the window icon
root.iconbitmap("jw.ico")

# Add an input field
input_label = tk.Label(root, text="Enter text:")
input_label.pack()
input_entry = tk.Entry(root, width=150)
input_entry.pack()

# Add a button to execute the command
submit_button = tk.Button(root, text="Generate Answer", command=on_submit)
submit_button.pack()

# Add a text box to display the output
output_textbox = tk.Text(root, height=50, width=150, state=tk.DISABLED, wrap=tk.WORD)
output_textbox.pack()

# Add an event handler for CTRL + ENTER
root.bind("<Control-Return>", on_submit)

# Start the TKinter event loop
root.mainloop()
