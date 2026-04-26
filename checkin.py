import requests

check_in_url = "https://railgun.info/api/user/checkin"

# koa:sess=eyJ1c2VySWQiOjM4OTY2LCJfZXhwaXJlIjoxODAzMTI3MjA2OTI1LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=xOe2inD4Jf_rjPVOMXbOd0S3Tl4

cookies = {
    "koa:sess": "eyJ1c2VySWQiOjM4OTY2LCJfZXhwaXJlIjoxODAzMTI3MjA2OTI1LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=",
    "koa:sess.sig": "xOe2inD4Jf_rjPVOMXbOd0S3Tl4"
}

headers = {
    "user-agent": "Mozilla/5.0",
    "referer": "https://railgun.info/console/checkin",
    "origin": "https://railgun.info"
}

res = requests.post(
    check_in_url,
    headers=headers,
    cookies=cookies,
    json={}
)

print(res.status_code)
print(res.text)
