from flask_dir import app, flask_app, app2
from flask_dir.plotlydash.dashboard import layout, layout2
app.layout = layout
app2.layout = layout2



if __name__ == "__main__":
    flask_app.run(debug=True)

