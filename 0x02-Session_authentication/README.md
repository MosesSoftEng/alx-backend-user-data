# :computer: Tasks.
## [0. Et moi et moi et moi!](api/v1/app.py)
### :page_with_curl: Task requirements.
Score: 0.0% (Checks completed: 0.0%)

Copy all your work of the **0x06. Basic authentication** project in this new folder.

In this version, you implemented a **Basic authentication** for giving you access to all User endpoints:

* `GET /api/v1/users`
* `POST /api/v1/users`
* `GET /api/v1/users/<user_id>`
* `PUT /api/v1/users/<user_id>`
* `DELETE /api/v1/users/<user_id>`

Now, you will add a new endpoint: `GET /users/me` to retrieve the authenticated `User` object.

* Copy folders `models` and `api` from the previous project `0x06. Basic authentication`
* Please make sure all mandatory tasks of this previous project are done at 100% because this project (and the rest of this track) will be based on it.
* Update `@app.before_request` in `api/v1/app.py`:
    * Assign the result of `auth.current_user(request)` to `request.current_user`
* Update method for the route `GET /api/v1/users/<user_id>` in `api/v1/views/users.py`:
    * If `<user_id>` is equal to `me` and `request.current_user` is `None`: `abort(404)`
    * If `<user_id>` is equal to `me` and `request.current_user` is not `None`: return the authenticated `User` in a JSON response (like a normal case of `GET /api/v1/users/<user_id>` where `<user_id>` is a valid `User` ID)
    * Otherwise, keep the same behavior

In the first terminal:
```
    bob@dylan:~$ cat main_0.py
    #!/usr/bin/env python3
    """ Main 0
    """
    import base64
    from api.v1.auth.basic_auth import BasicAuth
    from models.user import User
    
    """ Create a user test """
    user_email = "bob@hbtn.io"
    user_clear_pwd = "H0lbertonSchool98!"
    
    user = User()
    user.email = user_email
    user.password = user_clear_pwd
    print("New user: {}".format(user.id))
    user.save()
    
    basic_clear = "{}:{}".format(user_email, user_clear_pwd)
    print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))
    
    bob@dylan:~$
    bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py 
    New user: 9375973a-68c7-46aa-b135-29f79e837495
    Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
    bob@dylan:~$
    bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
     * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    ....
```    

In a second terminal:
```
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
    {
      "status": "OK"
    }
    bob@dylan:~$
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
    {
      "error": "Unauthorized"
    }
    bob@dylan:~$ 
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
    [
      {
        "created_at": "2017-09-25 01:55:17", 
        "email": "bob@hbtn.io", 
        "first_name": null, 
        "id": "9375973a-68c7-46aa-b135-29f79e837495", 
        "last_name": null, 
        "updated_at": "2017-09-25 01:55:17"
      }
    ]
    bob@dylan:~$
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
    {
      "created_at": "2017-09-25 01:55:17", 
      "email": "bob@hbtn.io", 
      "first_name": null, 
      "id": "9375973a-68c7-46aa-b135-29f79e837495", 
      "last_name": null, 
      "updated_at": "2017-09-25 01:55:17"
    }
    bob@dylan:~$
```

### :wrench: Task setup.
```bash
```

### :heavy_check_mark: Solution
> [:point_right: api/v1/app.py](api/v1/app.py), [:point_right: api/v1/views/users.py](api/v1/views/users.py)
