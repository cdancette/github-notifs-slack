This app sends incoming notifications from github to a slack hook.

# Installation :

- Create a slack incoming webhook : https://api.slack.com/incoming-webhooks

- Create a github personal token (it should have "notification" permission)

- Put those two parameters in the `config.ini` file (copied from `config.ini.dist`) OR create the 
`SLACK_HOOK` and `GITHUB_TOKEN` environment variables

- run the app

You can also run the app using the dockerfile, using the same environment variables to configure the app.

Feel free to add issues or PR

