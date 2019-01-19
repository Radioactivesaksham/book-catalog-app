A web application built using flask has google OAuth 2.0 authentication mechanism  also has JSON endpoints for access of database.The web application makes use of basic 4 operations of the internet i.e. CRUD(Create, Read Update and Delete)

## Running the application
Assuming that you working on linux OS.

<code>python database_setup.py</code><br>
<code>python populate_database.py</code><br>
<code>pip install -r requirements.txt</code><br>
<code>python project.py</code>

### In browser, type in
```
http://localhost:8000
```
## API Endpoints

```
http://localhost:8000/catalog/JSON
```
```
http://localhost:8000/catalog/6/8/JSON
```
```
http://localhost:8000/catalog/6/JSON
```
