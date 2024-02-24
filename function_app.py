import logging
import azure.functions as func
from jinja2 import Environment, FileSystemLoader

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
environment = Environment(loader=FileSystemLoader("templates/"))

# Landing page containing the html that loads htmx.js
@app.route(route="index", auth_level=func.AuthLevel.ANONYMOUS)
def index(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger index processed a request.')

    template = environment.get_template("index.html")
    return func.HttpResponse(
           template.render(), status_code=200, mimetype="text/html"
    )

# This is the function that will be called from index.html using htmx.js
@app.route(route="htmxtest", auth_level=func.AuthLevel.ANONYMOUS)
def htmxtest(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger htmxtest processed a request.')

    return func.HttpResponse( "<div>It worked!</div>", status_code=200, mimetype="text/html")
   
# This is the standard function from Azure abd unrelated to htmx.js
# It shows how to use request parameters
@app.route(route="myhtmxfunc")
def myhtmxfunc(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )