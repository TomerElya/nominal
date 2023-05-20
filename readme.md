**Intro**

In order to run the project, you must first authenticate yourself through /auth route.
Once authenticated, your session credentials are saved over the HTTP session and used to interact with QuickBooks API.

**Notes**

Most of them noted in the response email to the task's initial mail.
Configuration is implemented using configparser and toml. Obviously, the sensitive information saved
in the file, in a more organized infrastructure, could be injected to the pod environment
through a secret file or different approaches used to store sensitive data.
