class AppointmentScheduler:
    def __init__(self):
        self.appointments = {}  # Dictionary to store appointments (date: list of appointments)

    def schedule_appointment(self, date, patient_name, start_time):
        """
        Schedule an appointment for the given date and start time.
        Args:
            date (str): Date in the format 'YYYY-MM-DD'.
            patient_name (str): Name of the patient.
            start_time (str): Start time in the format 'HH:MM' (24-hour clock).
        """
        if date not in self.appointments:
            self.appointments[date] = []
        self.appointments[date].append((patient_name, start_time))
        print(f"Appointment scheduled for {patient_name} on {date} at {start_time}")

    def get_appointments(self, date):
        """
        Get the list of appointments for the given date.
        Args:
            date (str): Date in the format 'YYYY-MM-DD'.
        Returns:
            list: List of tuples (patient name, start time).
        """
        return self.appointments.get(date, [])

    def cancel_appointment(self, date, patient_name):
        """
        Cancel an existing appointment.
        Args:
            date (str): Date in the format 'YYYY-MM-DD'.
            patient_name (str): Name of the patient.
        """
        if date in self.appointments:
            self.appointments[date] = [(p, t) for p, t in self.appointments[date] if p != patient_name]
            print(f"Appointment canceled for {patient_name} on {date}")
        else:
            print(f"No appointment found for {patient_name} on {date}")

if __name__ == "__main__":
    scheduler = AppointmentScheduler()

    while True:
        print("\nAppointment Scheduler Menu:")
        print("1. Schedule an appointment")
        print("2. View appointments for a date")
        print("3. Cancel an appointment")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            date = input("Enter appointment date (YYYY-MM-DD): ")
            patient_name = input("Enter patient name: ")
            start_time = input("Enter start time (HH:MM, 24-hour format): ")
            scheduler.schedule_appointment(date, patient_name, start_time)
        elif choice == "2":
            date = input("Enter date to view appointments (YYYY-MM-DD): ")
            appointments = scheduler.get_appointments(date)
            if appointments:
                print(f"Appointments on {date}:")
                for patient, time in appointments:
                    print(f"{patient} at {time}")
            else:
                print(f"No appointments on {date}")
        elif choice == "3":
            date = input("Enter appointment date (YYYY-MM-DD): ")
            patient_name = input("Enter patient name: ")
            scheduler.cancel_appointment(date, patient_name)
        elif choice == "4":
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
