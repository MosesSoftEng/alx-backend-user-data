# :book: 0x02. Session authentication.
## :page_with_curl: Topics Covered.
The project is about implementing a session authentication mechanism without installing any other module. The learning objectives of the project include;
1. Understanding authentication, session authentication.
2. Cookies, sending cookies, and parsing cookies.

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


## [1. Empty session](api/v1/app.py)
### :page_with_curl: Task requirements.
Score: 0.0% (Checks completed: 0.0%)

Create a class `SessionAuth` that inherits from `Auth`. For the moment this class will be empty. It’s the first step for creating a new authentication mechanism:

* validate if everything inherits correctly without any overloading
* validate the “switch” by using environment variables

Update `api/v1/app.py` for using `SessionAuth` instance for the variable `auth` depending of the value of the environment variable `AUTH_TYPE`, If `AUTH_TYPE` is equal to `session_auth`:

* import `SessionAuth` from `api.v1.auth.session_auth`
* create an instance of `SessionAuth` and assign it to the variable `auth`

Otherwise, keep the previous mechanism.

In the first terminal:
```
    bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth python3 -m api.v1.app
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
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status/"
    {
      "status": "OK"
    }
    bob@dylan:~$
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
    {
      "error": "Unauthorized"
    }
    bob@dylan:~$ 
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
    {
      "error": "Forbidden"
    }
    bob@dylan:~$
```

### :wrench: Task setup.
```bash
# Start server.
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app

# Tests.
curl "http://0.0.0.0:5000/api/v1/unauthorized"
```

### :heavy_check_mark: Solution
> [:point_right: api/v1/auth/session_auth.py](api/v1/auth/session_auth.py), [:point_right: api/v1/app.py](api/v1/app.py)

## [2. Create a session](api/v1/app.py)
### :page_with_curl: Task requirements.
Score: 0.0% (Checks completed: 0.0%)

Update `SessionAuth` class:

* Create a class attribute `user_id_by_session_id` initialized by an empty dictionary
* Create an instance method `def create_session(self, user_id: str = None) -> str:` that creates a Session ID for a `user_id`:
    * Return `None` if `user_id` is `None`
    * Return `None` if `user_id` is not a string
    * Otherwise:
        * Generate a Session ID using `uuid` module and `uuid4()` like `id` in `Base`
        * Use this Session ID as key of the dictionary `user_id_by_session_id` \- the value for this key must be `user_id`
        * Return the Session ID
    * The same `user_id` can have multiple Session ID - indeed, the `user_id` is the value in the dictionary `user_id_by_session_id`

Now you an “in-memory” Session ID storing. You will be able to retrieve an `User` id based on a Session ID.
```
    bob@dylan:~$ cat  main_1.py 
    #!/usr/bin/env python3
    """ Main 1
    """
    from api.v1.auth.session_auth import SessionAuth
    
    sa = SessionAuth()
    
    print("{}: {}".format(type(sa.user_id_by_session_id), sa.user_id_by_session_id))
    
    user_id = None
    session = sa.create_session(user_id)
    print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))
    
    user_id = 89
    session = sa.create_session(user_id)
    print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))
    
    user_id = "abcde"
    session = sa.create_session(user_id)
    print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))
    
    user_id = "fghij"
    session = sa.create_session(user_id)
    print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))
    
    user_id = "abcde"
    session = sa.create_session(user_id)
    print("{} => {}: {}".format(user_id, session, sa.user_id_by_session_id))
    
    bob@dylan:~$
    bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_1.py 
    <class 'dict'>: {}
    None => None: {}
    89 => None: {}
    abcde => 61997a1b-3f8a-4b0f-87f6-19d5cafee63f: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde'}
    fghij => 69e45c25-ec89-4563-86ab-bc192dcc3b4f: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde', '69e45c25-ec89-4563-86ab-bc192dcc3b4f': 'fghij'}
    abcde => 02079cb4-6847-48aa-924e-0514d82a43f4: {'61997a1b-3f8a-4b0f-87f6-19d5cafee63f': 'abcde', '02079cb4-6847-48aa-924e-0514d82a43f4': 'abcde', '69e45c25-ec89-4563-86ab-bc192dcc3b4f': 'fghij'}
    bob@dylan:~$
```

### :wrench: Task setup.
```bash
```

### :heavy_check_mark: Solution
> [:point_right: api/v1/auth/session_auth.py](api/v1/auth/session_auth.py)
