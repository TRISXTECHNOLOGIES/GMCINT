from werkzeug.security import generate_password_hash

password = generate_password_hash('super')
print(password)