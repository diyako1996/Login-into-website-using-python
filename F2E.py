#Written By Abi

import requests
from lxml import html
import sys

def get_login(url,form_data):
    s=requests.Session()
    form={}
    login=s.get(url)
    login_html = html.fromstring(login.text)
    hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
    form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
    form[form_data["user_nameField"]],form[form_data["pass_form"]]=form_data["username"],form_data["password"]
    res=s.post(url,data=form)
    print(res,'\n',res.status_code,res.content)
    return


def main():
    print(len(sys.argv))
    if(len(sys.argv)!=6):
        print("Usage: 1:pageUrl   2:username_field   3:password_field   4:passwordname_of_form   5:usename_of_form \n"
             +"Exaple: https://blabla.com admin password normal_username noral_password")
        return
    url=sys.argv[1]
    data={"user_nameField":sys.argv[5],"username":sys.argv[2],"pass_form":sys.argv[4],"password":sys.argv[3]}

    get_login(url,data)
    
if __name__ == '__main__':
    main()
