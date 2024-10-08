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
    - [Unfixed bugs:](#unfixed-bugs)
    - [Fixed after assessment result](#fixed-after-assessment-result)

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
| ------------------------ | ------------ | ----------- |
| about.html             |            |           |
| add_subscribtion.html  | N/A        | NO ERRORS |
| edit_subscription.html | N/A        | ERROR 1   |
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

**ERROR 2**

![HTML Validation](docs/readme_images/testing/Val_2.png)
This error was harder to find a solution for. After a while i realised that the problem was related to the ul inside the span, which is not allowed. This was resolved by changing <code>form.as_p</code> to <code>form.as_div</code> .

### CSS

The stylesheet style.css was validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) without any errors found.

### Javascript

The Javascript files was validated with [Jshint](https://jshint.com/) with the following results:


| Script  | Result      | Comments       |
| --------- | ------------- | ---------------- |
| add.js  | 1 warning   | Warning 1      |
| base.js | no warnings | Note 1         |
| edit.js | no warnings | Note 1, Note 2 |
| list.js | no warnings | Note 1, Note 2 |

**Warning 1:** The array literal notation [] is preferable. Fixed ([#80](https://github.com/andersganander/Subscription_manager/issues/80)).<br>
**Note 1:** Comments about the way Materialize components are initialized, f ex:
<code>M.updateTextFields();</code><br>
As it was mentioned, but not as a warning I just let it be. It's also the way that Materialize components are initialized in the documentation.<br>
**Note 2:** One unused variabled reported. Fixed.

### Python

All Python files were run through the [CI Python Linter](https://pep8ci.herokuapp.com/) and all errors were corrected.

### Lighthouse

The pages of the web site were tested using Lighthouse to check performance and accessibility.

<details>
<summary>Mobile</summary>

**Log in**
![Lighthouse validation](docs/readme_images/testing/LH_M_1.png)
<br>

**Sign up**
![Lighthouse validation](docs/readme_images/testing/LH_M_2.png)
<br>

**Subscription List**
![Lighthouse validation](docs/readme_images/testing/LH_M_4.png)
<br>

**Add subscription**
![Lighthouse validation](docs/readme_images/testing/LH_M_5.png)
<br>

**Edit subscription**
![Lighthouse validation](docs/readme_images/testing/LH_M_6.png)
<br>

**Delete subscription**
Not validated. It seems like the modal used in delete subscription is not "compatible" with Lighthouse validation. When trying to validate the delete page the modal disappears and it looks like the subscription list (which is the page that is shown after deletion) is validated instead
<br>

**Subscription summary**
![Lighthouse validation](docs/readme_images/testing/LH_M_7.png)
<br>

**Log out**
![Lighthouse validation](docs/readme_images/testing/LH_M_8.png)
<br>

</details>

<details>
<summary>Desktop</summary>

**Log in**
![Lighthouse validation](docs/readme_images/testing/LH_DT_1.png)
<br>

**Sign up**
![Lighthouse validation](docs/readme_images/testing/LH_DT_2.png)
<br>

**Subscription List**
![Lighthouse validation](docs/readme_images/testing/LH_DT_4.png)
<br>

**Add subscription**
![Lighthouse validation](docs/readme_images/testing/LH_DT_5.png)
<br>

**Edit subscription**
![Lighthouse validation](docs/readme_images/testing/LH_DT_6.png)
<br>

**Delete subscription**
Not validated. It seems like the modal used in delete subscription is not "compatible" with Lighthouse validation. When trying to validate the delete page the modal disappears and it looks like the subscription list (which is the page that is shown after deletion) is validated instead
<br>

**Subscription summary**
![Lighthouse validation](docs/readme_images/testing/LH_DT_7.png)
<br>

**Log out**
![Lighthouse validation](docs/readme_images/testing/LH_DT_8.png)
<br>

</details>

## Browser Testing

- The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.

## Device Testing

- The website was viewed on different devices such as Desktop, Laptop, iPhone SE,  and iPad to ensure responsiveness. The responsive design was also checked using Chrome developer tools.

## Bugs

### Fixed Bugs

![Fixed bugs](docs/readme_images/testing/Fixed_bugs.png)

### Unfixed bugs:

The following bugs are still on the backlog.

![Unfixed bugs](docs/readme_images/testing/Unfixed_bugs.png)

**Fix Check box is not shown in edit subscription form #47**

The initial idea was to use materialize's switch component in the edit subscription form. Due to an incompability between materialize and Django that was not as easy to implement as expected. There seem to be some inconsistence in the way Django renders it's checkbox widget and the html that materialize expects. The following discussion on StackOverflow describes the problem.
https://stackoverflow.com/questions/54500348/django-checkbox-not-showing-up-in-html
The proposed solution is to overwrite the default checkbox widget.

To be able to change the value for active, a workaround has been implemented. Instead of using the checkboxinput widget, the select widget has been used:
'active': forms.Select(attrs={'class': 'browser-default'}, choices=[[True,'Yes'],[False,'No']]),

### Fixed after assessment result

The following bug was detected during assessment and fixed before resubmission of the project.

[Issue #92](https://github.com/andersganander/Subscription_manager/issues/92)