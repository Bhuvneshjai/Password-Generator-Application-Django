# Password Generator Application
## Overview
Password Generator Django is a web application built with Django that allows users to generate strong, secure passwords based on various criteria. The application also includes user authentication, allowing users to input their name to personalize the experience.

## Features
- User authentication with a username
- Password generation based on user-inputted criteria
- Attractive UI using Bootstrap and custom CSS
- Gradient background and modern design
- Form validation

## Project Structure
![image](https://github.com/user-attachments/assets/3729b349-6234-42b6-a8cf-92c34fc8d10a)

## Setup Instructions
### Prerequisites
- Python 3.8
- Django

### Installation
1. Clone the repository:
   * git clone https://github.com/yourusername/password-generator-django.git
   * cd password-generator-django

3. Create and activate a virtual environment:
   * python -m venv env
   * source env/bin/activate, (On Windows, use `env\Scripts\activate`)

3. Install the required packages:
   * pip install -r requirements.txt

4. Apply migrations:
   * python manage.py migrate

5. Run the development server:
   * python manage.py runserver

6. Open the application in your browser:
Visit http://127.0.0.1:8000/ to see the application running.

## Usage
1. Home Page:
   * Enter your username to log in.
   * Form validation ensures only alphabetic characters with one space are allowed in the username.

2. Password Generator Page:
   * Fill in the form with your name, date of birth, email ID, and mobile number.
   * Select the criteria to include in the password.
   * Click the "Generate Password" button to see the generated password.

3. Result Page:
   * View your generated password.
   * Options to generate another password or log out.

## Screenshots
1. Home Page
![image](https://github.com/user-attachments/assets/ac22cb11-235d-411e-af58-b9432e54dc67)
2. Password Generator Page
![image](https://github.com/user-attachments/assets/02ebf170-6d85-4f74-982e-7d643fc3db05)
3. Result Password Page
![image](https://github.com/user-attachments/assets/ef2cc3e7-a781-4e27-b9c8-c074015e621f)

## Contributing
Feel free to fork this repository, make your changes, and create a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

### Notes:
- Ensure you replace the placeholder GitHub URL with your actual repository URL.
- Add appropriate screenshots to the `images` directory and update the screenshot links in the README accordingly.
- Create a `requirements.txt` file that includes all dependencies, such as Django and any other packages you might be using.
- Add a `LICENSE` file to your repository if it is not already included.
