# codabox-interview

Welcome to the codabox-interview

## requirements
* docker
* docker-compose
* python (2.7) (for the commandline app)

## running the app

Start the containers:

`docker-compose up`

Create a superuser:

`docker-compose run web ./manage.py createsuperuser`

Login by going to http://localhost/admin and add a few greets

see your greets: http://localhost/hello-world/ &lt;id&gt;

## Extra

Expose ID's on admin page so you don't have to find them on the shell



## caveats

I could not find a docker approach to get a hostname other than `localhost` for the hostname
of the container. A simple solution could be to add the following line to your `/etc/hosts`:

`127.0.0.1 codabox-interview.dev`

Another solution uses a tool called "dnsmasq" to do this in a slightly more dynamic way.
