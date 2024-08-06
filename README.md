# Django games forum webapp "Gamecat"


## 🚀 Technologies

- **Framework**: Built with Django 4.x
  
- **Used Languages**: Python, HTML, CSS, JavaScript.
  
- **API**: Example external API page with room data (more features to come)
  
- **Version Control**: Managed with Git and GitHub for source code versioning.

## ✨ Features

- **Discussion Forum**: Allows users to create and comment on rooms about various topics.
  
- **User Profiles**: Each user has a profile showcasing their recent activity, bio, and avatar.
  
- **CRUD**: Basic operations on rooms, topics, and messages.
  
- **Search bar**: Search and filter games by topics or text
  
- **Content Moderation**: Tools for superusers to manage posts and users.

  <p align="center">
    <img src="github_files/main_page.gif" alt="main_page" />
    <br />
    <span>Main page view</span>
  </p>

## 🔒 Authorization

- **Login/Register**: Role-based access control for users and administrators.
  
- **Custom User Model**: Login via unique email instead of username, with support for avatars.
  
- **Editing User's Data**: Users can edit their data, avatar, and manage rooms and messages they created.

<p align="center">
    <img src="github_files/auth.gif" alt="auth.gif" />
    <br />
    <span>Example of access control</span>
</p>


## 🎨 UX/UI

- **Theme**: Consistent design with a few main colors and a gradient animated background.
  
- **Room Details**: Each room includes details about the host, creation time, and participants.
  
- **Messages**: All messages include timestamps and a delete option.
  
- **Dynamic Filtering**: Animated topic browser, with topics ordered by participant count.

<p align="center">
    <img src="github_files/dynamic_topic.gif" alt="dynamic_topic.gif" />
    <br />
    <span>Filtering by topics</span>
</p>


## ⚙️ API

- **Simple API Page**: External page to find rooms by ID and get JSON data.
  
- **Room Access**: JSON data displays each room linked to the original page.


<p align="center">
    <img src="github_files/api.gif" alt="api" />
    <br />
    <span>simple api</span>
</p>

## 🔜 To be done

- **Extend API**: Add more objects such as participants and messages.
  
- **Upvoting System**: Implement an upvoting system for messages and rooms.
  
- **Similar Rooms**: Introduce a feature to recommend rooms with similar topics or messages.
  
- **Message Search**: Add a search bar to filter messages by text.

- **Responding**: Implement a responding to messages system in rooms

- **Analytics**: Add simple statistics about number of written messages and displaying top users on home page
