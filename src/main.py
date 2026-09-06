import html
import json
import os
import re #First time use (Import re) but it stands for regular expressions


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