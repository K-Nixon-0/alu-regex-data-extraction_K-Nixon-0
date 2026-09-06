import html
import json
import os
import re #First time use (Import re) but it stands for "regular expressions"


# Different ALU emails datatypes
alu_official_type = r"\b[a-zA-Z0-9._%+-]+@alueducation\.com\b"
alu_alumni_type = r"\b[a-zA-Z0-9._%+-]+@alumni\.alueducation\.com\b"
alu_si_type = r"\b[a-zA-Z0-9._%+-]+@si\.alueducation\.com\b"
all_email_type = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

# Credit card datatypes
card_type = r"\b(?:\d{4}[-\s]?){3}\d{4}\b|\b\d{13,16}\b"

# Also data types
phone_type = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
url_type = r"https?://[^\s<>\"]+|www\.[^\s<>\"]+"
time_type = r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b"
money_type = r"\$?\b\d{1,3}(?:,\d{3})*(?:\.\d{2})?\b"

# Hiding the last 4 digits of a credit card number for security purposes
def hide_card_digits(card_number):
    only_numbers = re.sub(r"\D", "", card_number)
    if len(only_numbers) >= 13:
        return "****-****-****-" + only_numbers[-4:]
    return "****"

# Function to find all datatpes in raw-text.txt
def find_all_data(text):
    found_cards = re.findall(card_type, text)
    found_phones = re.findall(phone_type, text)
    found_urls = re.findall(url_type, text)
    found_times = re.findall(time_type, text)
    found_money = re.findall(money_type, text)
    all_emails = re.findall(all_email_type, text)
    alu_official = re.findall(alu_official_type, text)
    alu_alumni = re.findall(alu_alumni_type, text)
    alu_si = re.findall(alu_si_type, text)

    safe_cards = []
    for card in found_cards:
        safe_cards.append(hide_card_digits(card))

    result_data = {
        "emails": {
            "all_extracted": [html.escape(e) for e in set(all_emails)],
            "alu_official": [html.escape(e) for e in set(alu_official)],
            "alu_alumni": [html.escape(e) for e in set(alu_alumni)],
            "alu_si": [html.escape(e) for e in set(alu_si)],
        },
        "urls": [html.escape(u) for u in set(found_urls)],
        "credit_cards": safe_cards,
        "phone_numbers": [html.escape(p) for p in set(found_phones)],
        "time_formats": [html.escape(t) for t in set(found_times)],
        "currency_amounts": [html.escape(m) for m in set(found_money)],
    }

    return result_data

def start_program():

    current_folder = os.path.dirname(os.path.abspath(__file__))
    project_folder = os.path.abspath(os.path.join(current_folder, ".."))

    # Looks for raw-text.txt file in input
    file_path = os.path.join(project_folder, "input", "raw-text.txt")
    if not os.path.exists(file_path):
        file_path = os.path.join(project_folder, "raw-text.txt")

    output_path = os.path.join(project_folder, "output", "sample-output.json")

    # Read raw-text.txt file
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            my_text = f.read()
    except FileNotFoundError:
        print("----------------------------------------------------------------")
        print("Error: Could not find raw-text.txt file!")
        return

    # Extract data
    extracted_results = find_all_data(my_text)

    # Make output folder if it doesnot exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save to output json file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(extracted_results, f, indent=4)
    
    print("----------------------------------------------------------------")
    print("Done! Output saved to output/sample-output.json")

if __name__ == "__main__":
    start_program()