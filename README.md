# Django Address Book API

## Overview
This repository contains a **Django Address Book API** that enables users to manage their contacts. It includes user authentication and CRUD operations for managing contact details. The project is built using Django and Django REST Framework (DRF), showcasing best practices in API development followed by **[Differenz System](http://www.differenzsystem.)**.

## Features
1. **User Authentication:**
   - Built-in Django authentication system.

2. **Contact Management:**
   - Add new contacts.
   - Retrieve all contacts.
   - Update contact details.
   - Delete contacts.

3. **Scalability and Modularity:**
   - Structured application with reusable components.

## Prerequisites
1. [Python 3.8+](https://www.python.org/downloads/)
2. [Pip](https://pip.pypa.io/en/stable/)
3. [Virtualenv](https://virtualenv.pypa.io/en/latest/)
4. [SQLite (default)](https://www.sqlite.org/index.html) or [Other databases](https://docs.djangoproject.com/en/stable/ref/databases/)

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/differenz-system/AddressBook-Python-Django-Rest-framework
cd AddressBook-Python-Django-Rest-framework
```

### 2. Set Up the Environment
1. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser for the admin panel (optional):
   ```bash
   python manage.py createsuperuser
   ```

### 3. Run the Server
Start the Django development server:
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000`.

## Project Structure
```
addressbook/
├── app/                  # Main app containing models, views, and serializers
│   ├── admin.py          # Admin panel configurations
│   ├── models.py         # Database models
│   ├── serializers.py    # API serializers
│   ├── views.py          # API views
│   ├── urls.py           # App-specific routes
├── addressbook/          # Project configuration
│   ├── settings.py       # Project settings
│   ├── urls.py           # Project routes
│   ├── wsgi.py           # WSGI entry point
├── manage.py             # Django management tool
```

## API Endpoints
### Authentication
- Authentication is handled by Django's built-in system. Use the admin panel to manage users if necessary.

### Contact Management
#### Get All Contacts
**GET** `/app/contacts/`

**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "1234567890",
    "address": "123 Main St"
  }
]
```

#### Add a Contact
**POST** `/app/contacts/`

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "address": "123 Main St"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "address": "123 Main St"
}
```

#### Update a Contact
**PUT** `/app/contacts/{id}/`

**Request Body:**
```json
{
  "name": "John Smith",
  "email": "john.smith@example.com",
  "phone": "9876543210",
  "address": "456 Elm St"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "John Smith",
  "email": "john.smith@example.com",
  "phone": "9876543210",
  "address": "456 Elm St"
}
```

#### Delete a Contact
**DELETE** `/app/contacts/{id}/`

**Response:**
```json
{
  "message": "Contact deleted successfully"
}
```

## Troubleshooting
### Common Issues
1. **Database Migration Errors:** Ensure migrations are applied:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Dependency Issues:** Verify dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

3. **Server Errors:** Check logs for debugging:
   ```bash
   python manage.py runserver
   ```

### Useful Commands
- Start the server: `python manage.py runserver`
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`

## Support
If you encounter any issues, feel free to [open an issue](https://github.com/differenz-system/AddressBook-Python-Django-Rest-framework/issues).
