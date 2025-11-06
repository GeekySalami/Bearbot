# Bearbot

A Django-based multi-module web application that integrates user authentication, blog functionality, a learning hub, media uploads, and modular resource management.

---

## Table of Contents
- [About](#about)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
  - [Running the Development Server](#running-the-development-server)
- [Usage](#usage)
- [Environment Configuration](#environment-configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About
Bearbot is a Django hub project consisting of multiple Django apps that together form a flexible, extendable web system. It includes user management, blogs, learning modules, resource viewers, and video content sections. The project is structured for easy expansion and experimentation.

---

## Features
- User authentication and profiles
- Blog module for creating and viewing posts
- Dashboard module for central management interfaces
- Learning modules (e.g., video-based content)
- Resource viewer for displaying and managing files
- Profile picture and media uploads
- Modular Django app structure for easy expansion

---

## Architecture
The project structure includes:

```
Bearbot/
  blog/
  dashboard/
  learn/
  media/profile_pics/
  resource_viewer/
  text_editor/
  users/
  ytvids/
  db.sqlite3
  manage.py
```

### Notable Apps
- **blog/** – User blog system
- **dashboard/** – Admin/overview tools
- **learn/** – Course or lesson modules
- **resource_viewer/** – View and manage uploaded resources
- **text_editor/** – Internal text-editing tool
- **users/** – Authentication, profile images, profile management
- **ytvids/** – Video content section (YouTube or local media)

---

## Getting Started

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)
- Git

### Installation
```bash
git clone https://github.com/GeekySalami/Bearbot.git
cd Bearbot
```

Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
# or
venv\Scripts\activate         # Windows
```

Install requirements:
```bash
pip install -r requirements.txt
```

### Database Setup
Apply migrations:
```bash
python manage.py migrate
```

Create a superuser:
```bash
python manage.py createsuperuser
```

### Running the Development Server
```bash
python manage.py runserver
```
Visit:
```
http://127.0.0.1:8000/
```

---

## Usage
- Register/login from the user module
- Upload profile pictures (stored in `media/profile_pics/`)
- Create and manage blog posts from the blog section
- Access learning modules and view video content
- Use the resource viewer to upload or view files
- Navigate the dashboard for centralized tools (if configured)

---

## Environment Configuration
You may configure the following in `settings.py` or a `.env` file:
- `DEBUG`
- `ALLOWED_HOSTS`
- Database settings
- `MEDIA_URL` / `MEDIA_ROOT`
- Secret key handling for production

---

## Contributing
Contributions are welcome:
1. Fork the repository
2. Create a feature branch
3. Make changes and test
4. Submit a pull request with a clear description

---

## License
Specify a license here (e.g., MIT, Apache 2.0) if the project uses one.

---

## Contact
Author: **GeekySalami**  
GitHub: https://github.com/GeekySalami
