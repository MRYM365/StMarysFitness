def manage_members(self):
    manage_window = tk.Toplevel(self.root)
    manage_window.title("Manage Members")
    manage_window.geometry("500x300")

    heading = tk.Label(manage_window, text="Manage Members", font=("Arial", 14, "bold"))
    heading.pack(pady=10)

    # Add member button
    add_member_button = tk.Button(manage_window, text="Add Member", command=self.add_member)
    add_member_button.pack(pady=5)

    # View all members button
    view_members_button = tk.Button(manage_window, text="View All Members", command=self.view_members)
    view_members_button.pack(pady=5)


def add_member(self):
    messagebox.showinfo("Add Member", "Add Member functionality coming soon!")


def view_members(self):
    messagebox.showinfo("View Members", "View Members functionality coming soon!")
