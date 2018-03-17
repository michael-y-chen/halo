

Framework used:

Flask
SQLAlchemy
Flask-sqlalchemy
Flask-bcrypt
Flask-session

Not Implemented:
1. No Validation - No protection when entries from HTML are invalid or empty
2. No GUI Optimization -- simply make it work, and dress up later.  Use alert for login screen too.
3. Reusing same form for login and registration -- just to save some typing (per 2, simple GUI)
4. No password confirmation field (per 1, no validation)
5. Since no validation, if a new key matches existing key, it will overwrite, rather than warning
6. Database is created at /tmp/test.db in sqlite 

TESTING URL:
 /showall will display both User and Record database entries, it is a straight JSON dump.


