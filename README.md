Edyn created this as a guide.
***
#### CURRENT BUGS: ####
* Logout page is not actually logging user out
    * Can redirect back to main page (Maybe fixed?)
    
***
#### SETUP: ####

To migrate any data before running server: 
* python manage.py migrate

To run server:
* python manage.py runserver

***

#### AUTHENTICATION: ####

To create an admin: 
* python manage.py createsuperuser

Info Already Created:

* Admin Username: admin

* Admin Email: admin@adelaide.edu.au

* Admin Password: password

Require Login to access any page:
* @login_required added before def
    * e.g 
    
        * @login_required 
    
            def index(request):
***
#### URLS: ####
* /admin
* /data
* /data/outliers
* /settings
* "index" (Blank)
* /wineTable

***
#### DIRECTORY STRUCTURE: ####
* dashboard
    * This is where any url other than admin is setup
    * Can also add any models etc. here.
    * Consider it the same as the "polls" from the tutorial
* static
    * assets
        * This contains all the files used to render the pages
    * csv_table
        * This is exclusively for rendering the CSV Table as we may have to delete
        * CSV is at location static/csv_table/data
* templates
    * This is where any of the html pages to be rendered are stored
    
* wineWebsite
    * This is the root project folder.
***
#### BOOTSTRAP STUDIO: ####
The pages have been created in bootstrap studio

To simplify the testing on the inbuilt preview in bootstrap and Django, an export script is used
File Name: 
* bootstrap_script.py

Export Script Description:
   * Bootstrap Studio --> After Export
   * /assets --> /static/assets
   * href="filename.html" --> href="{% url 'filename'%}"
      * Using this structure to use the named URLS from urls.py in dashboard
        * Location: wineWebsite/dashboard/urls.py
        * Example for data:
            * Code: path('data/', views.data, name='data'),
            * Change: href="data.html" --> href="{% url 'data'%}"

***
#### OTHER: ####

* Clicking Download as CSV in Dashboard shows raw data