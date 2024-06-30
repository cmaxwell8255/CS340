# CS340

How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

Writing programs that are maintainable, readable, and adaptable depends on what functions have been added, what order the code and comments are in, and how well the code has been updated. The right functions for a program should be reusable to avoid writing new code every time and for easy maintenance. The order is important because anyone who looks at the code in the future should be able to read it and know what it says. I can use this code in the future for website design or other projects at work or school.

How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

Working in mainframes I have already learned not to present a problem without a solution. For any programming issue, I look at the problem and determine a potential solution. I then look at what tools or software I will need and refer back to any documentation we already have for it. I have never used the tools we used for this project so the approach was different from previous courses where we used tools and software I'm more familiar with.

What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists keep this world running by creating, maintaining, and updating programs. Without computer scientists we would not have video games, smartphones, POS systems, or other forms of technology that we use every day. At the company I already work at, we use graphs and charts every day so the project for this course really helped me understand what our system programmers have to do to simplify what I see.

About the Project/Project Title

Grazioso Salvare needs a program that can quickly search for animals available for adoption at the shelter. The project team’s goal is to create this program using CRUD operations in Python. The program should be capable of searching for, updating, and deleting animals in the system as well as creating charts and graphs to analyze how many of what breed, age group, sex, etc. are in the shelter.

Motivation
The motivation for this project comes from the need to be able to quickly and efficiently search for dogs that are available for adoption by utilizing a user-friendly program. 

Getting Started
Follow the steps in Usage and Code Example to import, view, and update the shelter database.

Installation Tools 
•	Jupyter Notebook 
•	MongoDB – used with Python scripts making it easier to use. Flexible, easily scalable.
•	Python 
•	Dash – used for building interactive dashboards that make the program user-friendly

Usage and Code Example
1.	Import the Austin Animal Center (AAC) database.
2.	Create a username and password with READ/WRITE permissions. 
3.	Confirm user was setup using mongosh and can access the database.
4.	In the Python file, update the _init_function with the correct information for MongoClient. AnimalShelter.py
5.   	Make sure the username and password match the user that was just created.
6.	Create – insert the data for the record you want added to the system: 
7.	Read – insert the data you are looking for to print results on the screen:
8.	Update – insert the data you are looking for and the new data to update the record with:
9.	Delete – call the delete function using the data you are looking for:
10.	Make the necessary changes to your .ypnb file. See sample code below for creating a bar graph:

Def update_graphs(viewData):
    ###FIX ME ####
    # add code for chart of your choice (e.g. pie chart) #
    dff = pd.DataFrame.from_dict(viewData)
        return [
        dcc.Graph(
           figure = px.bar(dff, x='breed')
       )
   ]
Tests

Summary
	This project was completed by first importing the AAC file into MongoDB. Then I created a username and password giving the user read/write permission. Using Python, I created a CRUD program to create, read, update, and delete data from the AAC file. From there, I used an already written program with Dash framework to import an image for Grazioso Salvare and created tables, charts, maps, etc. to show the data to the user in an easy-to-read way.
Challenges
	I had challenges with my Python file connecting to MongoDB as well as applying the correct permissions to the username I created. 

Contact
Your name: Courtney Maxwell
