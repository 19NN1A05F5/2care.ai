def process_request(text):

    if "book" in text:
        return "Appointment booked"

    if "cancel" in text:
        return "Appointment cancelled"

    if "reschedule" in text:
        return "Appointment rescheduled"

    return "Sorry, I couldn't understand the request."
