from flaskblog import create_app

def application():
    app  = create_app()
    app.run()

# if __name__=="__main__":
#     app.run(debug=True)