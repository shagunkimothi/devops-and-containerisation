# This program is intentionally basic
# Focus of this task is containerization, not Python

import numpy as np  # dependency for learning purpose

stored_sapid = "500120283"
user_sapid = input("Enter your SAP ID:500120283 ")

if user_sapid == stored_sapid:
    print("Matched")
else:
    print("Not Matched")
