appointments = []

def check_availability(doctor):
    return ["10:30 AM", "2:00 PM", "4:30 PM"]

def book_appointment(doctor, slot):
    appointment = {
        "doctor": doctor,
        "slot": slot
    }
    appointments.append(appointment)
    return f"Appointment booked with {doctor} at {slot}"

def cancel_appointment():
    if appointments:
        appointments.pop()
        return "Appointment cancelled"
    return "No appointment found"
