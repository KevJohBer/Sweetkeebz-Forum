# SweetKeebz Forum

Sweetkeebz Forum is an online forum designed to let users communicate specifically about mechanical keyboards. It allows users on any device to ask questions or share news in the scene.

## Contents

* [User Experience](#user-experience-ux)
    * [User Stories](#user-stories)
* [Design](#design)
    * [Colour scheme](#colour-scheme)
    * [typography](#typography)
    * [imagery](#imagery)
* [Features](#features)
    * [Navbar](#navbar)
    * [Footer](#footer)
    * [Home Page](#home-page)
    * [About Page](#about-page)
    * [Create Post](#create-post)
    * [Profile page](#profile-page)
    * [Notifications](#notifications)
    * [Edit posts](#edit-posts)
    * [Edit comments](#edit-comments)
    * [Edit profile](#edit-profile)

* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
    * [Deployment](#deployment-instructions)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Media](#media)

---

## User Experience (UX)

Sweetkeebz Forum allows users to make posts related to mechanical keyboard building. Users can post content via text and are able to include images aswell. Users can also view and interact with posts made on the site by up/downvoting or commenting. Users can edit and delete their own posts and comments. Users can even personalize their own profiles and view other peoples profiles.

## User Stories

### User Goals

* Users should be able to enter the forum and view other users posts in order to get information.

* Users should be able to create an account nad log in.

* Users should be able to upvote, downvote and comment on posts.

* Users should be able to edit and delete posts and comments that they themselves create.

* Users should be able to personalize their profiles by updating their avatars, usernames and about sections.

### Admin Goals

* Admin should be able to manage posts by editing and deleting posts and comments made by any user. 

## Design

### colour scheme

Sweetkeebz uses a very minimal color pallette, white black and blue. The reason why this website does not use a lot of colors is because most of the content viewed on the page is made by users who might post images. Posting images will introduce a wide veriety of colors which can be distracting if it contradicts the websites main color scheme. Which is why the color scheme of this website is not very noticable. 

### Typography

Sweetkeebz uses A font called Lora for paragraphs and Open Sans for headers which is the default fonts used in the bootstrap template called "Clean Blog".

### Imagery

The header image was taken from google and is credited [here](#credits)

## Features

### Navbar

Sweetkeebz Forum has a navbar from which nearly all features can be accessed. The logo on the left takes you to the home page. On the right side is an array of links which turn into a dropdown box if the screen is smaller. The first link is to the about page which gives information about the website. The second labeled "create post" takes you to the post creation feature where you fill in the content you wish to post. The third is labelled "logout" ("login if you are already logged out") which allows you to logout or login. The fourth is labelled "Profile". This takes you to your own personal profile page. And finally we have an envelope icon which takes you to your notifications page where you can see who interacted with your post. The navbar also has a background with a stylish looking keyboard on it.

### Footer

The footer consists of three links to social media and use icons to make them look cleaner and recognizable.

### Home page

The homepage is one big ListView. Here Users posts are displayed in order of ther posted date.Each post includes who made the post. You can also click the user who posted in order to see their profile. Each post also has a title, some text (which is optional) and an image (also optional) so each post will look different depending on the information it is trying to convey. In any case you can press either the title, text, or image in order to see the full post. On the left of each post there is an upvote/downvote button with a upvote/downvote counter in the middle of the two buttons. At the bottom of each post there is a clickable comment icon with a comment counter next to it. Clicking this will open the full post where you can comment on the post. If the user is logged in, and a post belongs to the logged in user, a clickable three dot icon will appear at the top right of the post. When clicked it will display a dropdown box with the labels 'delete' and 'edit'. You can click the labels in order to edit or delete your own posts but you cannot do this to other users posts.

### Full Post

If you decide to click on a post It will take you to the posts own page. Here you will be met with the "full post" as the list view on the home page only displays a certain amount of information for aesthetic consistency. Here you can upvote and downvote like you can in the listview. You can also write a comment on the post from this view. You can also view other users comment on the same post. If a user is logged in and a comment was made by the logged in user, then the user will be able to edit and delete that comment. Other users are unable to do so. However the user who made the post can choose to delete comments on his/hers own post.

### About Page

Clicking the "about" label on the navbar will take you to the about page. The about page contains information about the website, its history and goals.

### Create Post

Clicking the "create post" label on the navbar will take you to a form. Here you have to choose a title for your post. Then you can choose to add some text to your post or add an image to your post. When picking an image, the image will be displayed so you can preview it to make sure it is the correct image being uploaded. Both text and image are optional. You are required to input a Title, the form will display an error message if the input is invalid. If the post is not related to keyboards or the post is inappropriate then it can be removed by an admin.

### Profile page

Clicking the "Profile" label on the navbar will take you to your own personal profile page. Here you can see your profile picture, your username and a small text that tells a little bit about yourself. By default the profile picture and about section are not set. You can set both by clicking your profile picture. This takes you to a form where you can edit your own profile. Below the profile information you can find a list of posts that were made by the user who owns the profile. 

### Notifications

Clicking the envelope on the navbar will take you to your own notifications page. Here you can see all notifications that you have recieved. The notifications alert you when someone has commented on your post. As soon as you click one of the notifications the notification will be marked as read. You can still view the notifications however. 

### Edit Posts

If a post belongs to you, you will be able to edit it by clicking the three dot icon on the top right of the post and then choosing edit from the dropdown. The edit page is the same as create post. Only that if you press edit, each field in the form will be filled with the content you originally posted. Still the form needs to be valid and appropriate. 

### Edit Profile

If you are viewing your own profile page and you press your own profile picture, you will be taken to a form in which you can edit your own username, about section, and profile image. You can even clear your profile image if you wish not to have one. 

### Edit Comments

If you are viewing a post and the post has a comment that is made by you, then the comment will also have a three dot icon on the top right. When clicked you can choose edit and it will take you to the original comment form but it will be filled with the same text as you originally posted. From here you can edit the text or add if you wish to do so.

## Technologies used

### Languages Used

* HTML
* CSS
* Python
* Javascript

### Frameworks, libraries & Programs Used

* Django Web Framework
* Bootstrap
* Font Awesome

## Deployment

### Deployment Instructions

Heroku was used to deploy the live website.

1. Login to Heroku
2. In the dashboard click your application
3. Click deploy
4. Connect your heroku app to github repository
5. Choose main branch as the branch to deploy to
6. Click Deploy Branch

## Testing

All testing can be found [here](TESTING.md)

## Credits

### Code Used

The post and comment models were inspired by the Code Institute Djangoblog tutorial

The code for automatically creating profiles for users was taken from this [article](https://dev.to/earthcomfy/django-user-profile-3hik)

The Notification model was taken from this stackoverflow [post](https://stackoverflow.com/questions/72264677/how-can-i-implement-notifications-system-in-django)

### Media

The navbar background image was taken from [here](https://wallhere.com/en/wallpaper/2096969)

bootstratp template used was [Clean Blog](https://startbootstrap.com/theme/clean-blog)