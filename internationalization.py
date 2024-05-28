import json

def load_config(filename="config.json"):
    """Loads configuration data from the specified JSON file."""
    with open(filename, "r", encoding="utf-8") as config_file:
        config_data = json.load(config_file)  
    return config_data

# Load configuration settings from config.json
config = load_config()

# Extract internationalization strings for Portuguese (Brazil)
pt_br_config = config["internacionalization"]["pt-br"]

# Assign values to variables from the configuration file
title = pt_br_config["title"]               
city_field = pt_br_config["city_field"]      
user_question = pt_br_config["user_question"]  
checkbox_notifications = pt_br_config["checkbox_notifications"] 
button_forest = pt_br_config["button_forest"]   
response_ai_title = pt_br_config["response_ai_title"] 
title_graphic = pt_br_config["title_graphic"]  
y_graphic = pt_br_config["y_graphic"] 
x_graphic = pt_br_config["x_graphic"] 
spinner_text = pt_br_config["spinner_text"]
warning_message = pt_br_config["warning_message"]
alert_text = pt_br_config["alert_text"]
