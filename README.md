#Item Catalog App

##Project Description

The gain in this project is to develop an application that provides a list of
items within a variety of categories as well as provide a user registration and
authentication system. Registered users will have the ability to create, edit and
delete their own items.

***

##Requirements

Here are the steps need in order to run this project:

1. Install [vagrant](https://www.vagrantup.com/) and [virtualBox](https://www.virtualbox.org/)
2. Clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm.git)
3. Under the _fullstack-nanodegree-vm_ file Navigate to vagrant file using **git bash** Launch the vagrant VM using command **_(vagrant up)_**
4. Connect to the VM using command **_(vagrant ssh)_**
6. *Do you remember about that folder vagrant under the fullstack-nanodegree-vm?* We will use this folder to share files within the virtual machine. So now we will need to clone the project to this file.

Just navigate to catalog file under the vagrant file and clone [Item Catalog Application](https://github.com/irzelindo/Item-Catalog-Application.git)

***

##Packages
In order to run the app you will need to Install:
1. [flask](http://flask.pocoo.org/)
2. [sqlalchemy](http://docs.sqlalchemy.org/en/latest/intro.html#installation-guide)

***

***

##Run the Application
Navigate to **Item-catalog-Application** in this folder you will find this subfolders:
1. static - where I placed all static files such as *css, images, javascript and etc...*
2. templates - where I placed all templates I used in this project.
3. To run the application just run command **python project.py**  
4. After that open a web browser and type **http://localhost:8000**
5. There is a Json endpoints for those who may planning to use this info.
For another purposes witch can be loaded typing. **http://localhost:8000/catalog/json**
To display all App. categories and **http://localhost:8000/catalog/<int:catalog_id>/items/json**
To display each category items remember to replace _<int:catalog_id>_ in the link with
the category ID. 
