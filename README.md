# Subscription Manager

Subscription Manager is a powerful tool designed to simplify the way you handle your subscriptions. Keeping track of various subscriptions for online services can be challenging. It’s often difficult to get a clear overview of your monthly expenses. Subscription Manager is here to help you manage and monitor all your subscriptions in one place.

The live link can be found here -[Subscription Manager](https://subscription-manager-da751aeb9bdc.herokuapp.com/)

## Table of Contents

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## User Experience (UX)

### User Stories

Some of the user stories could possibly be acceptance criterias instead of user stories, but since they were added later when the user story was already implented they were added as user stories.

#### EPIC | Accounts

- As a user, I want to be able to create an account by providing my email address and a password, so that I can register and log in to the application.
- As a user I can cancel log out so that i don't need to log in again if i change my mind.
- As a administrator I can view, edit, and delete user accounts so that I can manage access to the application

#### EPIC | Navigation

- As a user i can navigate the website using a menu so that i can find the information i am looking for.
- As a user I can read about the application on the start page so that i understand how to use it.

#### EPIC | Subscriptions

- As a user I can add a subscription by filling out a form with the name, cost, and renewal date so that I can see it in my overview.
- As a user I can see a list of all my subscriptions so that i get an overview
- As a user I can edit a subscription so that I can update with relevant information.
- As a user i can delete a subscription from the list so that i only have the relevant subscriptions in my list.
- As a user i can make a subscription inactive so that it’s still on the list so that i can make it active again when i start using it again.
- As a user i can categorize my subscriptions so that i can view costs for each category
- As a user i can see a summary of my total monthly expenses for subscriptions so that I can budget my expenses more effectively.
- As a user i can view the details of a subscription so that i can decide if i want to keep it
- As a user I can add my own service name when i add a subscription so that i can track all my subscriptions even if they are not in the service list
- As a user I want to see subscriptions and services in alphabetical order so that i can easier find what i'm looking for

#### EPIC | Reminders

- As a user i can create a reminder with a custom message for a subscription that will be shown on a specific date so that i can decide whether to keep the subscription or not
- As a user I can receive a reminder so that I remember to manage the subscription
- As a user I can edit a reminder so that I can change the date or message for the reminder
- As a user i can delete a reminder so that it’s not shown when it’s not needed
- As a user I want to receive a mail with my reminder note so that I don't have to log in to the application every day
- As a user I can add a mail address that the reminder will be sent to so that i can receive a mail reminder even if i don't have a mail address on my account

#### EPIC | Services

- As a administrator I can add, edit, and delete services so that I can manage the list of available subscription services

#### EPIC | Categories

- As a administrator I can create, modify, and remove categories so that I can organize subscription services into logical groups.

### Design

The Subscription Manager web application is designed with a user-centric approach, emphasizing an engaging and intuitive user experience. The goal is to provide users with a seamless way to manage and track their various online subscriptions while offering clear insights into their monthly expenses through the strategic use of icons and colors.

- The application's interface is designed to be straightforward, with a clean menu structure that allows users to easily access different sections such as adding subscriptions, viewing subscriptions, setting reminders, and summarizing expenses.
- The interface utilizes icons to represent different actions, such as a plus sign for adding subscriptions and a chart for summary. This visual approach helps users quickly understand and perform tasks without confusion. Icons are also used to visualize the state of the subscription and if there's an active reminder.w
- The layout avoids unnecessary clutter, focusing on essential information and actions. This ensures that users can quickly find what they are looking for without feeling overwhelmed.
- Subscriptions are grouped into categories such as streaming services, music, cloud storage, and more. This categorization helps users understand their spending patterns and identify areas where they might want to cut back.
- Clicking on a subscription reveals detailed information including the service name, monthly cost, category, and any notes. This detail view also provides options to edit or delete the subscription.
- Users can view a summary of expenses by category, allowing them to see how much they spend on different types of services each month.
- Users can set up email reminders for specific subscriptions, with alert icons indicating if a reminder is active and if the reminder has been triggered. This feature ensures users are notified ahead of time, helping them avoid unwanted charges.
- The form for adding new subscriptions is designed to be simple, with auto-fill options for common services and clear input fields for subscription name and monthly price.
- Users can easily update their subscription details through an edit form that mirrors the simplicity of the add subscription form.
- The application is built to be fully responsive, ensuring a seamless experience across devices, whether on a desktop, tablet, or mobile phone.

#### Colour Scheme

Colour...

#### Icons

There is only one static image ...

#### Wireframes

Wireframes were created at an early stage of the project to provide a visualization of how the application would look on both mobile and desktop. During the development process, some minor deviations were made from the original design.

<details>

<summary>Mobile</summary>
<img src="docs/wireframes/LoginPage_mobile.png" width="200">
<img src="docs/wireframes/Signup Page_mobile.png" width="200">
<img src="docs/wireframes/Start page_mobile.png" width="200">
<img src="docs/wireframes/Add Subscription_mobile.png" width="200">
<img src="docs/wireframes/Edit Subscription_mobile.png" width="200">
<img src="docs/wireframes/View Subscription_mobile.png" width="200">

</details>

<details>

<summary>Desktop</summary>

<img src="docs/wireframes/Login Page_desktop.png" width="400">
<img src="docs/wireframes/Signup Page_desktop.png" width="400">
<img src="docs/wireframes/Start Page_desktop.png" width="400">
<img src="docs/wireframes/Add Subscription_desktop.png" width="400">
<img src="docs/wireframes/Edit_Subscription_desktop.png" width="400">
<img src="docs/wireframes/View_Subscription_desktop.png" width="400">

</details>

## Agile Methodology

The project was structured into five one-week sprints, each beginning with a planning session that utilized the MoSCoW method for prioritizing user stories and issues from the backlog. Detailed acceptance criteria and tasks were defined for each user story to ensure clarity and focus. Throughout the sprints, minor adjustments were made to accommodate new insights and challenges, ensuring that the project stayed on track and met its objectives effectively.

Link to GitHub project: [Subscription Manager board](https://github.com/users/andersganander/projects/4)

<details>
<summary>Sprint 1</summary>

**Objective:** First sprint. Objective is to set up the project, implement at least one admin user story and make first deploy to Heroku.

![Sprint 1](docs/readme_images/sprints/Sprint_1.jpg)


The goals of the sprint were achieved except for the deployment to Heroku, which was not done. This will instead be one of the goals for the next sprint.

</details>

<details>
<summary>Sprint 2</summary>

**Objective:** Add model and basic functionality for subscriptions. First deploy to Heroku.

![Sprint 2](docs/readme_images/sprints/Sprint_2.jpg)

</details>

<details>
<summary>Sprint 3</summary>

**Objective:** Add styling with materialize for signup, llogin, edit and add. Functionality for adding reminders. Fix routing for first page. Add logic for checking if user is logged in.

Some of the user stories didn’t have any tasks when the sprint was started since they were dependent on decisions that would be made in user storys that was to be implemented earlier in the sprint. 

![Sprint 3 start](docs/readme_images/sprints/Sprint_3.jpg)

**Changes during sprint:**
- During the work with subscription details in the subscription list there were som design changes that affected the data models. Since the most important design principle in this project is simplicity and making it as easy as possible for the user to manage their subscriptions the following decisions were made:
  - Add fields for reminder date and reminder note into the subscription detail.<br>
    **Reason:** There’s a risk for adding complexity and making the user confused if reminders are handled separately. It will also be easier for the user to manage reminders together with the subscription.
  - Remove expiry date.<br>
    **Reason:** The sole purpose of the expiry date was to create automatic reminders connected to the expiry date, but since the custom reminder is now handled in a more intuitive way there’s no need for it anymore.
  - Remove payment method<br>
    **Reason:** 
  - Change Notes from TextField to CharField<br>
    **Reason:** It has been discovered that the need for being able to write long messages was overrated.

**Added user stories during sprint:**
- Add Authentication was added to the sprint and decided to be implemented instead of Information architecture
- Add custom service name for subscription.
  During the sprint it was obvious that there was a need for the possibility to add your own name to identify your subscription.

**Problems encountered during sprint:**
While working on USER STORY: Add subscription easily [#43](https://github.com/andersganander/Subscription_manager/issues/43) several problems were encountered:

In order to get the functionality to work so that the text field for price could be automatically populated with the service’s default price i need some way to send data from the view to the template to use in in javascript. This wasn’t so easy as i had expected. After realizing that i would need JSON i tried to send JSON data using the context variable.

<u>Problem 1:</u>

After creating the JSON data and adding it to the context variable something happened with the rendering of the page. Only the source was shown without rendering. 
Solution: After troubleshooting and trying a lot of different things i discovered that i had two context variables, one explicit context and one implicit ('form': form
). The solution was to add the form to the context variable.

<u>Problem 2:</u>

After the first problem was solved the page was rendered with the form and everything looked fine. The next challenge was to fetch data from the JSON object when an option was selected in the select element with javascript. Though i could see the JSON object i wasn’t able to fetch the price with the service name as key. After a lot of troubleshooting i contacted tutor support which could help me to solve the problem.The solution was to remove json.dumps in the view as it made the JSON object being converted to a string.

</details>

<details>
<summary>Sprint 4</summary>

**Objective:** All functionality implemented including mail reminders. Responsiveness issues fixed. Tests started. About page implemented. All routing fixed.

In the planning of Sprint 4, it was decided to remove one of the user stories. Since expiry date was removed in sprint 3, there was no longer any need for expiry date reminders. This can be achieved by the user by creating a custom reminder.

![Sprint 4](docs/readme_images/sprints/Sprint_4.jpg)

**Decisions:**
While planning the user story “Mail reminder” the idea was to keep track of if a reminder has been sent by adding a field in the database. The reason behind this was the following warning in the Heroku Scheduler documentation:<br>
“Scheduler job execution is expected but not guaranteed. Scheduler is known to occasionally (but rarely) miss the execution of scheduled jobs.”

Therefore there was a suggestion to run the job more than once a day and to check if a reminder was sent or not. This was later abandoned due to several reasons:
- The mail functionality is not critical since the reminder will also be shown in the app.
- Adding a field in the model adds complexity since the reminders are a part of the subscriptions and not an own entity. 

**Retro:**
The  objective was not entirely reached and several activities had to be moved to the last sprint du to project members participation in the june hackathon which partly took place in Gothenburg.

</details>

<details>
<summary>Sprint 5</summary>

**Objective:** Last sprint. 

![Sprint 1](docs/readme_images/sprints/Sprint_5.jpg)


</details>


## Data Model

I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views.

The diagram below details the database schema.

Describe changes made during development...

![ER Diagram](docs/readme_images/SubCheck_ER_FINAL.drawio.png)

## Testing

Testing and results can be found [here](/TESTING.md)

## Security Features and Defensive Design (???)

### User Authentication

### Form Validation

If incorrect or empty data is added to a form, the form won't submit and a warning will appear to the user informing them what field raised the error.

### Database Security

The database url and secret key are stored in the env.py file to prevent unwanted connections to the database and this was set up before the first push to Github.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

### Custom error pages:

Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

- 400 Bad Request - The Easy Eater is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - The Easy Eater is currently unable to handle this request

## Features

### Login and sign up

- Start page - login
- Sign up

### Navigation

**Navbar**

- Clickin

**Sidemenu**

* wqwq

### Subscription

- The home page includes a call to action section which encourages the user to sign up to the site w

**Add subscription**

![header](docs/readme_images/features/what_we_do.png)

- The "What We Do' section gives a brief overview of what the site has to offer and summarises the basic features with three simple steps illustrated with font-awesome icons.

**Edit subscription**

![header](docs/readme_images/features/what_we_do.png)

- The "What We Do' section gives a brief overview of what the site has to offer and summarises the basic features with three simple steps illustrated with font-awesome icons.

**Delete subscription**

![header](docs/readme_images/features/what_we_do.png)

- The "What We Do' section gives a brief overview of what the site has to offer and summarises the basic features with three simple steps illustrated with font-awesome icons.

**Add reminder**

![header](docs/readme_images/features/what_we_do.png)

- The "What We Do' section gives a brief overview of what the site has to offer and summarises the basic features with three simple steps illustrated with font-awesome icons.

**Edit reminder**

![header](docs/readme_images/features/what_we_do.png)

- The "What We Do' section gives a brief overview of what the site has to offer and summarises the basic features with three simple steps illustrated with font-awesome icons.

**Clear reminder**

![header](docs/readme_images/features/what_we_do.png)

- The "What We Do' section gives a brief overview of what the site has to offer and summarises the basic features with three simple steps illustrated with font-awesome icons.

**Summary view**

![header](docs/readme_images/features/what_we_do.png)

- The "What We Do' section gives a brief overview of what the site has to offer and summarises the basic features with three simple steps illustrated with font-awesome icons.

### Error Pages

Custom Error Pages were created to give the user more information on the error and to guide them back to the site.

![header](docs/readme_images/features/403_error.png)

- 400 Bad Request - The Easy Eater is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - The Easy Eater is currently unable to handle this request

### Not implemented

- As a user I can receive a reminder when a subscription is nearing its expiry date so that i can decide whether to cancel the subscription or not
-

### Future Features

The following user stories and functionality ...

- As a user i can simulate canceling and adding subscriptions so that i can understand how it affects my monthly cost
- As a user i can view all my reminders in a list so that i can get an overview and quickyly clear or add reminders
- As a user i can suggest a service that is missing so that it can be added to the list
- As an administrator i can view a list of suggested services so that i can decide if they will be added to the service list

## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:

- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next select your region.
- Click on the Create App button.

### Attach the Postgres database:

- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file:

- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py
- Add the cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files / directories

- Create requirements.txt file
- Create three directories in the main directory; media, storage and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi

### Update Heroku Config Vars

Add the following Config Vars in Heroku:

- SECRET_KEY value
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy

- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.

## Forking this repository

- Locate the repository at this link [The Easy Eater](https://github.com/AliOKeeffe/PP4_My_Meal_Planner).
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
- A copy of the repository is now created.

## Cloning this repository

To clone this repository follow the below steps:

1. Locate the repository at this link [The Easy Eater](https://github.com/AliOKeeffe/PP4_My_Meal_Planner).
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided.
3. Open **Terminal**.
4. In Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier.
6. Type **'Enter'** to create the local clone.

## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks - Libraries - Programs Used

- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [PostgreSQL](https://www.postgresql.org/) was used as the database for this project.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud based platform to deploy the site on.
- [Responsinator](http://www.responsinator.com/) - Used to verify responsiveness of website on different devices.
- [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and performance.
- [Font Awesome](https://fontawesome.com/) - Used for icons in information bar.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [PEP8 Online](http://pep8online.com/) - used to validate all the Python code
- [Jshint](https://jshint.com/) - used to validate javascript
- [Coolors](https://coolors.co/) - Used to create colour palette.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design
- [Grammerly](https://app.grammarly.com/) - used to proof read the README.md
- [Summernote](https://summernote.org/): A WYSIWYG editor to allow users to edit their posts
- [Techsini](https://techsini.com/multi-mockup/index.php) - Site mockup generator
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS Framework for developing responsiveness and styling
- [Hatchful](https://hatchful.shopify.com/): Used to generate custom logo
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to convert excel testing tables to markdown

## Credits

- [W3Schools](https://www.w3schools.com/)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Pexels](https://www.pexels.com/): All imagery on the site was sourced from Pexels.com
- [BBC Goodfood](https://www.bbcgoodfood.com/): All recipe content was sourced from BBC Goodfood.
- [Update View](https://pytutorial.com/django-updateview-example)
- [Pagination](https://docs.djangoproject.com/en/2.2/topics/pagination/#using-paginator-in-a-view)
- [AutoSlugField](https://django-extensions.readthedocs.io/en/latest/field_extensions.html)
- [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog)
- [Ian Meigh - Custom Validator function](eateasy/validators.py)

## Acknowledgments

Many thanks to my mentor Antonio for his support and advice. Thanks to
The Code Institute slack community for their quick responses and very helpful feedback in particular Ian Meigh.
