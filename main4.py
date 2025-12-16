from pyscript import Element, display

def send_message(event=None):
    name = Element("contact_name").value.strip()
    email = Element("contact_email").value.strip()
    message = Element("contact_message").value.strip()

    if not name or not email or not message:
        Element("contact_output").write("<span style='color:#FFCC00;'>Please fill in all fields!</span>")
        return
    
    # Here you could add code to actually send an email or store in database
    Element("contact_output").write(f"""
        <span style='color:#FFD700; font-weight:700;'>Thank you, {name}! Your message has been received.</span>
    """)

    # Clear the form
    Element("contact_name").value = ""
    Element("contact_email").value = ""
    Element("contact_message").value = ""

# Connect button click to function
Element("contact_submit").element.addEventListener("click", send_message)
