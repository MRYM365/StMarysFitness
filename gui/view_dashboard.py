def view_dashboard(self):
    dashboard_window = tk.Toplevel(self.root)
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("500x300")

    heading = tk.Label(dashboard_window, text="Dashboard", font=("Arial", 14, "bold"))
    heading.pack(pady=10)

    metrics_button = tk.Button(dashboard_window, text="Generate Metrics", command=self.generate_metrics)
    metrics_button.pack(pady=5)

    trends_button = tk.Button(dashboard_window, text="Revenue Trends", command=self.view_revenue_trends)
    trends_button.pack(pady=5)


def generate_metrics(self):
    messagebox.showinfo("Generate Metrics", "Generate Metrics functionality coming soon!")


def view_revenue_trends(self):
    messagebox.showinfo("Revenue Trends", "Revenue Trends functionality coming soon!")
