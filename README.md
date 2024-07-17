# Exercise Tracker

## 🏋️‍♂️ Overview

The Exercise Tracker is your personal fitness companion, designed to help you log and monitor your physical activities effortlessly. Utilizing the power of the Nutritionix API, it analyzes the exercises you perform, and with the Sheety API, it stores your exercise data in a Google Sheets document. This seamless integration ensures you have a detailed and organized record of your exercise routines, including the type of exercise, duration, and calories burned.

## ✨ Features

- **Interactive Exercise Logging:** Describe your workout, and the app takes care of the rest.
- **Smart API Integration:**
  - **Nutritionix API:** Breaks down your exercise input to provide specifics like exercise name, duration, and calories burned.
  - **Sheety API:** Logs your exercise data into a Google Sheets document, making it easy to track and review your progress.
- **Detailed Data Logging:** Captures the date and time of each entry along with comprehensive exercise details.
- **Robust Error Handling:** Ensures smooth data processing even when some API responses are incomplete.

## 🛠 Technologies Used

- **Python:** The backbone of our application.
- **Requests Library:** Handles communication with Nutritionix and Sheety APIs.
- **Datetime Module:** Manages date and time for precise logging.
- **OS Module:** Accesses environment variables for API keys and endpoints.

## 📋 Prerequisites

- **API Keys:** Obtain valid API keys for both Nutritionix and Sheety services.
- **Environment Variables:** Set up the following:
  - `nutrition_API_KEY`
  - `nutrition_APPID`
  - `sheety_endpoint`

## 🚀 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/flack74/exercise-tracker.git
    cd exercise-tracker
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure your environment variables:
    ```bash
    export nutrition_API_KEY="your_nutrition_api_key"
    export nutrition_APPID="your_nutrition_app_id"
    export sheety_endpoint="your_sheety_endpoint"
    ```

## 🏃‍♀️ Usage

1. Launch the application:
    ```bash
    python exercise_tracker.py
    ```

2. When prompted, describe the exercise you performed (e.g., "Ran 5 miles").

3. The application will:
   - Send your input to the Nutritionix API for analysis.
   - Log the detailed exercise information to a Google Sheets document via the Sheety API.

4. You will receive confirmation and details of the logged exercise in the console.

## 🔍 Example

```plaintext
Tell me what exercise you did: Ran 5 miles
Added exercise: running
{"workout":{"date":"17/07/2024","time":"14:05:32","exercise":"running","duration":50,"calories":500}}
```

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add your commit message"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Big thanks to [Nutritionix](https://www.nutritionix.com/business/api) for providing the comprehensive exercise analysis API.
- A shout-out to [Sheety](https://sheety.co/) for making Google Sheets integration straightforward and powerful.

---

Feel free to customize this README to better reflect your project's unique aspects and goals.
