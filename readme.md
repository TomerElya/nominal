**Set up manual**
In order to run the project, first adjust your configuration (config.toml) to match the client's credentials and
environment settings.
Once the configuration is set up, all that is left to do is to simply 'python main.py'. This will run the Flask
application.
A requirements.txt is attached for required packages.

**Integration**
Once the application is running, the user is first required to authenticate through http://localhost:5000/auth.
This will require the user to log into his QuickBooks account, once that's done he'll be re-routed to the callback
route.
From this point on, the application takes care of tokenization, refreshment, sync between resources et cetera.

**Notes**

Most of them noted in the response email to the task's initial mail.
Configuration is implemented using configparser and toml. Obviously, the sensitive information saved
in the file, in a more organized infrastructure, could be injected to the pod environment
through a secret file or different approaches used to store sensitive data.
