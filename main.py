from github import Github
import slackweb
import time
import sys, getopt
import configargparse

p = configargparse.ArgParser(default_config_files=['config.ini'])

p.add('-u', '--hook-url', required=True, env_var='HOOK_URL', help="Slack hook url")
p.add('-t', '--token', help="Github token", required=True, env_var='TOKEN')

options = p.parse_args()

slack = slackweb.Slack(url=options.hook_url)

f = open("credentials")
token = f.readline().strip()
f.close()
g = Github(login_or_token=token)

saved_notifs = []

user = g.get_user()

while True:
    notifs = g.get_user().get_notifications()
    list_notifs = [notif for notif in notifs]
    if list_notifs == []:
        saved_notifs = []
    else:
        for notif in user.get_notifications():
            if notif.id not in saved_notifs:
                url = notif.subject.url \
                    .replace("/api.github.com", "/github.com") \
                    .replace("/repos/", "/") \
                    .replace("/pulls/", "/pull/")
                attachment = [{
                    "title": notif.repository.name + " - " + notif.subject.title,
                    "pretext": "New github notification",
                    "title_link": url,
                    "color": "#000000",
                    "fallback": "Comment on : " + notif.subject.title + " - " + notif.repository.name
                }]
                slack.notify(
                             attachments=attachment,
                             username="Github bot",
                             icon_url="https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png")
                saved_notifs.append(notif.id)

    time.sleep(5)
