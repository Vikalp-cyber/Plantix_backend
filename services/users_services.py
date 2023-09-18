from flask import jsonify
from models._init_ import cursor, conn
import hashlib

def is_email_unique(email):
    # Check if the email already exists in the database
    query = 'SELECT COUNT(*) FROM users WHERE email = ?'
    cursor.execute(query, (email,))
    result = cursor.fetchone()

    # If the count is greater than 0, the email is not unique
    return result[0] == 0

def prepare_send_data(data):
    if data:
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        dob = data.get('dob')

        # Check if the email is unique before inserting
        if is_email_unique(email):
            query = '''
                INSERT INTO users (
                name,
                email,
                password,
                dob
                ) VALUES (?,?,?,?)
            '''
            params = (name, email, password, dob)

            cursor.execute(query, params)
            conn.commit()
            return jsonify({"message": "registered successfully"})
        else:
            return jsonify({"error": "Email is already in use"}), 400
    else:
        return jsonify({"error": "No data provided"}), 400

def authenticate_user(data):
    if data:
        email = data.get('email')
        password = data.get('password')

        # Check if a user with the provided email exists in the database
        query = 'SELECT * FROM users WHERE email = ?'
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user:
            # Verify the provided password against the stored password
            stored_password = user[3]

            # Hash the provided password for comparison
            password_hash = password

            if stored_password == password_hash:
                # Passwords match, generate and return an authentication token
                # You can use a library like JWT to generate tokens
                # Example: token = generate_token(user['id'])
                # Replace generate_token with your actual token generation logic
                return jsonify({"message": "Login successful"})
            else:
                return jsonify({"error": "Invalid password"}), 401
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "No data provided"}), 400
