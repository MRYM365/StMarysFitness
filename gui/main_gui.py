import tkinter as tk
from tkinter import ttk, messagebox


class FitnessManagementApp:
    def __init__(self, root):
        self.gyms = []  # List to store gym locations
        self.members = []  # In-memory storage for members
        self.root = root
        self.root.title("St. Mary’s Fitness Management System")
        self.root.geometry("800x600")

        # Header
        header = tk.Label(self.root, text="St. Mary’s Fitness Management System", font=("Arial", 16, "bold"), bg="blue", fg="white")
        header.pack(fill=tk.X)

        # Main layout: Left navigation and right content area
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Navigation Bar (Left)
        nav_frame = tk.Frame(self.main_frame, width=200, bg="lightgray")
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Content Area (Right)
        self.content_frame = tk.Frame(self.main_frame, bg="white")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Add "Manage Gyms" button to the navigation bar
        buttons = [
            ("Manage Members", self.show_manage_members),
            ("Manage Gyms", self.show_manage_gyms),  # New button for gym management
            ("View Workout Zones", self.show_view_zones),
            ("Schedule Appointments", self.show_schedule_appointments),
            ("View Dashboard", self.show_dashboard),
        ]

        for text, command in buttons:
            button = tk.Button(nav_frame, text=text, font=("Arial", 12), command=command, bg="lightblue", relief=tk.FLAT)
            button.pack(fill=tk.X, pady=5, padx=5)

        # Show default view
        self.show_manage_members()

    # Utility method to clear content area
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # Manage Members Section
    def show_manage_members(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Manage Members", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Add Member Button
        add_member_button = tk.Button(self.content_frame, text="Add Member", command=self.show_add_member_form)
        add_member_button.pack(pady=10)

        # View Members Button
        view_members_button = tk.Button(self.content_frame, text="View All Members", command=self.view_members)
        view_members_button.pack(pady=10)

    def show_add_member_form(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Add Member", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Form fields
        tk.Label(self.content_frame, text="Name:").pack(anchor="w", padx=20)
        name_entry = tk.Entry(self.content_frame)
        name_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Membership Type (Regular/Premium/Trial):").pack(anchor="w", padx=20)
        membership_type_entry = tk.Entry(self.content_frame)
        membership_type_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Age:").pack(anchor="w", padx=20)
        age_entry = tk.Entry(self.content_frame)
        age_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Height (cm):").pack(anchor="w", padx=20)
        height_entry = tk.Entry(self.content_frame)
        height_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Weight (kg):").pack(anchor="w", padx=20)
        weight_entry = tk.Entry(self.content_frame)
        weight_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Medical Conditions (Optional):").pack(anchor="w", padx=20)
        medical_conditions_entry = tk.Entry(self.content_frame)
        medical_conditions_entry.pack(fill="x", padx=20, pady=5)

        # Submit button
        submit_button = tk.Button(
            self.content_frame,
            text="Add Member",
            command=lambda: self.add_member(
                name_entry.get(),
                membership_type_entry.get(),
                age_entry.get(),
                height_entry.get(),
                weight_entry.get(),
                medical_conditions_entry.get()
            )
        )
        submit_button.pack(pady=10)

    def add_member(self, name, membership_type, age, height, weight, medical_conditions):
        # Validate input
        if not name or not membership_type or not age or not height or not weight:
            messagebox.showerror("Input Error", "All fields except Medical Conditions are required!")
            return

        if membership_type not in ["Regular", "Premium", "Trial"]:
            messagebox.showerror("Input Error", "Invalid membership type!")
            return

        try:
            age = int(age)
            height = float(height)
            weight = float(weight)
            if age <= 0 or height <= 0 or weight <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Age, height, and weight must be positive numbers!")
            return

        # Add member to the backend
        member_id = len(self.members) + 1  # Simulate unique ID generation
        self.members.append({
            "id": member_id,
            "name": name,
            "membership_type": membership_type,
            "age": age,
            "height": height,
            "weight": weight,
            "medical_conditions": medical_conditions,
            "status": "Active",  # Default status
        })

        messagebox.showinfo("Success", f"Member '{name}' added successfully!")

    def view_members(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="All Members", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Table for members
        table = ttk.Treeview(
            self.content_frame,
            columns=("ID", "Name", "Membership", "Age", "Status"),
            show="headings"
        )
        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("Membership", text="Membership")
        table.heading("Age", text="Age")
        table.heading("Status", text="Status")
        table.pack(fill="both", expand=True, padx=20, pady=10)

        # Insert members into the table
        for member in self.members:
            table.insert("", "end", values=(
                member["id"],
                member["name"],
                member["membership_type"],
                member["age"],
                member["status"]
            ))
            # Buttons for Edit, Delete, and View Profile
            button_frame = tk.Frame(self.content_frame)
            button_frame.pack(pady=10)

            edit_button = tk.Button(button_frame, text="Edit Member", command=lambda: self.edit_member(table))
            edit_button.pack(side=tk.LEFT, padx=5)

            delete_button = tk.Button(button_frame, text="Delete Member", command=lambda: self.delete_member(table))
            delete_button.pack(side=tk.LEFT, padx=5)

            view_profile_button = tk.Button(button_frame, text="View Profile", command=lambda: self.view_profile(table))
            view_profile_button.pack(side=tk.LEFT, padx=5)

    def delete_member(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a member to delete!")
            return

        member_id = table.item(selected_item, "values")[0]

        # Confirm deletion
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this member?")
        if not confirm:
            return

        # Remove member from the list
        self.members = [m for m in self.members if str(m["id"]) != member_id]

        messagebox.showinfo("Success", "Member deleted successfully!")
        self.view_members()


    def view_profile(self, table):
            selected_item = table.selection()
            if not selected_item:
                messagebox.showerror("Error", "Please select a member to view their profile!")
                return

            member_id = table.item(selected_item, "values")[0]

            # Find member by ID
            for member in self.members:
                if str(member["id"]) == member_id:
                    self.show_member_profile(member)
                    break

    def show_member_profile(self, member):
            self.clear_content()

            # Title
            label = tk.Label(self.content_frame, text=f"Profile: {member['name']}", font=("Arial", 14, "bold"))
            label.pack(pady=10)

            for key, value in member.items():
                tk.Label(self.content_frame, text=f"{key.capitalize()}: {value}").pack(anchor="w", padx=20, pady=5)

    def edit_member(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a member to edit!")
            return

        member_id = table.item(selected_item, "values")[0]

        # Find member by ID
        for member in self.members:
            if str(member["id"]) == member_id:
                self.show_edit_member_form(member)
                break

    def show_edit_member_form(self, member):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Edit Member", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Form fields
        tk.Label(self.content_frame, text="Name:").pack(anchor="w", padx=20)
        name_entry = tk.Entry(self.content_frame)
        name_entry.insert(0, member["name"])  # Pre-fill current name
        name_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Membership Type (Regular/Premium/Trial):").pack(anchor="w", padx=20)
        membership_type_entry = tk.Entry(self.content_frame)
        membership_type_entry.insert(0, member["membership_type"])  # Pre-fill current membership type
        membership_type_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Age:").pack(anchor="w", padx=20)
        age_entry = tk.Entry(self.content_frame)
        age_entry.insert(0, str(member["age"]))  # Pre-fill current age
        age_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Height (cm):").pack(anchor="w", padx=20)
        height_entry = tk.Entry(self.content_frame)
        height_entry.insert(0, str(member.get("height", "")))  # Pre-fill current height or leave blank
        height_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Weight (kg):").pack(anchor="w", padx=20)
        weight_entry = tk.Entry(self.content_frame)
        weight_entry.insert(0, str(member.get("weight", "")))  # Pre-fill current weight or leave blank
        weight_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Medical Conditions:").pack(anchor="w", padx=20)
        medical_conditions_entry = tk.Entry(self.content_frame)
        medical_conditions_entry.insert(0, member.get("medical_conditions", ""))  # Pre-fill or leave blank
        medical_conditions_entry.pack(fill="x", padx=20, pady=5)

        # Save button
        save_button = tk.Button(
            self.content_frame,
            text="Save Changes",
            command=lambda: self.save_member_changes(
                member,
                name_entry.get(),
                membership_type_entry.get(),
                age_entry.get(),
                height_entry.get(),
                weight_entry.get(),
                medical_conditions_entry.get()
            )
        )
        save_button.pack(pady=10)

    def delete_member(self, table):
            selected_item = table.selection()
            if not selected_item:
                messagebox.showerror("Error", "Please select a member to delete!")
                return

            member_id = table.item(selected_item, "values")[0]

            # Confirm deletion
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this member?")
            if not confirm:
                return

            # Remove member from list
            self.members = [m for m in self.members if str(m["id"]) != member_id]

            messagebox.showinfo("Success", "Member deleted successfully!")
            self.view_members()

    def save_member_changes(self, member, name, membership_type, age, height, weight, medical_conditions):
        # Validate input
        if not name or not membership_type or not age or not height or not weight:
            messagebox.showerror("Input Error", "All fields except Medical Conditions are required!")
            return

        if membership_type not in ["Regular", "Premium", "Trial"]:
            messagebox.showerror("Input Error", "Invalid membership type!")
            return

        try:
            age = int(age)
            height = float(height)
            weight = float(weight)
            if age <= 0 or height <= 0 or weight <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Age, height, and weight must be positive numbers!")
            return

        # Update member details
        member["name"] = name
        member["membership_type"] = membership_type
        member["age"] = age
        member["height"] = height
        member["weight"] = weight
        member["medical_conditions"] = medical_conditions

        messagebox.showinfo("Success", f"Member '{name}' updated successfully!")
        self.view_members()

    def show_manage_gyms(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Manage Gym Locations", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Add Gym Button
        add_gym_button = tk.Button(self.content_frame, text="Add Gym", command=self.show_add_gym_form)
        add_gym_button.pack(pady=10)

        # View Gyms Button
        view_gyms_button = tk.Button(self.content_frame, text="View Gyms", command=self.view_gyms)
        view_gyms_button.pack(pady=10)

    def show_add_gym_form(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Add Gym Location", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Form fields
        tk.Label(self.content_frame, text="Gym ID:").pack(anchor="w", padx=20)
        gym_id_entry = tk.Entry(self.content_frame)
        gym_id_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Gym Name:").pack(anchor="w", padx=20)
        gym_name_entry = tk.Entry(self.content_frame)
        gym_name_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="City:").pack(anchor="w", padx=20)
        city_entry = tk.Entry(self.content_frame)
        city_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Manager:").pack(anchor="w", padx=20)
        manager_entry = tk.Entry(self.content_frame)
        manager_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Workout Zones (comma-separated):").pack(anchor="w", padx=20)
        zones_entry = tk.Entry(self.content_frame)
        zones_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Equipment (comma-separated):").pack(anchor="w", padx=20)
        equipment_entry = tk.Entry(self.content_frame)
        equipment_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Amenities (comma-separated):").pack(anchor="w", padx=20)
        amenities_entry = tk.Entry(self.content_frame)
        amenities_entry.pack(fill="x", padx=20, pady=5)

        # Submit button
        submit_button = tk.Button(
            self.content_frame,
            text="Add Gym",
            command=lambda: self.add_gym(
                gym_id_entry.get(),
                gym_name_entry.get(),
                city_entry.get(),
                manager_entry.get(),
                zones_entry.get(),
                equipment_entry.get(),
                amenities_entry.get()
            )
        )
        submit_button.pack(pady=10)

    def add_gym(self, gym_id, name, city, manager, zones, equipment, amenities):
        # Validate input
        if not gym_id or not name or not city or not manager:
            messagebox.showerror("Input Error", "Gym ID, Name, City, and Manager are required!")
            return

        # Convert zones, equipment, and amenities to lists
        zones_list = [z.strip() for z in zones.split(",") if z.strip()]
        equipment_list = [e.strip() for e in equipment.split(",") if e.strip()]
        amenities_list = [a.strip() for a in amenities.split(",") if a.strip()]

        # Add gym to the list
        self.gyms.append({
            "id": gym_id,
            "name": name,
            "city": city,
            "manager": manager,
            "zones": zones_list,
            "equipment": equipment_list,
            "amenities": amenities_list,
        })

        messagebox.showinfo("Success", f"Gym '{name}' added successfully!")
        self.show_manage_gyms()

    def view_gyms(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Gym Locations", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Table for gyms
        table = ttk.Treeview(
            self.content_frame,
            columns=("ID", "Name", "City", "Manager"),
            show="headings"
        )
        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("City", text="City")
        table.heading("Manager", text="Manager")
        table.pack(fill="both", expand=True, padx=20, pady=10)

        # Insert gyms into the table
        for gym in self.gyms:
            table.insert("", "end", values=(gym["id"], gym["name"], gym["city"], gym["manager"]))

            # Buttons for Edit, Delete, and View Details
        button_frame = tk.Frame(self.content_frame)
        button_frame.pack(pady=10)

        edit_button = tk.Button(button_frame, text="Edit Gym", command=lambda: self.edit_gym(table))
        edit_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(button_frame, text="Delete Gym", command=lambda: self.delete_gym(table))
        delete_button.pack(side=tk.LEFT, padx=5)

        view_details_button = tk.Button(button_frame, text="View Details", command=lambda: self.view_gym_details(table))
        view_details_button.pack(side=tk.LEFT, padx=5)

    def edit_gym(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a gym to edit!")
            return

        gym_id = table.item(selected_item, "values")[0]

        # Find gym by ID
        for gym in self.gyms:
            if gym["id"] == gym_id:
                self.show_edit_gym_form(gym)
                break

    def show_edit_gym_form(self, gym):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Edit Gym Location", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Form fields
        tk.Label(self.content_frame, text="Gym ID:").pack(anchor="w", padx=20)
        gym_id_entry = tk.Entry(self.content_frame)
        gym_id_entry.insert(0, gym["id"])  # Pre-fill current ID
        gym_id_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Gym Name:").pack(anchor="w", padx=20)
        gym_name_entry = tk.Entry(self.content_frame)
        gym_name_entry.insert(0, gym["name"])  # Pre-fill current name
        gym_name_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="City:").pack(anchor="w", padx=20)
        city_entry = tk.Entry(self.content_frame)
        city_entry.insert(0, gym["city"])  # Pre-fill current city
        city_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Manager:").pack(anchor="w", padx=20)
        manager_entry = tk.Entry(self.content_frame)
        manager_entry.insert(0, gym["manager"])  # Pre-fill current manager
        manager_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Workout Zones (comma-separated):").pack(anchor="w", padx=20)
        zones_entry = tk.Entry(self.content_frame)
        zones_entry.insert(0, ", ".join(gym["zones"]))  # Pre-fill current zones
        zones_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Equipment (comma-separated):").pack(anchor="w", padx=20)
        equipment_entry = tk.Entry(self.content_frame)
        equipment_entry.insert(0, ", ".join(gym["equipment"]))  # Pre-fill current equipment
        equipment_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Amenities (comma-separated):").pack(anchor="w", padx=20)
        amenities_entry = tk.Entry(self.content_frame)
        amenities_entry.insert(0, ", ".join(gym["amenities"]))  # Pre-fill current amenities
        amenities_entry.pack(fill="x", padx=20, pady=5)

        # Save button
        save_button = tk.Button(
            self.content_frame,
            text="Save Changes",
            command=lambda: self.save_gym_changes(
                gym,
                gym_id_entry.get(),
                gym_name_entry.get(),
                city_entry.get(),
                manager_entry.get(),
                zones_entry.get(),
                equipment_entry.get(),
                amenities_entry.get()
            )
        )
        save_button.pack(pady=10)

    def save_gym_changes(self, gym, gym_id, name, city, manager, zones, equipment, amenities):
        # Validate input
        if not gym_id or not name or not city or not manager:
            messagebox.showerror("Input Error", "Gym ID, Name, City, and Manager are required!")
            return

        # Update gym details
        gym["id"] = gym_id
        gym["name"] = name
        gym["city"] = city
        gym["manager"] = manager
        gym["zones"] = [z.strip() for z in zones.split(",") if z.strip()]
        gym["equipment"] = [e.strip() for e in equipment.split(",") if e.strip()]
        gym["amenities"] = [a.strip() for a in amenities.split(",") if a.strip()]

        messagebox.showinfo("Success", f"Gym '{name}' updated successfully!")
        self.view_gyms()

    def delete_gym(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a gym to delete!")
            return

        gym_id = table.item(selected_item, "values")[0]

        # Confirm deletion
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this gym?")
        if not confirm:
            return

        # Remove gym from list
        self.gyms = [g for g in self.gyms if g["id"] != gym_id]

        messagebox.showinfo("Success", "Gym deleted successfully!")
        self.view_gyms()

    def view_gym_details(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a gym to view details!")
            return

        gym_id = table.item(selected_item, "values")[0]

        # Find gym by ID
        for gym in self.gyms:
            if gym["id"] == gym_id:
                self.show_gym_details(gym)
                break

    def show_gym_details(self, gym):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text=f"Gym Details: {gym['name']}", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Display details
        details = f"""
        Gym ID: {gym['id']}
        Name: {gym['name']}
        City: {gym['city']}
        Manager: {gym['manager']}
        Zones: {', '.join(gym['zones'])}
        Equipment: {', '.join(gym['equipment'])}
        Amenities: {', '.join(gym['amenities'])}
        """
        details_label = tk.Label(self.content_frame, text=details, justify="left", anchor="w")
        details_label.pack(pady=10, padx=20)

    # Placeholder for other sections
    def show_view_zones(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="View Workout Zones", font=("Arial", 14, "bold"))
        label.pack(pady=20)

    def show_schedule_appointments(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="Schedule Appointments", font=("Arial", 14, "bold"))
        label.pack(pady=20)

    def show_dashboard(self):
        self.clear_content()
        label = tk.Label(self.content_frame, text="View Dashboard", font=("Arial", 14, "bold"))
        label.pack(pady=20)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessManagementApp(root)
    root.mainloop()
