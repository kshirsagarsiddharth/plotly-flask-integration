from flask_dir import app, flask_app
from flask_dir.plotlydash.dashboard import layout
app.layout = layout



if __name__ == "__main__":
    flask_app.run(debug=True)

