import streamlit as st             
import matplotlib.pyplot as plt    
from utils import (
    get_personalized_response, 
    get_weather_data, 
    check_severe_weather, 
    process_weather_data
)

from internacionalization import (
    title, 
    city_field, 
    user_question, 
    checkbox_notifications, 
    spinner_text,
    button_forest, 
    response_ai_title,
    warning_message    
)


def main():
    """Main function to run the Streamlit app."""

    # Set the title of the web app
    st.title(f"🤖 {title} 🤖")  

    # Get user input for the city and the weather question
    city = st.text_input(f"{city_field}:")
    question = st.text_input(f"{user_question}:")

    # Checkbox to enable/disable weather notifications
    notification_enabled = st.checkbox(checkbox_notifications)

    # When the "Get Forecast" button is clicked
    if st.button(button_forest):
        if city and question:  # Check if both city and question are provided
            with st.spinner(spinner_text): 
                response = get_personalized_response(city, question)  
                st.subheader(f"{response_ai_title}:")
                st.write(response)  

                # Get weather data and create a plot
                weather_data = get_weather_data(city)  
                fig, ax = plt.subplots()
                process_weather_data(weather_data)
                st.pyplot(fig)

                # Check for severe weather and display a notification if enabled
                if notification_enabled:  
                    st.write(check_severe_weather(weather_data)) 
        else:  # Show a warning if either city or question is missing
            st.warning(warning_message)

# Entry point for the script
if __name__ == "__main__":
    main()  # Run the main function
