# Creating Server-side session Authentication using Flask and Redis

The regular JWT token auth method is great but can some times pose a security threat when token stored in client side are maliciously accessed through things like cross-site forgery or other means. 

Server-side sessions are another great way of authentication where logged in use utilize an authenticated open session and all that is store on the client side are just session Ids (by cookies) used to identify active users. 

Flask_sessions server session sets a session cookie that can be used to retrieve logged in authorized user

## Needed packages 
- flask-session
- redis