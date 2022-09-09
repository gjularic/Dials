# Dials - Wrist Watch Store

![Home Page](readme_img/main-page.png)

# Overview

### About
* Dials is and fictional ecommerce store that sells a variety of wrist watches for men and women. Built as a Final Full Stack Project.

* The live deployed application can be found here [Dials](https://dials-watches.herokuapp.com/)

# User Experience

## Project goals

* Goal of the project was to show my competency in being able to develop complex full stack application. 
* The users of the site will be able to register and login on the page if they whish to do so. Registration is not needed
to make the purchases, but they can sign up for the newsletter and check out the blog page.

## Agile

## Strategy

* Goals
    * Site Owner Goals
        * to be able to sell the products on the site
        * to be able to display products on the site easily
        * to be able to add, edit, delete all the products
        * to interact with buyers through the newsletter and facebook page
        * to easily navigate the website
        * to be able to modify the content through the owner profile page

    * Customer Goals
        * to easily find the product of interest on the site
        * to be able to navigate the website on any page
        * to be able the add the products to the bag
        * to be able to checkout securely
        * to be able to sign up for the newsletter and check blog for the news



## User Stories
![Agile](readme_img/user-stories.png)

# Features

* The first release includes:
    - A main page where customers can immediately open one of the basic categories
    - They can sign up for the newsletter and check blogs
    - Users can register and login, modify their information and reset the password
    - They are able to add items to the bag and checkout securely using Stripe
    - can purchase items as anonymous
    - users can log out at any time.

* Future features
    * will include the full review option for the products (currently only model and template present)
    * commenting on the blog posts and liking the items

# Features with manual testing

### Login page
![Home Page](readme_img/sign-in.png)

* User can open the webpage from the URL provided and will be asked to log in. If they dont have an account there is a "Sign Up" link which will lead them to register page.
8 Tested and it work without any issues

### Register page
![Register](readme_img/sign-up.png)

* If user doesn't have sign in details already they can register here
* feature has been tested and it's sending the verification emails accordingly

### E-mail verification
![Verify](readme_img/verify.png)

* E-mail verification page is displaying message correctly.
* Tested, emails are being sent though the message will need to be updated

### Products
![Products](readme_img/products.png)

* List of products, can be sorted with filters
* Tested manually, product are benig displayed preperly by price etc.

### Product Detail
![Product detail](readme_img/product-detail.png)

* Product detail page shows all the info about the item, allows users to more all at one and proceed to checkout
* Items are being added properly and the notification shown that the item has been added

### Checkout
![Checkout](readme_img/checkout.png)

* The site user can view all their items and checkout securely
* feature has been tested and test payments are going through and order summary displaying

### Blog
![Blog](readme_img/blog.png)

* currently simple blog page where customers can se some upcoming products

