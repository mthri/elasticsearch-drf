### Running the Application

To run the application, please follow these steps:

1. Create an `.env` file in the project directory and add the following environment variables:
   - SECRET_KEY: [your_secret_key]
   - DEBUG: [True/False]
   - DATABASE_NAME: [your_database_name]
   - DATABASE_USER: [your_database_user]
   - DATABASE_PASSWORD: [your_database_password]
   - DATABASE_HOST: [your_database_host]
   - DATABASE_PORT: [your_database_port]
   - ELASTICSEARCH_HOST_PORT: [your_elasticsearch_host_port]

2. Open a terminal or command prompt and navigate to the project directory.

3. Set up a virtual environment by running the following command:
   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```

5. Install the required dependencies by running the following command:
   ```bash
   pip3 install -r requirements.txt
   ```

6. Apply the database migrations:
   ```bash
   python3 manage.py migrate
   ```

7. Initialize the necessary groups:
   ```bash
   python3 manage.py init_group
   ```

8. Start the development server:
   ```bash
   python3 manage.py runserver
   ```

The application should now be up and running locally. You can access it by opening a web browser and visiting the specified URL provided by the development server.