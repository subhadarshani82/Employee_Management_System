## Project Description
Employee_Management_System 
A web application to manage employees with features like:
- Add, Read, Update, Delete (CRUD) employees.
- Search employees by name, email, or contact.
- Validation on blank or invalid entries.
- Shows success/error messages in modals.

## Technology usage
python 3.11.5
django 5.2.5
html,css,bootstrap 5
mysql


## steps to Installation
1. Clone the repository:
git clone <repository_url>

2. Navigate to the project folder:
cd employee_Management_System

3. Create and activate a virtual environment:
#windows
virtualenv venv
venv\Scripts\activate

4. Install dependencies:
pip install -r requirements.txt

5. Apply migrations:
python manage.py migrate

6. Run the development server:
python manage.py runserver

7. Open the app in your browser:
http://127.0.0.1:8000/

## Usage
Click "Add New Employee" to add an employee.
Use "Update" button to modify employee details.
Use "Delete" button to remove an employee.
Use the search bar to search employees by name, email, or contact.
Use "Home" button to return in main employee list page.
Form validation ensures entries are correct, with messages shown in modals.
