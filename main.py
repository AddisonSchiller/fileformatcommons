from flask import Flask,request
from mako.lookup import TemplateLookup
from datetime import datetime
from files import file_data
from parse import parse_data,file_search
app = Flask(__name__)

mako_lookup = TemplateLookup(directories=['templates'])


def render(filename, **kwargs):

    t = mako_lookup.get_template(filename).render(**kwargs)
    return t

app = Flask(__name__)

@app.route('/')
def main_page():
    return render('home.mako')

@app.route('/search/<file_query>/')
def show_results(file_query):
	hits = file_search(file_query,file_data)
	return render("search_index.mako",
            hits=hits,
            )


@app.route('/file/<file_type>/')
def show_file(file_type):
    try:
        return render("display_file.mako",
                data=file_type,
                file_type=file_type,
                ext=file_data[file_type]["ext"],
                name=file_data[file_type]["name"],
                download=file_data[file_type]["download"],
                icon=file_data[file_type]["icon"],
                wiki=file_data[file_type]["wiki"],
                tags=", ".join(file_data[file_type]["tags"]),
                file_kind=file_data[file_type]["file_kind"][0],
                popularity=file_data[file_type]["popularity"],
                usability=file_data[file_type]["usability"],
                about=file_data[file_type]["about"],
                )
    except: 
        return main_page()

