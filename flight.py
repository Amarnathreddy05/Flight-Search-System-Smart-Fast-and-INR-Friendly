import tkinter as tk
from tkinter import messagebox

USD_TO_INR = 80  # Example conversion rate: 1 USD = 80 INR

class Flight:
    def __init__(self, flight_name, departure_date, departure_time, price_in_usd):
        self.flight_name = flight_name
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.price_in_usd = price_in_usd
        self.price_in_inr = price_in_usd * USD_TO_INR  # Convert price to INR

    def __repr__(self):
        return f"{self.flight_name}: {self.departure_date} {self.departure_time} for ₹{self.price_in_inr}"

def merge_sort(flights, key_func):
    if len(flights) > 1:
        mid = len(flights) // 2
        left_half = flights[:mid]
        right_half = flights[mid:]

        merge_sort(left_half, key_func)
        merge_sort(right_half, key_func)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if key_func(left_half[i]) < key_func(right_half[j]):
                flights[k] = left_half[i]
                i += 1
            else:
                flights[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            flights[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            flights[k] = right_half[j]
            j += 1
            k += 1

def binary_search(flights, low, high, key_func):
    start = -1
    end = -1
    low_index, high_index = 0, len(flights) - 1
    while low_index <= high_index:
        mid = (low_index + high_index) // 2
        if key_func(flights[mid]) < low:
            low_index = mid + 1
        else:
            start = mid
            high_index = mid - 1
    low_index, high_index = 0, len(flights) - 1
    while low_index <= high_index:
        mid = (low_index + high_index) // 2
        if key_func(flights[mid]) > high:
            high_index = mid - 1
        else:
            end = mid
            low_index = mid + 1
    if start == -1 or end == -1:
        return []
    else:
        return flights[start:end + 1]

def flight_price(flight):
    return flight.price_in_inr

def add_flight(flight_list, flight_name, departure_date, departure_time, price_in_usd):
    flight = Flight(flight_name, departure_date, departure_time, price_in_usd)
    flight_list.append(flight)
    return f"Flight {flight_name} has been added successfully!"

def sort_flights(flight_list):
    merge_sort(flight_list, key_func=flight_price)
    return flight_list

def search_flights_by_price(flight_list, min_price, max_price):
    merge_sort(flight_list, key_func=flight_price)
    result_flights = binary_search(flight_list, min_price, max_price, key_func=flight_price)
    return result_flights

def show_flights(flights):
    flights_str = ""
    for flight in flights:
        flights_str += str(flight) + "\n"
    return flights_str

class FlightApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Search System")

        self.flight_list = []

        # Add Flight Section
        self.add_flight_label = tk.Label(root, text="Add Flight")
        self.add_flight_label.grid(row=0, column=0, columnspan=2)

        self.flight_name_label = tk.Label(root, text="Flight Name")
        self.flight_name_label.grid(row=1, column=0)
        self.flight_name_entry = tk.Entry(root)
        self.flight_name_entry.grid(row=1, column=1)

        self.departure_date_label = tk.Label(root, text="Departure Date (YYYY-MM-DD)")
        self.departure_date_label.grid(row=2, column=0)
        self.departure_date_entry = tk.Entry(root)
        self.departure_date_entry.grid(row=2, column=1)

        self.departure_time_label = tk.Label(root, text="Departure Time (HH:MM)")
        self.departure_time_label.grid(row=3, column=0)
        self.departure_time_entry = tk.Entry(root)
        self.departure_time_entry.grid(row=3, column=1)

        self.price_in_usd_label = tk.Label(root, text="Price in USD")
        self.price_in_usd_label.grid(row=4, column=0)
        self.price_in_usd_entry = tk.Entry(root)
        self.price_in_usd_entry.grid(row=4, column=1)

        self.add_flight_button = tk.Button(root, text="Add Flight", command=self.add_flight)
        self.add_flight_button.grid(row=5, column=0, columnspan=2)

        # Sort Flights Section
        self.sort_button = tk.Button(root, text="Sort Flights by Price", command=self.sort_flights)
        self.sort_button.grid(row=6, column=0, columnspan=2)

        # Search Flights Section
        self.search_label = tk.Label(root, text="Search Flights by Price Range")
        self.search_label.grid(row=7, column=0, columnspan=2)

        self.min_price_label = tk.Label(root, text="Min Price (₹)")
        self.min_price_label.grid(row=8, column=0)
        self.min_price_entry = tk.Entry(root)
        self.min_price_entry.grid(row=8, column=1)

        self.max_price_label = tk.Label(root, text="Max Price (₹)")
        self.max_price_label.grid(row=9, column=0)
        self.max_price_entry = tk.Entry(root)
        self.max_price_entry.grid(row=9, column=1)

        self.search_button = tk.Button(root, text="Search Flights", command=self.search_flights)
        self.search_button.grid(row=10, column=0, columnspan=2)

        # Display Flights Section
        self.flight_display_label = tk.Label(root, text="Flights Display")
        self.flight_display_label.grid(row=11, column=0, columnspan=2)

        self.flight_display_text = tk.Text(root, height=10, width=50)
        self.flight_display_text.grid(row=12, column=0, columnspan=2)

    def add_flight(self):
        flight_name = self.flight_name_entry.get()
        departure_date = self.departure_date_entry.get()
        departure_time = self.departure_time_entry.get()
        price_in_usd = float(self.price_in_usd_entry.get())

        result = add_flight(self.flight_list, flight_name, departure_date, departure_time, price_in_usd)
        messagebox.showinfo("Success", result)

    def sort_flights(self):
        sorted_flights = sort_flights(self.flight_list)
        self.flight_display_text.delete(1.0, tk.END)
        self.flight_display_text.insert(tk.END, show_flights(sorted_flights))

    def search_flights(self):
        min_price = float(self.min_price_entry.get())
        max_price = float(self.max_price_entry.get())

        result_flights = search_flights_by_price(self.flight_list, min_price, max_price)
        if result_flights:
            self.flight_display_text.delete(1.0, tk.END)
            self.flight_display_text.insert(tk.END, show_flights(result_flights))
        else:
            messagebox.showinfo("No Results", f"No flights found in the price range ₹{min_price} to ₹{max_price}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightApp(root)
    root.mainloop()