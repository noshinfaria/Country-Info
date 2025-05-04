# Country Info Application

This Django project provides country-related information through RESTful APIs. It allows users to view all countries and fetch details of a specific country by its `id`.

---
## Features

- ✅ Fetches all country data from the Countries API
- ✅ Stores data in a relational database

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/noshinfaria/Country-Info.git
cd Country-Info
```
### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```
### 3. Install Requirements
```bash
pip install -r requirements.txt
```
### 4. Apply migrations to set up the database:
```bash
python manage.py migrate
```
### 5. Run the development server:
```bash
python manage.py runserver
```

## Endpoints
### 1. List All Countries
- **URL**: `/api/countries/`
- **Method**: `GET`
- **Description**: Fetch a list of all countries.
- **Response Example**:
  ```json
  [
    {
      "id": 1,
      "name_common": "United States",
      "capital": "Washington, D.C.",
      "region": "Americas",
      "population": 331000000
    },
    ...
  ]
### 2. Retrieve Specific Country by ID

- **URL**: `/api/countries/<int:id>/`
- **Method**: `GET`
- **Description**: Fetch details of a specific country by its ID.
- **URL Params**:
  - `id`: The unique identifier of the country.

- **Example URL**: `/api/countries/1/`

- **Response Example**:
  ```json
  {
    "id": 1,
    "name_common": "United States",
    "capital": "Washington, D.C.",
    "region": "Americas",
    "population": 331000000
  }
### 3. Create a New Country Entry

- **URL**: `/api/countries/`
- **Method**: `POST`
- **Description**: Create a new country entry in the database.
- **Request Body** (JSON):
  ```json
  {
    "name_common": "Japan",
    "name_official": "Japan",
    "capital": "Tokyo",
    "region": "Asia",
    "population": 126300000   
  }
- **Response Example**:
  ```json
    {
        "id": 251,
        "name_common": "Japan",
        "name_official": "Japan",
        "capital": "Tokyo",
        "region": "Asia",
        "subregion": null,
        "population": 126300000,
        "area": null,
        "flag_url": null
    }
### 4. Update an Existing Country

- **URL**: `/api/countries/<int:id>/`
- **Method**: `PUT or PATCH`
- **Description**: Update the details of an existing country entry by its ID.
- **Full Update Request Body (PUT)**:
  ```json
    {
    "name_common": "Japan",
    "name_official": "State of Japan",
    "capital": "Tokyo",
    "region": "Asia",
    "population": 126300000
    }
- **Partial Update Request Body (PATCH)**:
  ```json
    {
    "capital": "New Tokyo"
    }


- **Response Example**:
  ```json
    {
        "id": 251,
        "name_common": "Japan",
        "name_official": "State of Japan",
        "capital": "New Tokyo",
        "region": "Asia",
        "subregion": null,
        "population": 126300000,
        "area": null,
        "flag_url": null
    }
### 5. Delete an Existing Country

- **URL**: `/api/countries/<int:id>/delete/`
- **Method**: `DELETE`
- **Description**: Delete an existing country by its ID.
- **URL Params**:
    - `id`: The unique identifier of the country.
- **Example URL**:  `/api/countries/1/delete/` (Deletes the country with ID = 1)
- **Response Example**:
  ```json
    {
    "detail": "Country deleted successfully."
    }