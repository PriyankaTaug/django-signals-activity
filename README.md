# Django User activity tracking

A simple djang project to track user login actitvity and events suing **signals**

## Features

- Tracks  user login events when user login `user_logged_in` signal.
- Stores the logs in activity.log file


## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Django-UserActivity.git
   cd Django-UserActivity


2. Create user

   ```sh
   python manage.py createsuperuser

3. Run server

   ```sh 
   python manage.py runserver


## Step 1 

Create a **signals.py** file add  code mentioned in signals.py

## Step 2

In **settings.py** add logging setting

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'activity.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'activity_logger': {  # Custom logger for your app
            'handlers': ['file'],
            'level': 'INFO',  
            'propagate': False,
        },
    },
}
}

## Step 3

In app.py add 

    def ready(self):
        import activity.signals  # Ensure this is correctly importing signals

inside the  ActivityConfig class




