
# halo
Framework used:

Flask
SQLAlchemy
Flask-sqlalchemy
Flask-bcrypt
Flask-session

Not Implemented:
1. No Validation - No protection when entries from HTML are invalid or empty
2. No GUI Optimization -- simply make it work, and dress up later.  Use alert for login screen too.
3. Reusing same form for login and registration -- just to save some typing 
4. No password confirmation field (linked to 1, no validation)
5. Since no validation, if a new key matches existing key, it will overwrite, rather than wraning

