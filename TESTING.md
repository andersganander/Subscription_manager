## Table of contents

<!-- TOC -->

- [Table of contents](#table-of-contents)
- [Manual Testing](#manual-testing)
    - [Epic: Account](#epic-account)
    - [Epic: Navigation](#epic-navigation)
    - [Epic: Subscriptions](#epic-subscriptions)
    - [Epic: Reminders](#epic-reminders)
    - [Epic: Services](#epic-services)
    - [Epic: Categories](#epic-categories)
- [Validator Testing](#validator-testing)
    - [HTML](#html)
        - [Fixed Errors](#fixed-errors)
    - [CSS](#css)
    - [Javascript](#javascript)
    - [Python](#python)
    - [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Bugs](#bugs)
    - [Fixed Bugs](#fixed-bugs)
        - [- #### Bug 1](#---bug-1)
    - [Unfixed bugs:](#unfixed-bugs)

<!-- /TOC -->

## Manual Testing

All user stories have been manually tested upon implementation, and this has been documented in each user story by the fulfilled acceptance criteria for each user story. In connection with the deployment to Heroku, which occurred in each sprint, testing was also conducted there. In addition to these continuous tests, manual tests were conducted at the end of sprint 5. The results of these tests are presented below.

### Epic: Account

![Manual Testing - Account](docs/readme_images/testing/MT_1.jpg)
![Manual Testing - Account](docs/readme_images/testing/MT_2.jpg)

### Epic: Navigation

![Manual Testing - Navigation](docs/readme_images/testing/MT_3.png)

### Epic: Subscriptions

![Manual Testing - Subscriptions](docs/readme_images/testing/MT_Sub_1.png)
![Manual Testing - Subscriptions](docs/readme_images/testing/MT_Sub_2.png)
![Manual Testing - Subscriptions](docs/readme_images/testing/MT_Sub_3.png)
![Manual Testing - Subscriptions](docs/readme_images/testing/MT_Sub_4.png)
![Manual Testing - Subscriptions](docs/readme_images/testing/MT_Sub_5.png)
![Manual Testing - Subscriptions](docs/readme_images/testing/MT_Sub_6.png)

### Epic: Reminders

![Manual Testing - Reminders](docs/readme_images/testing/MT_Rem_1.png)
![Manual Testing - Reminders](docs/readme_images/testing/MT_Rem_2.png)
![Manual Testing - Reminders](docs/readme_images/testing/MT_Rem_3.png)
![Manual Testing - Reminders](docs/readme_images/testing/MT_Rem_4.png)

### Epic: Services

![Manual Testing - Services](docs/readme_images/testing/MT_Ser_1.png)

### Epic: Categories

![Manual Testing - Categorys](docs/readme_images/testing/MT_Cat_1.png)

## Validator Testing

### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). For the pages that can be accessed without login, the "Validate by URI" was used. For the pages that does require log in the page source was used as input to the validator, using "Validate by Direct Input".

| Page                   | Logged Out | Logged In |
|------------------------|------------|-----------|
| about.html             |            |           |
| add_subscribtion.html  | N/A        | NO ERRORS |
| edit_subscription.html | N/A        | ERROR 1 |
| subscription_list.html | N/A        | NO ERRORS |
| subscription_summary   | N/A        | NO ERRORS |
| login.html             | NO ERRORS  | N/A       |
| logout.html            | N/A        | NO ERRORS |
| signup.html            | ERROR 2    | N/A       |
| 400.html               | No errors  | No errors |
| 500.html               | N/A        | No errors |


#### Fixed Errors
**ERROR 1**
![HTML Validation](docs/readme_images/testing/Val_1.png)
Fixed by removing the action attribute.

#### Unfixed Errors
The errors below relate to the validation of signup.html, which belongs to the all-auth library. I have troubleshooted the issue to see if it is related to the changes I have made, but since the error occurs when the code for the form is generated, I cannot see that it has to do with my code. I have also investigated the error by removing all my own code, but the error persists.

![HTML Validation](docs/readme_images/testing/Val_2.png)


### CSS

The stylesheet style.css was validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) without any errors found.


### Javascript
The Javascript files was validated with [Jshint](https://jshint.com/) with the following results:

| Script   | Result      | Comments       |
|----------|-------------|----------------|
| add.js   | 1 warning   | Warning 1      |
| base.js  | no warnings | Note 1         |
| edit.js  | no warnings | Note 1, Note 2 |
| list.js  | no warnings | Note 1, Note 2 |


**Warning 1:** The array literal notation [] is preferable. Fixed ([#80](https://github.com/andersganander/Subscription_manager/issues/80)).<br>
**Note 1:** Comments about the way Materialize components are initialized, f ex:
<code>M.updateTextFields();</code><br>
As it was mentioned, but not as a warning I just let it be. It's also the way that Materialize components are initialized in the documentation.<br>
**Note 2:** One unused variabled reported. Fixed.

<details>

<summary>Jshint</summary>

![Jshint](docs/readme_images/jshint_validation.png)
</details>

### Python
All Python files were run through [Pep8](http://pep8online.com/) with no errors found. 

### Lighthouse

Lighthouse validation was run on all pages (both mobile and desktop) in order to check accessibility and performance. At first I received the warning *'Background and foreground colors do not have a sufficient contrast ratio'* in relation to buttons where I had used the Bootstrap class `btn-info`. After I updated the button styling I received the below scores. 

| Page           | Performance  | Accessibility | Best Practices  | SEO |
|----------------|:------------:|:-------------:|:---------------:|:---:|
|                |              |               |                 |     |
| Desktop        |              |               |                 |     |
| Home           |          100 |           100 |             100 | 100 |


## Browser Testing
- The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.
    
## Device Testing
- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone SE,  and iPad to ensure responsiveness on various screen sizes in both portrait and landscape mode. The website performed as intended. The responsive design was also checked using Chrome developer tools across multiple devices with structural integrity holding for the various sizes.


## Bugs 

### Fixed Bugs

- #### Bug 1
     - **Bug**: When
     - **Fix**: in 


### Unfixed bugs:
 