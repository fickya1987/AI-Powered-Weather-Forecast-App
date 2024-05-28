
# AI-Powered Weather Forecast App

## Description

This Streamlit application aims to provide weather forecasts by leveraging the OpenWeatherMap API and generate insightful responses using a Groq-hosted open-source AI model. 

## Installation

### Prerequisites
Ensure you have Python 3.7+ installed on your system.

### Step-by-Step Guide

1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install the Required Packages**
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

### Setting Up Credentials

You need to configure the `config.json` file with your API credentials. Below is an example of how your `config.json` should look:

```json
{
  "openweathermap": {
    "api_key": "<YOUR_OPENWEATHERMAP_API_KEY>",
    "base_url": "http://api.openweathermap.org/data/2.5/weather"
  },
  "groq": {
    "api_key": "<YOUR_API_GROQ_TOKEN_KEY>",
    "base_url": "https://api.groq.com/openai/v1/chat/completions"
  },
  "internacionalization": {
    "pt-br": {
      "title": "Previsão do tempo com AI",
      "city_field": "Nome da cidade",
      "user_question": "Faça uma pergunta sobre o tempo",
      "checkbox_notifications": "Habilitar notificações",
      "button_forest": "Obter previsão do tempo",
      "response_ai_title": "Resposta AI",
      "title_graphic": "Previsão do tempo",
      "y_graphic": "Humidade (%)",
      "x_graphic": "Temperatura (°C)",
      "spinner_text": "Consultando resposta IA e dados metereológicos...",
      "warning_message": "Por favor informe a cidade e a questão.",
      "alert_text": "🚨 Alerta para temperatura mais baixas"
    }
  }
}
```

Replace `YOUR_OPENWEATHERMAP_API_KEY` and `YOUR_API_GROQ_TOKEN_KEY` with your actual API keys.

## Running the Application

To run the application, use the following command:

```sh
streamlit run .\main_gui.py
```

This will start the Streamlit server and open the application in your default web browser.

## Internationalization

You can change the texts in the GUI by editing the `config.json` file. The internationalization settings for Portuguese (Brazil) can be found under the `internacionalization` section.

## Troubleshooting

If you encounter any issues during the setup or running of the application, please check the following:

- Ensure that your virtual environment is activated.
- Verify that all required packages are installed correctly.
- Double-check your API keys in the `config.json` file.
- Refer to the Streamlit [documentation](https://docs.streamlit.io) for additional help.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions!

## Contact
For questions or support, please contact me Igor Medeiros [igor.medeiros@gmail.com](mailto:igor.medeiros@gmail.com).
