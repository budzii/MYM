import tkinter as ttk

#----------------------------------------------------------------------

def on_option_change(event):
    selected = step_type.get()

    if selected == "Kill":
        goal_label['text'] = "Required Kills"
    elif selected == "Explore":
       goal_label['text'] = "Location ID"
    elif selected == "Conversation":
       goal_label['text'] = "NPC ID"

    # show label and entry
    #goal_label.grid(column=1, row=17)
    #goal_entry.grid(column=2, row=17, sticky='E')

#----------------------------------------------------------------------

mainframe = ttk.Tk()

# Step Type

step_type = ttk.StringVar() # there is the rule: variable name lowercase with _
ttk.Label(mainframe, text="Step Type").grid(column=1, row=16)
type_entry = ttk.OptionMenu(mainframe, step_type, "Kill", "Explore" , "Conversation", command=on_option_change)
type_entry.grid(column=2, row=16, sticky='E')
step_type.set("Kill")

# Step Goal

step_goal = ttk.StringVar()
goal_label = ttk.Label(mainframe, text="Required Kills")
goal_label.grid(column=1, row=17)
goal_entry = ttk.Entry(mainframe, width=20, textvariable=step_goal)
goal_entry.grid(column=2, row=17, sticky='E')

# hide label and entry
#goal_label.grid_forget()
#goal_entry.grid_forget()

# --- star the engine ---

mainframe.mainloop()


