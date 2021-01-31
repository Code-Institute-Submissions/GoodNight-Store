# Good Night - all what you need is a good sleep.

Good Night project is my final project during studing Software Web Developing in Code Institute. It is a e-commerce website with products which give better sleep.
My wife and I came up with the idea when we both sat sleepy after a day's work. That day I decided that whatever happened in the evening I would have an idea for my last milestone project. And we came up with an online store with a 'good sleep' product. A 'good sleep' that customers will be able to get when buying products in the store.
Products such as pajamas, pillows, bedding and aromatherapy accessories. I also decide to add blog section in the service, where user can find useful information about products itself, sleeping, relaxing.

# UX

I started designing the website with a two necessary assumptions:
-   modern design,
-   responsiveness.

To find more details of the requirements, I have defined a group of people who will be potential customers of the store and what are the needs of them. 
They will be people of all ages, who like to sleep, who care about the comfort of sleep and for whom sleep is relaxation. They will also be parents and people who wear pajamas.
Users will come to the website to find way of better sleep and the products for good sleeping. To help achieve this, I have defined further requirements, such as:
-   friendly design,
-   dreamlike design.

Then I created a user stories to better define the needs and further requirements of the site.

[Open User Stories](Readme-purpose/user-stories.pdf)

# Scope

## Visual requirements

-   modern, friendly design,
-   responsiveness,
-   the color scheme and pictures must be associated with sleeping,
-   first page needs to have main picture, overview of main products,
-   navigation bar needs to contain basket button and categories selectors,
-   products view page needs to display products with image and basic product information displayed in columns different number dependence of the screen size,
-   product page needs to display bigger images and detailed information about product,

I used these requirements to create wireframes.

-   [Home Page - Desktop](Readme-purpose/wireframe-desktop-Home-page.pdf)
-   [Home Page - Mobile](Readme-purpose/wireframe-mobile-Home-page.pdf)

## Functional requirements:

1.  Requirements for customer:
-   needs to have possibility to create account
-   in created account can have visibility of the orders history
-   in account can save the delivery/address information
-   can add products to the bag
-   needs to have good visibility of how much he spend already
-   can edit, update products in the bag before makes the order
-   can easly and intutive navigate thru the website
-   can pay for shopping
-   can add own product review
-   can see products review added by others

2. Admin/ service owner:
-   can add products
-   can add the product images
-   can edit and remove products
-   can manage the accounts in service (approve, delete, block)
-   can manage products reviews (have possibility to remove reviews)
-   can add the blog posts
-   can add the image to the blog post
-   can edit and removing blog posts

3. Overall service requirements:
-   service needs to be connected to the database where all information will be stored
-   service needs to have possibility of uploading images

# Surface

## The Colors

Main service colors are blue and black.

## Fonts

*   Main Logo font:  'Exo 2'
*   Main Headings font: 'Assistant'
*   Main regular font: 'DM Sans'

# Features

Please refer to requirements point as all of those are implemented.

# Technologies used:

For detailed packages please refer to requirements.txt file.
The other technologies are listed below:

1. Django v3 as the base framework of the service.
2. Python as the back-end of the service.
3. HTML5 as the front-end of the service.
4. Payment infrastructure via the stripe service - service is using test service and for test below cards can be used:
    -   No authentication: 4242 4242 4242 4242.
    -   Authentication required: 4000 0027 6000 3184.
5. Postgres database via heroku service.
6. AWS S3 - Free cloud storage on Amazon AWS - used for storage static files.
7. AOS animate on scroll for animation used on the homepage.
8. Git for version control.
9. Github for keeping remote respository.
10. VSCode - code editor used during writing the service.
11. django-allauth==0.42.0 for user accounts
12. django-autoslug==1.9.8 for slug field in django blog model
13. Bootstrap v4 as the front-end framework.
14. django messages and bootstrap toasts for displaying messages to the user on service.

# Testing

*   Most of the tests were done during implementation each application and feature and were fixed during the process.
*   I used the two browser for live preview and testing during process: 
    -   Firefox Browser in version 85.0 (64-bit)
    -   Google chrome in version 88.0.4324.104 (64-bit)
    I used the developer tools in both browser to test web responsivness.
*   The service were tested on windows and android devices with different screen size:
    -   24"
    -   17"
    -   5"
    -   10"
*   I used code validators to check errors and beautify code:
    -   https://validator.w3.org/ - for HTML
    -   https://jigsaw.w3.org/css-validator/ - for CSS
    -   http://beautifytools.com/javascript-validator.php - for JavaScript
    -   https://extendsclass.com/python-tester.html - for python syntax check
*   I used the https://temp-mail.org/ to check creating account, password change and removing account.
*   To test service I go thru whole process of creating account to buy products.
*   I did also send the link for my service to friends for testing.
*   I did end test by adding, removing, editing products and blog posts and also adding products reviews.

# Deployment

Repository is deploed in github. Live service is deployed on the heroku.com. Static files are stored in the AWS S3 free service.

## To run this project locally, please follow below steps:

Before running the project locally you need to have installed python and Django, then follow next steps:

1. Open my Github Repository https://github.com/dejvoss/GoodNight-Store
2. Clone or download the code by clicking on green Code button.
3. Open code editor with terminal
4. install packages from requirements.txt file.
5. Create environmental variables and save in .env file in goodnight_store folder. Environmental file should contain bellow variables:
    *   DEBUG - 1 to display of detailed error pages. (don't run a site into production with Debug turned on - for production puprose debug should be set to 0)
    *   SECRET_KEY - DJANGO SECRET KEY (you can generate one on https://djecrety.ir/)
    For payment works you should also save the Stripe variables as below (you can find all of those by creating account in stripe.com and looking in to the developers menu in stripe dashboard):
    *   STRIPE_PUBLIC_KEY
    *   STRIPE_SECRET_KEY
    *   STRIPE_WH_KEY
6. Make migrations by typing in termianl 'python manage.py migrations --show' to display all migrations and 'python manage.py migrate' - to make all migrations, be sure that you are in terminal in the folder where manage.py file is
7. Run the server by typing 'python manage.py runserver'
8. Create a superuser to open admin service page by typing 'python manage.py createsuperuser' and follow the instructions in terminal.

# Credits:

## Content:

I used https://github.com/ckz8780/boutique_ado_v1/ as guidance especially for bag and checkout applications, partly for product and toast messages.

Text for blog is taken from http://healthysleep.med.harvard.edu/healthy/getting/overcoming/tips

I used the AOS animation on home page from https://michalsnik.github.io/aos/

## Media:

Was taken from internet for not commercial use.
