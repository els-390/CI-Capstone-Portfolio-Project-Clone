# Capstone Portfolio Project

<img src=static/images/readme/responsive_mockup.png alt="A screenshot showing the project on multiple devices" width="600" height="300">

<br>

The deployed site can be found [here](https://ci-full-stack-portfolio-app-7c4baf7a6f9d.herokuapp.com/).

## Purpose 

This project aims to produce a portfolio web application for future potential employers to showcase multiple projects in one place. 

The application will showcase example projects, key skills and technologies used in specific projects, as well as to provide information about myself and my experience and how to contact me about potential collaboration or employment opportunities.

The target audience is potential future employers, clients other web developers looking for inspiration or collaboration. 

The design is simple and responsive with a few contrasting colours selected to highlight key functionality for ease of use. The overall site layout is designed to enhance the users experience of the site and support navigation across devices. 

Future iterations may also include a functioning blog, further sections to showcase skills more visually

## Planning 

<img src=static/images/readme/planning/capstone_miro_board.jpg image alt="Screenshot of project Miro board" width="600" height="300">

<br>

Initially the project was planned out using a Miro board to start to brainstorm some ideas, concepts and content. 

[View Miro board](https://miro.com/app/board/uXjVLA4YJ9I=/?share_link_id=560098034555)

## User Stories

<img src=static/images/readme/userstories/capstone_issues.png alt="Screenshot of issues in GitHub with user stories" width="600" height="300">

<br>



## Agile Methodolgies & Project Board 

<img src=static/images/readme/agile/capstone_project_board.png alt="Screenshot of GitHub project board" width="600" height="300">

The completed sprint was composed of 17 separate items. Having used the MoSCoW approach to prioritisation, 9 were classified as "Must-Have" making up less than 60% of the tasks as recommended. The rest of the first sprint was made up of "Should-Have" and "Could-Have" items.

There were no remaining backlog items.

## Flowchart & ERD

<img src=static/images/readme/planning/flowchart.png image alt="Flowchart for the application functions and features" width="600" height="">

<br>

<img src=static/images/readme/erd/ERD.png image alt="ERD diagram" width="600" height="300">

## Design Decisions & UX

Many different wireframes were produced to help plan the project including for desktop, tablet and mobile devices. 

Initially the project was planned to have multiple sections to the homepage but this was scaled back for the first iteration due to time constraints so further sections will be added in future to make the homepage more informative and link to other areas of the applications. 

### Desktop
<img src=static/images/readme/wireframes/desktop_homepage_wireframes.png image alt="desktop wireframe for homepage" width="600" height="300">

<br>

<img src=static/images/readme/wireframes/desktop_project_detail_1_wireframes.png image alt="desktop wireframe for project detail page showing project info" width="600" height="300">

<br>

<img src=static/images/readme/wireframes/desktop_project_detail_2_wireframes.png image alt="desktop wireframe for project detail page showing comments" width="600" height="300">

<br>

<img src=static/images/readme/wireframes/desktop_about_wireframes.png image alt="desktop wireframe for about page" width="600" height="300">

<br>

<img src=static/images/readme/wireframes/desktop_contact_wireframes.png image alt="desktop wireframe for contact page" width="600" height="300">

<br>

### Tablet
<img src=static/images/readme/wireframes/tablet_wireframes_1.png image alt="tablet wireframes for all pages" width="600" height="300">

<br> 

<img src=static/images/readme/wireframes/tablet_wireframes_2.png image alt="tablet wireframes for all pages" width="600" height="300">

<br>

### Mobile
<img src=static/images/readme/wireframes/mobile_wireframes_1.png image alt="mobile wireframes for all pages" width="600" height="300">

<br>

<img src=static/images/readme/wireframes/mobile_wireframes_2.png image alt="mobile wireframes for all pages" width="600" height="300">

<br>

#### Wireframes for future iterations

<img src=static/images/readme/wireframes/future_homepage_section_wireframes_1.png image alt="mobile wireframes for all pages" width="600">

<br>

<img src=static/images/readme/wireframes/future_homepage_section_wireframes_2.png image alt="mobile wireframes for all pages" width="600">

### Typography

<img src=static/images/readme/design/fonts.png image alt="Alt text" width="600">

<br>

Font decisions were sourced from [Google Fonts](www.googlefonts.com) chosing 2-3 simple fonts and the fallback font of sans-serif for any browsers where they may not be supported. 

- Bungee Shade was used for the nav bar logo and the project detail headings

- The main site text was Roboto

- Merriweather was used for some messages depending on user behaviour to indicate CRUD functionality.

 ### Colours and Images 

<img src=static/images/readme/design/colour_pallette.png image alt="Alt text" width="600">

<br>

The colours for the website were simple using a variation of white and #F7F2F2 to style the cards and navigation. 

The main font colours were  #3D2A48 a dark purple colour and a red #C7384A used for highlighting certain text,  buttons and accents. Some additional colours were also used for buttons to indicate their different functionality to make it easy to distinguish between editting and deleting and buttons for GitHub and the deployed site within projects.

### Images & Icons 

- Placeholder image provided by Code Institute from Django Blog walkthrough for About page. 

- Placeholder project image sourced from [Unsplash](https://unsplash.com/photos/lines-of-html-codes-4hbJ-eymZ1o)

- Favicon created with [Favicon.io](https://favicon.io/favicon-converter/)

- About image captured Tom Carpenter. 

- Other images are site owners own.

### Accessibility

<img src=static/images/readme/responsive_mockup.png alt="A screenshot showing the project on multiple devices" width="600" height="300">

<br>

The application has been designed to be responsive across all major device formats and browser, shrinking and adjusting as devices change or are rotated. 

The naviation collapses to a burger menu toggler icon on smaller devices and the number of projects viewable on the homepage reduce with the size of the aspect ratio.

### Accessibility Considerations

- Choosing accessible fonts
- Not having too many colours that clash
= Simple design and layout
- Adding ALT tags
- Ensuring links open in new tabs when clicked

## Features

- Navigation with Text logo and simple menu options, highlighting which page is the active page and hover state to show which buttons are selected while being fully responsive on different devices. 

- Multiple project post pagination showing 6 projects on the main page and a further 2. Pagination is flexible acorss devices shrinking to 2 and 1 columns on smaller screens.

- Each project post features information about the purpose of the project and the tools, skills and technologies used to complete the project.

- Links to GitHub Repositories and Deployed sites for each project. 

- Full CRUD functionality for making comments on project posts and creating, reading, updating and deleting reviews to the website including the ability to add a rating for reviews.

- User authentication for CRUD functionality with sign up and login functionality to ensure security and facilitiate comment and review approvals. 

- About page with bio about the site owner and further down a contact form to submit a contact request. 

- Seperate contact page with the same contact form repurposed. 

- Footer with professional and social media links

<br>

**Home Page**

The Home page of the site shows a selection of projects available to select to view more information or navigate to the next page to see more projects.

**Project Details Page**

The project details page for each project loads when each project is clicked or navigated to to show a summary of each project, sample image, list of technologies used, link to the repository and a link to the deployed site. From here site visitors navigate to the previous or next project or they can leave, edit and delete comments.

**About Page**

The About page gives details about the site owner including a photo and provides a contact form to submit a request to contact them.

**Reviews Page**

The reviews page provides an opportunity for people to leave a review about the site owner and the projects and displayed completed and approved reviews.

**Navigation Bar**

The navigation bar is fully responsive and provides links for the Home, About, Reviews and Contact page.

**The Footer**

The Footer has links to the various relevant professional and social media pages for the site owner.

**Reigster**

The site has a facility to sign up as a user in order this enables them to create, edit or delete their own reviews or comments on project posts.

**Sign In**

The site has a facility to sign in, once a user creates an account, this enables them to create, edit or delete their own reviews or comments on project posts.

**Sign Out**

The site has a facility for a user to sign out of their account.

**Admin**

The site has a facility for designated administrators to sign in, in order to administrate the site via the standard Django admin interface.

## Testing and Validation

### Manual Testing
The site was tested on the following browsers for compatibility:

### Chrome ###
|   Test	|  Expected Result 	|  Actual Result	|
|---	|---	|---	|
|   Click Home menu	|  Success 	|  Success 	|
|   Click About menu	|  Success 	|  Success 	|
|   Click Reviews menu	|  Success 	|  Success 	|
|   Click Login menu	|  Success 	|  Success 	|
|   Click Logout	|  Success 	|  Success 	|
|   Click individual project post	|  Success 	|  Success 	|
|   Create, edit, delete a personal comment	|  Success 	|  Success 	|
|   Register new account	|  Success 	|  Success 	|
|   Create contact request	|  Success 	|  Success 	|
|   Access admin interface	|  Success 	|  Success 	|
|   Responsivity	|  Success 	|  Success 	|
|   Open new page from social media links	|  Success 	|  Success 	|

### Safari ###
|   Test	|  Expected Result 	|  Actual Result	|
|---	|---	|---	|
|   Click Home menu	|  Success 	|  Success 	|
|   Click About menu	|  Success 	|  Success 	|
|   Click Reviews menu	|  Success 	|  Success 	|
|   Click Login menu	|  Success 	|  Success 	|
|   Click Logout	|  Success 	|  Success 	|
|   Click individual project post	|  Success 	|  Success 	|
|   Create, edit, delete a personal comment	|  Success 	|  Success 	|
|   Register new account	|  Success 	|  Success 	|
|   Create contact request	| Success	|  Success 	|
|   Access admin interface	|  Success 	|  Success 	|
|   Responsivity	|  Success 	|  Success 	|
|   Open new page from social media links	|  Success 	|  Success 	|

### Lighthouse
The site was tested using Lighthouse acheiving the following results: 

<img src=static/images/readme/testing/lighthouse_1.png alt="A screenshot showing the results of Lighthouse testing" width="600">

### Responsive Testing

Alongside other tests, Chrome dev tools were used frequently to test the site was responsive on standard desktop screens, and when viewed on smaller devices such as tablets and phones.

### Validator Testing

- HTML

  - No errors were returned when passing through the official W3C validator
<img src="assets/images/CSSvalidator.png" alt="css validation screenshot">


- CSS
  - No errors were found with our own CSS code when passing through the official Jigsaw validator.
<img src="assets/images/CSSvalidator.png" alt="css validation screenshot">

- Python

  - All Python code was tested for PEP8 compatibility with the Code Institute Linter.

  **The only code that didn't pass was code that was automatically generated by Django**
  
  which was then edited in order to pass.

<img src="assets/images/CSSvalidator.png" alt="css validation screenshot">

  - Javascript

  - All Javascript code was tested for errors with JSHint. There were no code errors and one error related to imported code, which is outside the domain of the test.
  
<img src="assets/images/CSSvalidator.png" alt="css validation screenshot">


## Bugs

<img src="assets/images/CSSvalidator.png" alt="css validation screenshot">

## AI

<img src=static/images/readme/ai/chatgpt.png alt="Screenshot from use of ChatGPT">

<br>

- Utilised ChatGPT to troubleshoot errors
- Supported with the creation of the views for the Reviews app to enable functionality to create, read, update, delete reviews and add a number rating.
 - ChatGPT suggested ways to fix some formatting issues with CSS. 
- Also used to provide content for project posts based on some provided promps and links to the relevant deployed sites and repositories.

## Deployment

The site was deployed to Heroku from the main branch of the repository early in the development stage for continuous deployment and checking.

The Heroku app is setup with 3 environment variables, repalcing the environment variables stored in env.py (which doesn't get pushed to github).

In order to create an Heroku app:

1. Click on New in the Heroku dashboard, and Create new app from the menu dropdown.

2. Give your new app a unique name, and choose a region, preferably one that is geographically closest to you.

3. Click "Create app"

4. In your app settings, click on "Reveal Config Vars" and add the environment variables for your app. These are:
- DATABASE_URL - your database connection string
- SECRET_Key - the secret key for your app
- CLOUDINARY_URL - the cloudinary url for your image store

The PostgreSQL database is served from NeonDB provided by Code Institute.

Once the app setup is complete, click on the Deploy tab then follow these steps:

1. Connect to the required GitHub account
2. Select the relevant repository to deploy from
3. Click the Deploy Branch button to start the  deployment.
4. Once deployment finishes the app can be launched.

The  deployed site can be found [here](https://ci-full-stack-portfolio-app-7c4baf7a6f9d.herokuapp.com/).

## Reflection on Development Process

### Successes

- Effective use of AI tools to help with development process to improve understanding of some features contributed to the development process

- Produced a completed project within the alloted time

- Implemented a custom model for the Reviews app with CRUD functionality

- Fully responsive accessible design


### Challenges

- Some challenges modifying existing models
- Difficulty getting approvals to functional correctly when submitting new comments and reviews, editting these and resubmiting for re-approval
- Challenges updating CSS template in some cases where multiple classes were used

### Final Thoughts

Provide any additional insights gained during the project and thoughts on the overall process.  

**Guidance:** Begin drafting reflections during Phase 1 and update throughout the project. Finalize this section after Phase 4. Highlight successes and challenges, particularly regarding the use of AI tools, and provide overall insights into the project.

### Future Improvements & Iterations

- Add a seperate blog

- Create a seperate homepage that has sections for an introduction, skills, experience, projects, reviews and blog

- Improve the layout of the About, Contact and Reviews pages so that the content fits either above or below the fold, not on the line for accessibility and design


## Credits
- This project is based on the "I Think Therefore I Blog" project from the Code Institute LMS
- Help received to troubleshoot varuious issues during the project from Coding Coach team at Code Institute and Headforwards Bootcamp cohort 
