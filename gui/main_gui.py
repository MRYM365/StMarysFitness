import tkinter as tk
from tkinter import ttk
from tkinter import ttk, messagebox
from collections import Counter


class FitnessManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("St. Mary’s Fitness Management System")
        self.root.geometry("800x600")

        # Initialize data storage
        self.members = []  # List to store members
        self.gyms = []  # List to store gyms
        self.zones = []  # List to store workout zones
        self.appointments = []  # List to store appointments
        self.attendance_records = []  # List to store attendance records

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

        self.subscription_plans = {
            "Monthly": 50,  # $50 per month
            "Quarterly": 135,  # $135 for 3 months (10% discount)
            "Annual": 480,  # $480 for 12 months (20% discount)
        }

        buttons = [
            ("Manage Members", self.show_manage_members),
            ("Manage Gyms", self.show_manage_gyms),
            ("Manage Workout Zones", self.show_manage_workout_zones),
            ("Schedule Appointments", self.show_manage_appointments),
            ("Manage Membership Fees", self.show_manage_membership_fees),
            ("Track Attendance", self.show_manage_attendance),
            ("View Dashboard", self.show_staff_dashboard),  # Add this button
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
            if age <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Age must be a positive number!")
            return

        try:
            height = float(height)
            if height <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Height must be a positive number!")
            return

        try:
            weight = float(weight)
            if weight <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Weight must be a positive number!")
            return

        # Check for duplicate members
        for member in self.members:
            if member["name"].lower() == name.lower() and member["membership_type"] == membership_type:
                messagebox.showerror("Duplicate Entry", "This member already exists!")
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
            "medical_conditions": medical_conditions if medical_conditions else "None",
            "status": "Active"
        })

        messagebox.showinfo("Success", f"Member '{name}' added successfully!")

        # Clear form fields
        self.clear_content()
        self.show_add_member_form()

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


    def show_manage_workout_zones(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Manage Workout Zones", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Add Workout Zone Button
        add_zone_button = tk.Button(self.content_frame, text="Add Workout Zone", command=self.show_add_zone_form)
        add_zone_button.pack(pady=10)

        # View Workout Zones Button
        view_zones_button = tk.Button(self.content_frame, text="View Workout Zones", command=self.view_workout_zones)
        view_zones_button.pack(pady=10)

    def show_add_zone_form(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Add Workout Zone", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Zone Name
        tk.Label(self.content_frame, text="Zone Name:").pack(anchor="w", padx=20)
        zone_name_entry = tk.Entry(self.content_frame)
        zone_name_entry.pack(fill="x", padx=20, pady=5)

        # Gym ID Dropdown
        tk.Label(self.content_frame, text="Gym ID:").pack(anchor="w", padx=20)
        gym_id_dropdown = ttk.Combobox(self.content_frame, values=[gym["id"] for gym in self.gyms])
        gym_id_dropdown.pack(fill="x", padx=20, pady=5)

        # Category Dropdown
        tk.Label(self.content_frame, text="Category:").pack(anchor="w", padx=20)
        category_dropdown = ttk.Combobox(self.content_frame,
                                         values=["Cardio", "Strength", "Yoga", "CrossFit", "General"])
        category_dropdown.pack(fill="x", padx=20, pady=5)

        # Attendant Dropdown
        tk.Label(self.content_frame, text="Attendant:").pack(anchor="w", padx=20)
        attendant_dropdown = ttk.Combobox(self.content_frame,
                                          values=["Dora", "Alice", "Ana", "Myre"])  # Example attendants
        attendant_dropdown.pack(fill="x", padx=20, pady=5)

        # Class Schedules
        tk.Label(self.content_frame, text="Class Schedules (comma-separated):").pack(anchor="w", padx=20)
        schedule_entry = tk.Entry(self.content_frame)
        schedule_entry.pack(fill="x", padx=20, pady=5)

        # Promotions
        tk.Label(self.content_frame, text="Promotions (comma-separated):").pack(anchor="w", padx=20)
        promotions_entry = tk.Entry(self.content_frame)
        promotions_entry.pack(fill="x", padx=20, pady=5)

        # Important Updates
        tk.Label(self.content_frame, text="Important Updates (comma-separated):").pack(anchor="w", padx=20)
        updates_entry = tk.Entry(self.content_frame)
        updates_entry.pack(fill="x", padx=20, pady=5)

        # Submit button
        submit_button = tk.Button(
            self.content_frame,
            text="Add Zone",
            command=lambda: self.add_zone(
                zone_name_entry.get(),
                gym_id_dropdown.get(),
                category_dropdown.get(),
                attendant_dropdown.get(),
                schedule_entry.get(),
                promotions_entry.get(),
                updates_entry.get()
            )
        )
        submit_button.pack(pady=10)

    def add_zone(self, zone_name, gym_id, category, attendant, schedule, promotions, updates):
        # Validate input
        if not zone_name or not gym_id or not category or not attendant:
            messagebox.showerror("Input Error", "Zone Name, Gym ID, Category, and Attendant are required!")
            return

        # Convert schedules, promotions, and updates to lists
        schedule_list = [s.strip() for s in schedule.split(",") if s.strip()]
        promotions_list = [p.strip() for p in promotions.split(",") if p.strip()]
        updates_list = [u.strip() for u in updates.split(",") if u.strip()]

        # Add zone to the list
        self.zones.append({
            "zone_name": zone_name,
            "gym_id": gym_id,
            "category": category,
            "attendant": attendant,
            "schedule": schedule_list,
            "promotions": promotions_list,
            "updates": updates_list,
        })

        messagebox.showinfo("Success", f"Workout Zone '{zone_name}' added successfully!")
        self.show_manage_workout_zones()

    def view_workout_zones(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Workout Zones", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Table for workout zones
        table = ttk.Treeview(
            self.content_frame,
            columns=("Zone Name", "Gym ID", "Category", "Attendant"),
            show="headings"
        )
        table.heading("Zone Name", text="Zone Name")
        table.heading("Gym ID", text="Gym ID")
        table.heading("Category", text="Category")
        table.heading("Attendant", text="Attendant")
        table.pack(fill="both", expand=True, padx=20, pady=10)

        # Insert zones into the table
        for zone in self.zones:
            table.insert("", "end", values=(zone["zone_name"], zone["gym_id"], zone["category"], zone["attendant"]))

        # Buttons for Edit, Delete, and View Details
        button_frame = tk.Frame(self.content_frame)
        button_frame.pack(pady=10)

        edit_button = tk.Button(button_frame, text="Edit Zone", command=lambda: self.edit_zone(table))
        edit_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(button_frame, text="Delete Zone", command=lambda: self.delete_zone(table))
        delete_button.pack(side=tk.LEFT, padx=5)

        view_details_button = tk.Button(button_frame, text="View Details",
                                        command=lambda: self.view_zone_details(table))
        view_details_button.pack(side=tk.LEFT, padx=5)

    def show_edit_zone_form(self, zone):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Edit Workout Zone", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Zone Name
        tk.Label(self.content_frame, text="Zone Name:").pack(anchor="w", padx=20)
        zone_name_entry = tk.Entry(self.content_frame)
        zone_name_entry.insert(0, zone["zone_name"])
        zone_name_entry.pack(fill="x", padx=20, pady=5)

        # Gym ID Dropdown
        tk.Label(self.content_frame, text="Gym ID:").pack(anchor="w", padx=20)
        gym_id_dropdown = ttk.Combobox(self.content_frame, values=[gym["id"] for gym in self.gyms])
        gym_id_dropdown.set(zone["gym_id"])  # Preselect the current Gym ID
        gym_id_dropdown.pack(fill="x", padx=20, pady=5)

        # Category Dropdown
        tk.Label(self.content_frame, text="Category:").pack(anchor="w", padx=20)
        category_dropdown = ttk.Combobox(self.content_frame,
                                         values=["Cardio", "Strength", "Yoga", "CrossFit", "General"])
        category_dropdown.set(zone["category"])  # Preselect the current category
        category_dropdown.pack(fill="x", padx=20, pady=5)

        # Attendant Dropdown
        tk.Label(self.content_frame, text="Attendant:").pack(anchor="w", padx=20)
        attendant_dropdown = ttk.Combobox(self.content_frame, values=["John", "Jane", "Mike", "Anna"])
        attendant_dropdown.set(zone["attendant"])  # Preselect the current attendant
        attendant_dropdown.pack(fill="x", padx=20, pady=5)

        # Class Schedules
        tk.Label(self.content_frame, text="Class Schedules (comma-separated):").pack(anchor="w", padx=20)
        schedule_entry = tk.Entry(self.content_frame)
        schedule_entry.insert(0, ", ".join(zone["schedule"]))
        schedule_entry.pack(fill="x", padx=20, pady=5)

        # Promotions
        tk.Label(self.content_frame, text="Promotions (comma-separated):").pack(anchor="w", padx=20)
        promotions_entry = tk.Entry(self.content_frame)
        promotions_entry.insert(0, ", ".join(zone["promotions"]))
        promotions_entry.pack(fill="x", padx=20, pady=5)

        # Important Updates
        tk.Label(self.content_frame, text="Important Updates (comma-separated):").pack(anchor="w", padx=20)
        updates_entry = tk.Entry(self.content_frame)
        updates_entry.insert(0, ", ".join(zone["updates"]))
        updates_entry.pack(fill="x", padx=20, pady=5)

        # Save button
        save_button = tk.Button(
            self.content_frame,
            text="Save Changes",
            command=lambda: self.save_zone_changes(
                zone,
                zone_name_entry.get(),
                gym_id_dropdown.get(),
                category_dropdown.get(),
                attendant_dropdown.get(),
                schedule_entry.get(),
                promotions_entry.get(),
                updates_entry.get()
            )
        )
        save_button.pack(pady=10)

    def edit_zone(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a zone to edit!")
            return

        # Get selected zone's name (first column)
        zone_name = table.item(selected_item, "values")[0]

        # Find the selected zone in self.zones
        for zone in self.zones:
            if zone["zone_name"] == zone_name:
                self.show_edit_zone_form(zone)
                return

        messagebox.showerror("Error", "Selected zone not found!")

    def delete_zone(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a zone to delete!")
            return

        # Get selected zone's name (first column)
        zone_name = table.item(selected_item, "values")[0]

        # Confirm deletion
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{zone_name}'?")
        if not confirm:
            return

        # Remove the zone from self.zones
        self.zones = [zone for zone in self.zones if zone["zone_name"] != zone_name]

        messagebox.showinfo("Success", f"Workout Zone '{zone_name}' deleted successfully!")
        self.view_workout_zones()

    def save_zone_changes(self, zone, zone_name, gym_id, category, attendant, schedule, promotions, updates):
        # Validate input
        if not zone_name or not gym_id or not category or not attendant:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        # Update the zone details
        zone["zone_name"] = zone_name
        zone["gym_id"] = gym_id
        zone["category"] = category
        zone["attendant"] = attendant
        zone["schedule"] = [s.strip() for s in schedule.split(",") if s.strip()]
        zone["promotions"] = [p.strip() for p in promotions.split(",") if p.strip()]
        zone["updates"] = [u.strip() for u in updates.split(",") if u.strip()]

        messagebox.showinfo("Success", f"Workout Zone '{zone_name}' updated successfully!")
        self.view_workout_zones()

    def view_zone_details(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a zone to view details!")
            return

        # Get selected zone's name (first column)
        zone_name = table.item(selected_item, "values")[0]

        # Find the selected zone in self.zones
        for zone in self.zones:
            if zone["zone_name"] == zone_name:
                self.show_zone_details(zone)
                return

        messagebox.showerror("Error", "Selected zone not found!")

    def show_zone_details(self, zone):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text=f"Details for Zone: {zone['zone_name']}", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Display details
        details = f"""
        Zone Name: {zone['zone_name']}
        Gym ID: {zone['gym_id']}
        Category: {zone['category']}
        Attendant: {zone['attendant']}
        Class Schedules: {', '.join(zone['schedule'])}
        Promotions: {', '.join(zone['promotions'])}
        Important Updates: {', '.join(zone['updates'])}
        """
        details_label = tk.Label(self.content_frame, text=details, justify="left", anchor="w")
        details_label.pack(pady=10, padx=20)

        # Back button
        back_button = tk.Button(self.content_frame, text="Back to Workout Zones", command=self.view_workout_zones)
        back_button.pack(pady=10)

    def show_manage_appointments(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Manage Appointments", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Add Appointment Button
        add_appointment_button = tk.Button(self.content_frame, text="Add Appointment",
                                           command=self.show_add_appointment_form)
        add_appointment_button.pack(pady=10)

        # View Appointments Button
        view_appointments_button = tk.Button(self.content_frame, text="View Appointments",
                                             command=self.view_appointments)
        view_appointments_button.pack(pady=10)

    def show_add_appointment_form(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Schedule Appointment", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Member ID Dropdown
        tk.Label(self.content_frame, text="Member ID:").pack(anchor="w", padx=20)
        member_id_dropdown = ttk.Combobox(self.content_frame, values=[member["id"] for member in self.members])
        member_id_dropdown.pack(fill="x", padx=20, pady=5)

        # Appointment Type Dropdown
        tk.Label(self.content_frame, text="Appointment Type:").pack(anchor="w", padx=20)
        appointment_type_dropdown = ttk.Combobox(self.content_frame,
                                                 values=["Personal Training", "Group Class", "Nutrition Consultation"])
        appointment_type_dropdown.pack(fill="x", padx=20, pady=5)

        # Date and Time
        tk.Label(self.content_frame, text="Date (YYYY-MM-DD):").pack(anchor="w", padx=20)
        date_entry = tk.Entry(self.content_frame)
        date_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Time (HH:MM):").pack(anchor="w", padx=20)
        time_entry = tk.Entry(self.content_frame)
        time_entry.pack(fill="x", padx=20, pady=5)

        # Trainer/Nutritionist ID (Optional)
        tk.Label(self.content_frame, text="Trainer/Nutritionist ID (Optional):").pack(anchor="w", padx=20)
        trainer_id_entry = tk.Entry(self.content_frame)
        trainer_id_entry.pack(fill="x", padx=20, pady=5)

        # Submit button
        submit_button = tk.Button(
            self.content_frame,
            text="Schedule Appointment",
            command=lambda: self.add_appointment(
                member_id_dropdown.get(),
                appointment_type_dropdown.get(),
                date_entry.get(),
                time_entry.get(),
                trainer_id_entry.get()
            )
        )
        submit_button.pack(pady=10)

    def add_appointment(self, member_id, appointment_type, date, time, trainer_id):
        # Validate input
        if not member_id or not appointment_type or not date or not time:
            messagebox.showerror("Input Error", "Member ID, Appointment Type, Date, and Time are required!")
            return

        # Generate a unique appointment ID
        appointment_id = len(self.appointments) + 1

        # Add appointment to the list
        self.appointments.append({
            "id": appointment_id,
            "member_id": member_id,
            "appointment_type": appointment_type,
            "date": date,
            "time": time,
            "trainer_id": trainer_id if trainer_id else None,
            "status": "Scheduled"
        })

        messagebox.showinfo("Success", f"Appointment scheduled successfully with ID: {appointment_id}")
        self.show_manage_appointments()

    def view_appointments(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Appointments", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Table for appointments
        table = ttk.Treeview(
            self.content_frame,
            columns=("ID", "Member ID", "Type", "Date", "Time", "Trainer ID", "Status"),
            show="headings"
        )
        table.heading("ID", text="ID")
        table.heading("Member ID", text="Member ID")
        table.heading("Type", text="Type")
        table.heading("Date", text="Date")
        table.heading("Time", text="Time")
        table.heading("Trainer ID", text="Trainer ID")
        table.heading("Status", text="Status")
        table.pack(fill="both", expand=True, padx=20, pady=10)

        # Insert appointments into the table
        for appointment in self.appointments:
            table.insert("", "end", values=(
                appointment["id"],
                appointment["member_id"],
                appointment["appointment_type"],
                appointment["date"],
                appointment["time"],
                appointment.get("trainer_id", "N/A"),
                appointment["status"]
            ))

        # Buttons for managing appointments
        button_frame = tk.Frame(self.content_frame)
        button_frame.pack(pady=10)

        edit_button = tk.Button(button_frame, text="Edit Appointment", command=lambda: self.edit_appointment(table))
        edit_button.pack(side=tk.LEFT, padx=5)

        cancel_button = tk.Button(button_frame, text="Cancel Appointment", command=lambda: self.cancel_appointment(table))
        cancel_button.pack(side=tk.LEFT, padx=5)

    def show_edit_appointment_form(self, appointment):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Edit Appointment", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Member ID (Read-only)
        tk.Label(self.content_frame, text="Member ID:").pack(anchor="w", padx=20)
        member_id_label = tk.Label(self.content_frame, text=appointment["member_id"])
        member_id_label.pack(fill="x", padx=20, pady=5)

        # Appointment Type Dropdown
        tk.Label(self.content_frame, text="Appointment Type:").pack(anchor="w", padx=20)
        appointment_type_dropdown = ttk.Combobox(self.content_frame,
                                                 values=["Personal Training", "Group Class", "Nutrition Consultation"])
        appointment_type_dropdown.set(appointment["appointment_type"])
        appointment_type_dropdown.pack(fill="x", padx=20, pady=5)

        # Date and Time
        tk.Label(self.content_frame, text="Date (YYYY-MM-DD):").pack(anchor="w", padx=20)
        date_entry = tk.Entry(self.content_frame)
        date_entry.insert(0, appointment["date"])
        date_entry.pack(fill="x", padx=20, pady=5)

        tk.Label(self.content_frame, text="Time (HH:MM):").pack(anchor="w", padx=20)
        time_entry = tk.Entry(self.content_frame)
        time_entry.insert(0, appointment["time"])
        time_entry.pack(fill="x", padx=20, pady=5)

        # Trainer/Nutritionist ID (Optional)
        tk.Label(self.content_frame, text="Trainer/Nutritionist ID (Optional):").pack(anchor="w", padx=20)
        trainer_id_entry = tk.Entry(self.content_frame)
        trainer_id_entry.insert(0, appointment["trainer_id"] if appointment["trainer_id"] else "")
        trainer_id_entry.pack(fill="x", padx=20, pady=5)

        # Save Changes Button
        save_button = tk.Button(
            self.content_frame,
            text="Save Changes",
            command=lambda: self.save_appointment_changes(
                appointment,
                appointment_type_dropdown.get(),
                date_entry.get(),
                time_entry.get(),
                trainer_id_entry.get()
            )
        )
        save_button.pack(pady=10)

    def save_appointment_changes(self, appointment, appointment_type, date, time, trainer_id):
        # Validate input
        if not appointment_type or not date or not time:
            messagebox.showerror("Input Error", "Appointment Type, Date, and Time are required!")
            return

        # Update the appointment
        appointment["appointment_type"] = appointment_type
        appointment["date"] = date
        appointment["time"] = time
        appointment["trainer_id"] = trainer_id if trainer_id else None

        messagebox.showinfo("Success", "Appointment updated successfully!")
        self.view_appointments()

    def cancel_appointment(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an appointment to cancel!")
            return

        appointment_id = table.item(selected_item, "values")[0]

        # Find the appointment and mark it as canceled
        for appointment in self.appointments:
            if str(appointment["id"]) == appointment_id:
                appointment["status"] = "Canceled"
                messagebox.showinfo("Success", f"Appointment {appointment_id} has been canceled.")
                self.view_appointments()
                return

        messagebox.showerror("Error", "Appointment not found!")

    def edit_appointment(self, table):
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an appointment to edit!")
            return

        # Get selected appointment ID
        appointment_id = table.item(selected_item, "values")[0]

        # Find the appointment
        for appointment in self.appointments:
            if str(appointment["id"]) == appointment_id:
                self.show_edit_appointment_form(appointment)
                return

        messagebox.showerror("Error", "Selected appointment not found!")

    def show_manage_membership_fees(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Manage Membership Fees", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Member ID Dropdown
        tk.Label(self.content_frame, text="Member ID:").pack(anchor="w", padx=20)
        member_id_dropdown = ttk.Combobox(self.content_frame, values=[member["id"] for member in self.members])
        member_id_dropdown.pack(fill="x", padx=20, pady=5)

        # Subscription Plan Dropdown
        tk.Label(self.content_frame, text="Subscription Plan:").pack(anchor="w", padx=20)
        plan_dropdown = ttk.Combobox(self.content_frame, values=["Monthly", "Quarterly", "Annual"])
        plan_dropdown.pack(fill="x", padx=20, pady=5)

        # Discount Entry
        tk.Label(self.content_frame, text="Discount (Percentage):").pack(anchor="w", padx=20)
        discount_entry = tk.Entry(self.content_frame)
        discount_entry.pack(fill="x", padx=20, pady=5)

        # Payment Method Dropdown
        tk.Label(self.content_frame, text="Payment Method:").pack(anchor="w", padx=20)
        payment_method_dropdown = ttk.Combobox(self.content_frame, values=["Credit Card", "PayPal", "Bank Transfer"])
        payment_method_dropdown.pack(fill="x", padx=20, pady=5)

        # Total Fee Label
        total_fee_label = tk.Label(self.content_frame, text="Total Fee: $0", font=("Arial", 12))
        total_fee_label.pack(pady=10)

        # Calculate Button
        calculate_button = tk.Button(
            self.content_frame,
            text="Calculate Total Fee",
            command=lambda: self.calculate_total_fee(
                plan_dropdown.get(),
                discount_entry.get(),
                total_fee_label
            )
        )
        calculate_button.pack(pady=5)

        # Submit Button
        submit_button = tk.Button(
            self.content_frame,
            text="Confirm Payment",
            command=lambda: self.process_payment(
                member_id_dropdown.get(),
                plan_dropdown.get(),
                discount_entry.get(),
                payment_method_dropdown.get()
            )
        )
        submit_button.pack(pady=10)

        # Add "View Memberships" Button
        view_memberships_button = tk.Button(
            self.content_frame,
            text="View Memberships",
            command=self.view_memberships
        )
        view_memberships_button.pack(pady=10)

    def calculate_total_fee(self, plan, discount, total_fee_label):
        if not plan:
            messagebox.showerror("Input Error", "Please select a subscription plan!")
            return

        base_rate = self.subscription_plans.get(plan, 0)

        try:
            discount_percentage = float(discount) if discount else 0
            if discount_percentage < 0 or discount_percentage > 100:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Discount must be a number between 0 and 100!")
            return

        # Apply discount
        discount_amount = (discount_percentage / 100) * base_rate
        total_fee = base_rate - discount_amount

        # Update total fee label
        total_fee_label.config(text=f"Total Fee: ${total_fee:.2f}")

    def process_payment(self, member_id, plan, discount, payment_method):
        # Validate input
        if not member_id or not plan or not payment_method:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        # Calculate final fee
        base_rate = self.subscription_plans.get(plan, 0)
        discount_percentage = float(discount) if discount else 0
        discount_amount = (discount_percentage / 100) * base_rate
        total_fee = base_rate - discount_amount

        # Save payment details
        payment_details = {
            "plan": plan,
            "payment_method": payment_method,
            "total_fee": total_fee,
            "discount_applied": discount_percentage,
        }

        # Update the member's subscription details
        for member in self.members:
            if str(member["id"]) == str(member_id):
                member["subscription_plan"] = plan
                member["last_payment"] = payment_details
                break

        messagebox.showinfo("Success", f"Payment of ${total_fee:.2f} processed for Member {member_id}.")
        self.show_manage_membership_fees()

    def view_memberships(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Membership Details", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Table for membership details
        table = ttk.Treeview(
            self.content_frame,
            columns=("Member ID", "Name", "Plan", "Payment Method", "Last Payment", "Discount Applied"),
            show="headings"
        )
        table.heading("Member ID", text="Member ID")
        table.heading("Name", text="Name")
        table.heading("Plan", text="Plan")
        table.heading("Payment Method", text="Payment Method")
        table.heading("Last Payment", text="Last Payment")
        table.heading("Discount Applied", text="Discount Applied")
        table.pack(fill="both", expand=True, padx=20, pady=10)

        # Insert membership details into the table
        for member in self.members:
            subscription_plan = member.get("subscription_plan", "N/A")
            last_payment = member.get("last_payment", {})
            table.insert("", "end", values=(
                member["id"],
                member["name"],
                subscription_plan,
                last_payment.get("payment_method", "N/A"),
                f"${last_payment.get('total_fee', 0):.2f}",
                f"{last_payment.get('discount_applied', 0)}%"
            ))

    def show_manage_attendance(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Track Attendance", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Member ID Dropdown
        tk.Label(self.content_frame, text="Member ID:").pack(anchor="w", padx=20)
        member_id_dropdown = ttk.Combobox(self.content_frame, values=[member["id"] for member in self.members])
        member_id_dropdown.pack(fill="x", padx=20, pady=5)

        # Date
        tk.Label(self.content_frame, text="Date (YYYY-MM-DD):").pack(anchor="w", padx=20)
        date_entry = tk.Entry(self.content_frame)
        date_entry.pack(fill="x", padx=20, pady=5)

        # Time
        tk.Label(self.content_frame, text="Time (HH:MM):").pack(anchor="w", padx=20)
        time_entry = tk.Entry(self.content_frame)
        time_entry.pack(fill="x", padx=20, pady=5)

        # Activity Dropdown
        tk.Label(self.content_frame, text="Activity:").pack(anchor="w", padx=20)
        activity_dropdown = ttk.Combobox(self.content_frame,
                                         values=["Gym Use", "Yoga Class", "HIIT Training", "Spin Class"])
        activity_dropdown.pack(fill="x", padx=20, pady=5)

        # Log Attendance Button
        log_button = tk.Button(
            self.content_frame,
            text="Log Attendance",
            command=lambda: self.log_attendance(
                member_id_dropdown.get(),
                date_entry.get(),
                time_entry.get(),
                activity_dropdown.get()
            )
        )
        log_button.pack(pady=10)

        # View Reports Button
        reports_button = tk.Button(
            self.content_frame,
            text="View Attendance Reports",
            command=self.view_attendance_reports
        )
        reports_button.pack(pady=10)

    def log_attendance(self, member_id, date, time, activity):
        # Validate input
        if not member_id or not date or not time or not activity:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        # Add attendance record
        self.attendance_records.append({
            "member_id": member_id,
            "date": date,
            "time": time,
            "activity": activity,
        })

        messagebox.showinfo("Success", f"Attendance logged for Member {member_id}.")
        self.show_manage_attendance()

    def view_attendance_reports(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Attendance Reports", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Member Attendance Report
        member_attendance = Counter([record["member_id"] for record in self.attendance_records])
        tk.Label(self.content_frame, text="Member Attendance:").pack(anchor="w", padx=20, pady=5)
        for member_id, count in member_attendance.items():
            tk.Label(self.content_frame, text=f"Member {member_id}: {count} visits").pack(anchor="w", padx=40)

        # Class Popularity Report
        class_popularity = Counter([record["activity"] for record in self.attendance_records])
        tk.Label(self.content_frame, text="\nClass Popularity:").pack(anchor="w", padx=20, pady=5)
        for activity, count in class_popularity.items():
            tk.Label(self.content_frame, text=f"{activity}: {count} participants").pack(anchor="w", padx=40)

        # Peak Usage Hours Report
        peak_hours = Counter([record["time"][:2] + ":00" for record in self.attendance_records])
        tk.Label(self.content_frame, text="\nPeak Usage Hours:").pack(anchor="w", padx=20, pady=5)
        for hour, count in peak_hours.items():
            tk.Label(self.content_frame, text=f"{hour}: {count} visits").pack(anchor="w", padx=40)

        # Back Button
        back_button = tk.Button(self.content_frame, text="Back to Attendance Management",command=self.show_manage_attendance)
        back_button.pack(pady=10)

    def show_staff_dashboard(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Staff Management Dashboard", font=("Arial", 16, "bold"))
        label.pack(pady=10)

        # Membership Growth Report Button
        membership_growth_button = tk.Button(
            self.content_frame, text="View Membership Growth", command=self.view_membership_growth
        )
        membership_growth_button.pack(pady=10)

        # Revenue Trends Button
        revenue_trends_button = tk.Button(
            self.content_frame, text="View Revenue Trends", command=self.view_revenue_trends
        )
        revenue_trends_button.pack(pady=10)

        # Trainer Schedules Button
        trainer_schedules_button = tk.Button(
            self.content_frame, text="View Trainer Schedules", command=self.view_trainer_schedules
        )
        trainer_schedules_button.pack(pady=10)

        # Equipment Maintenance Button
        equipment_maintenance_button = tk.Button(
            self.content_frame, text="View Equipment Maintenance", command=self.view_equipment_maintenance
        )
        equipment_maintenance_button.pack(pady=10)

    def view_membership_growth(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Membership Growth Report", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Simulated Data
        growth_data = {"January": 50, "February": 60, "March": 80, "April": 100}

        # Plot Growth Data
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        months = list(growth_data.keys())
        members = list(growth_data.values())

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(months, members, marker="o")
        ax.set_title("Membership Growth Over Time")
        ax.set_xlabel("Month")
        ax.set_ylabel("Number of Members")

        canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def view_revenue_trends(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Revenue Trends", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Simulated Data
        revenue_data = {"January": 5000, "February": 6000, "March": 7500, "April": 8000}

        # Plot Revenue Data
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        months = list(revenue_data.keys())
        revenue = list(revenue_data.values())

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(months, revenue, color="green")
        ax.set_title("Revenue Trends Over Time")
        ax.set_xlabel("Month")
        ax.set_ylabel("Revenue ($)")

        canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def view_trainer_schedules(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Trainer Schedules", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Simulated Trainer Schedules
        trainer_schedules = [
            {"name": "Maryam", "schedule": "Mon-Wed-Fri, 6:00 AM - 10:00 AM"},
            {"name": "Sarah", "schedule": "Tue-Thu, 4:00 PM - 8:00 PM"},
            {"name": "Meow", "schedule": "Sat-Sun, 8:00 AM - 12:00 PM"},
        ]

        for trainer in trainer_schedules:
            tk.Label(self.content_frame, text=f"Trainer: {trainer['name']}").pack(anchor="w", padx=20)
            tk.Label(self.content_frame, text=f"Schedule: {trainer['schedule']}").pack(anchor="w", padx=40, pady=5)

    def view_equipment_maintenance(self):
        self.clear_content()

        # Title
        label = tk.Label(self.content_frame, text="Equipment Maintenance", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Simulated Maintenance Logs
        maintenance_logs = [
            {"equipment": "Treadmill", "last_maintenance": "2024-01-15", "status": "Operational"},
            {"equipment": "Dumbbells", "last_maintenance": "2024-02-01", "status": "Operational"},
            {"equipment": "Elliptical", "last_maintenance": "2024-01-10", "status": "Under Maintenance"},
        ]

        for log in maintenance_logs:
            tk.Label(self.content_frame, text=f"Equipment: {log['equipment']}").pack(anchor="w", padx=20)
            tk.Label(self.content_frame, text=f"Last Maintenance: {log['last_maintenance']}").pack(anchor="w", padx=40)
            tk.Label(self.content_frame, text=f"Status: {log['status']}").pack(anchor="w", padx=40, pady=5)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessManagementApp(root)
    root.mainloop()
