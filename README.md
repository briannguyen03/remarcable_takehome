# Set up

This guide assumes your are on a **Linux/Unix system** so all comands are given in **bash**.

### Setup Script
1. Clone this repo:
   ```bash
   git clone https://github.com/briannguyen03/remarcable_takehome
   cd remarcable_takehome
   ```
  
2. Run the included setup.sh script to automatically set up the **environment**, **install dependencies**, and **start the server**:
   ```bash
    ./setup.sh
    ```
  You might have to do
  ```bash
  chmod +x setup.sh
   ```

3. Open the server in a browser (eg. http://127.0.0.1:8000/)

### Manual Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/briannguyen03/remarcable_takehome
   cd remarcable_takehome
   ```
   
2. Setup the virtual python env:
   ```bash
   python -m venv venv
   ```
4. Activate the venv:
   ```bash
   source venv/bin/activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the dev server:
   ```bash
   python manage.py runserver
   ```
7. Open the server in a browser (eg. http://127.0.0.1:8000/)

# Admin login
login creds
* Username: brian
* Password: password123

# Process

Note: I haven't used django before, so a lot of time was spent going back and forth between the django reference, docs, and tutorial. I did use Gemini to point me to a general topic that I could use to quickly reference the official documentation. 

I stated at **which** and for **what** I used it for below.


Also due me juggling learning the framework during the build, it slipped my mind to commit at each stage, so the commit history will not accurately reflect the time spent for each module

The entire project took me around **~6 hours**, broken down into **5 stages**
1. **Design (40 minutes)**: At this stage I decided I wanted to pursue a "Blockbuster/Netflix" style model where the products are movies. 
   I modeled the relationship between these main tables on a whiteboard, and added aditional tables to support it like, Actor, and Director

2. **catalog/models.py (1 hr)**: Once I had the structure of my models, I started implementing the classes in models.py.
   Most of what I did here, I learned from the django official tutorial and documentation.
  
3. **catalog/views.py (1.5 hr)**: After migrating the model classes. I built the search and filtering logic for the app. I used Gemini to identify relevant sections of the QuerySet API (specifcally Q objects), and cross referenced it for implementation details. This process saved me alot of time, because manually reading through the lengthy docs for a specifc function would have
   taken more time than I had. I also created the urls.py file to add the trigger for my view function, and obviously also editted the global urlConf to include my app.
   
4. **Admin setup and populating the db (1.5 hr)**: I set up the admin config, and added 20 movies, 6 categories, and 10 tags. This part took quite a bit of time because I was manually entering data for each entry.
   I think if I had to do this again I would first just use generic data instead of real movies, and also create a small python script to automate this process

5. **Frontend (30 minutes)**: For this part I relied on the django tutorial to get a hang of the html loop and if syntax, but I also used Gemini to help me work through 'bugs' like the filter options reseting
   after the search button is pressed. And for filtering by category and tags, how to convert the id to a string so that it can be compared with the selected filter. I also applied some minor css styling to make the
   page look more readable

6. **Polishing/Cleanup (1 hr)**: Clean up of the project, created the setup.sh script to automate setup. It was also at this stage that I realized I hadn't commited since the initial project setup, so I tried to simulate that
   by add each stage individually with their own commit message.


   

   

   


