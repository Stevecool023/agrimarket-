#!/usr/bin/env python3


from app import create_app

app, db = create_app()

if __name__ == '__main__':
        app.run(debug=True)
