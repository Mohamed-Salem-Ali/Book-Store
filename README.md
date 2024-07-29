# Django Bookstore Project

This is a Django-based web application for managing a bookstore. The project utilizes Django models, forms, and templates to provide a comprehensive solution for adding, viewing, and managing books in the store.

## Features

- Add, update, and delete books.
- View a list of all books.
- Detailed view for each book.
- Search functionality to find books by title or author.
- User authentication for secure access.

## Tech Stack

- **Framework:** Django
- **Database:** SQLite (default Django database)
- **Front-end:** HTML, CSS (using Django templates)
- **Forms:** Django Forms

## Installation

1. **Clone the repository:**
    ```bash
    git clone (https://github.com/Mohamed-Salem-Ali/Book-Store.git)
    cd Book_Store
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```
    
5. **Create a superuser (admin user):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

### Adding a Book
1. Log in as an admin user.
2. Navigate to the admin interface at `http://127.0.0.1:8000/admin/`.
3. Add a new book using the provided form.

### Viewing Books
1. Go to the homepage.
2. Browse the list of available books.
3. Click on a book title to view detailed information.

### Searching for Books
1. Use the search bar on the homepage.
2. Enter a book title or author name to find specific books.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or inquiries, please contact [mohamed_salem_ali@outlook.com].

---

Happy coding.
