import os

users = []
data = '<td align="center"><a href="https://github.com/{username}"><img src="https://github.com/{username}.png" width="100px;" alt=""/><br /><sub><b>{name}</b></sub></a></td>\n'
for filename in os.listdir("members"):
    with open(os.path.join("members", filename), 'r') as f:
       text = f.readlines()
       users.append({"name":text[1][7:-1],"username":text[2][11:-1]})


with open("Members.md","w") as f: 
    f.write("<table>\n")
    for i in range(len(users)):
        if(i%10 == 0):
            f.write("<tr>\n")
        f.write(data.format(name=users[i]["name"],username=users[i]["username"]))
        if((i+1)%10 == 0):
            f.write("</tr>\n")
    f.write("</table>")

            
