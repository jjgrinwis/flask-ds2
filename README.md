little Flask application with Basic-Auth to check your Akamai Datastream configuration.

We added a little workaround to get some extra debugging when using gunicorn.
So you can now stream your logs to your endpoint and logs should be showing up in the console.

flask-ds-2] [2021-10-26 14:47:44] [2021-10-26 14:47:44 +0000] [16] [INFO] JSON: {'test': 'Hello JSON world'}
[flask-ds-2] [2021-10-26 14:47:44] 10.244.6.71 - john [26/Oct/2021:14:47:44 +0000] "POST /log HTTP/1.1" 204 0 "-" "PostmanRuntime/7.28.4"