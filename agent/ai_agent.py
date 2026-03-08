def process_request(text):

    if "book" in text:
        return "Appointment booked"

    if "cancel" in text:
        return "Appointment cancelled"

    return "Sorry, I couldn't understand the request."
