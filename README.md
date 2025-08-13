Finance Tracker
A simple Django-based personal finance management application to track budgets, categories, and transactions.

Features
-Add, edit, and delete budgets, categories, and transactions
-View lists of all entries
-Simple login system
-Responsive CSS styling

Installation
1. Clone the repository
git clone https://github.com/Hashneet24/finance_tracker.git
cd finance_tracker
2. Create and activate a virtual environment
python -m venv .venv
or
virtualenv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Apply database migrations
python manage.py migrate
5. Create a superuser (optional, for admin access)
python manage.py createsuperuser
6. Run the development server
python manage.py runserver
7. Open the application
Navigate to:
http://127.0.0.1:8000

Technologies Used:
Python 
Django
HTML / CSS


Code Structure
finance_tracker/
│
├── finance_tracker/                # Project settings package
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
│
├── finance/                        # Main app for finance tracking
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__/
│   ├── static/
│   │   └── finance/
│   │       └── style.css
│   └── __pycache__/
│
├── templates/                      # Project-level templates
│   ├── budget_confrim_delete.html
│   ├── budget_form.html
│   ├── budget_list.html
│   ├── category_confirm_delete.html
│   ├── category_form.html
│   ├── category_list.html
│   ├── home.html
│   ├── login.html
│   ├── transaction_confirm_delete.html
│   ├── transaction_form.html
│   └── transaction_list.html
│
└── README.md
