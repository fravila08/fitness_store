
# Fitness Store

The Fitness Store is a Django ran application to show some E-commerce capabilities.


## Tech Stack

**Client:** JavaScript, HTML, CSS, BootStrap

**Server:** Django, and PostgreSQL

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.nginx.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nginx/nginx-original.svg" alt="nginx" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Visit

Go to https://cpfitstore.com to see this project deployed.

## Noun API

#### Get Noun Information
Click here to view the documentation https://thenounproject.com/
```http
auth = OAuth1("your-api-key", "your-api-secret")
endpoint = f"http://api.thenounproject.com/icon/{item}"

response = requests.get(endpoint, auth=auth)
print(response.content)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
| `secret_key` | `string` | **Required**. Your Secret API key |
| `item`      | `string` | **Required**. name/number of item to fetch |




## Environment Variables

To run this project, you will need to add the following from the noun project into your 
environment variables to your .env file

`apikey`

`secretkey`


## Deployment

To deploy this project, first install requirements.txt then you need to create the data base with the following:

```bash
  createdb ecom_app
```
Now run the following:

```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py loaddata items.json
```
Finally:

```bash
  python3 manage.py runserver
```


## Thanks for Stopping By!

Thank you for checking out this project, feel free to follow me for more projects like this. Also,
if you happen to need help with any projects you are currently working on, please let me know where
I can help.

