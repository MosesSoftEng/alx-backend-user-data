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


## [3. User ID for Session ID](api/v1/auth/session_auth.py)
### :page_with_curl: Task requirements.
Score: 0.0% (Checks completed: 0.0%)

Update `SessionAuth` class:

Create an instance method `def user_id_for_session_id(self, session_id: str = None) -> str:` that returns a `User` ID based on a Session ID:

* Return `None` if `session_id` is `None`
* Return `None` if `session_id` is not a string
* Return the value (the User ID) for the key `session_id` in the dictionary `user_id_by_session_id`.
* You must use `.get()` built-in for accessing in a dictionary a value based on key

Now you have 2 methods (`create_session` and `user_id_for_session_id`) for storing and retrieving a link between a `User` ID and a Session ID.
```
    bob@dylan:~$ cat main_2.py 
    #!/usr/bin/env python3
    """ Main 2
    """
    from api.v1.auth.session_auth import SessionAuth
    
    sa = SessionAuth()
    
    user_id_1 = "abcde"
    session_1 = sa.create_session(user_id_1)
    print("{} => {}: {}".format(user_id_1, session_1, sa.user_id_by_session_id))
    
    user_id_2 = "fghij"
    session_2 = sa.create_session(user_id_2)
    print("{} => {}: {}".format(user_id_2, session_2, sa.user_id_by_session_id))
    
    print("---")
    
    tmp_session_id = None
    tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
    print("{} => {}".format(tmp_session_id, tmp_user_id))
    
    tmp_session_id = 89
    tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
    print("{} => {}".format(tmp_session_id, tmp_user_id))
    
    tmp_session_id = "doesntexist"
    tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
    print("{} => {}".format(tmp_session_id, tmp_user_id))
    
    print("---")
    
    tmp_session_id = session_1
    tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
    print("{} => {}".format(tmp_session_id, tmp_user_id))
    
    tmp_session_id = session_2
    tmp_user_id = sa.user_id_for_session_id(tmp_session_id)
    print("{} => {}".format(tmp_session_id, tmp_user_id))
    
    print("---")
    
    session_1_bis = sa.create_session(user_id_1)
    print("{} => {}: {}".format(user_id_1, session_1_bis, sa.user_id_by_session_id))
    
    tmp_user_id = sa.user_id_for_session_id(session_1_bis)
    print("{} => {}".format(session_1_bis, tmp_user_id))
    
    tmp_user_id = sa.user_id_for_session_id(session_1)
    print("{} => {}".format(session_1, tmp_user_id))
    
    bob@dylan:~$
    bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_2.py 
    abcde => 8647f981-f503-4638-af23-7bb4a9e4b53f: {'8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
    fghij => a159ee3f-214e-4e91-9546-ca3ce873e975: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde'}
    ---
    None => None
    89 => None
    doesntexist => None
    ---
    8647f981-f503-4638-af23-7bb4a9e4b53f => abcde
    a159ee3f-214e-4e91-9546-ca3ce873e975 => fghij
    ---
    abcde => 5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee: {'a159ee3f-214e-4e91-9546-ca3ce873e975': 'fghij', '8647f981-f503-4638-af23-7bb4a9e4b53f': 'abcde', '5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee': 'abcde'}
    5d2930ba-f6d6-4a23-83d2-4f0abc8b8eee => abcde
    8647f981-f503-4638-af23-7bb4a9e4b53f => abcde
    bob@dylan:~$
```

### :wrench: Task setup.
```bash
```

### :heavy_check_mark: Solution
> [:point_right: api/v1/auth/session_auth.py](api/v1/auth/session_auth.py


## [4. Session cookie](api/v1/auth/auth.py)
### :page_with_curl: Task requirements.
Score: 0.0% (Checks completed: 0.0%)

Update `api/v1/auth/auth.py` by adding the method `def session_cookie(self, request=None):` that returns a cookie value from a request:

* Return `None` if `request` is `None`
* Return the value of the cookie named `_my_session_id` from `request` \- the name of the cookie must be defined by the environment variable `SESSION_NAME`
* You must use `.get()` built-in for accessing the cookie in the request cookies dictionary
* You must use the environment variable `SESSION_NAME` to define the name of the cookie used for the Session ID

In the first terminal:
```
    bob@dylan:~$ cat main_3.py
    #!/usr/bin/env python3
    """ Cookie server
    """
    from flask import Flask, request
    from api.v1.auth.auth import Auth
    
    auth = Auth()
    
    app = Flask(__name__)
    
    @app.route('/', methods=['GET'], strict_slashes=False)
    def root_path():
        """ Root path
        """
        return "Cookie value: {}\n".format(auth.session_cookie(request))
    
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port="5000")
    
    bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_3.py 
     * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    ....
```

In a second terminal:
```
    bob@dylan:~$ curl "http://0.0.0.0:5000"
    Cookie value: None
    bob@dylan:~$
    bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id=Hello"
    Cookie value: Hello
    bob@dylan:~$
    bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id=C is fun"
    Cookie value: C is fun
    bob@dylan:~$
    bob@dylan:~$ curl "http://0.0.0.0:5000" --cookie "_my_session_id_fake"
    Cookie value: None
    bob@dylan:~$
```

### :wrench: Task setup.
```bash
```

### :heavy_check_mark: Solution
> [:point_right: api/v1/auth/auth.py](api/v1/app.py)

## [5. Before request](api/v1/app.py)
### :page_with_curl: Task requirements.
Score: 0.0% (Checks completed: 0.0%)

Update the `@app.before_request` method in `api/v1/app.py`:

* Add the URL path `/api/v1/auth_session/login/` in the list of excluded paths of the method `require_auth` \- this route doesn’t exist yet but it should be accessible outside authentication
* If `auth.authorization_header(request)` and `auth.session_cookie(request)` return `None`, `abort(401)`

In the first terminal:
```
    bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
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
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/auth_session/login" # not found but not "blocked" by an authentication system
    {
      "error": "Not found"
    }
    bob@dylan:~$
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me"
    {
      "error": "Unauthorized"
    }
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh" # Won't work because the environment variable AUTH_TYPE is equal to "session_auth"
    {
      "error": "Forbidden"
    }
    bob@dylan:~$
    bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=5535d4d7-3d77-4d06-8281-495dc3acfe76" # Won't work because no user is linked to this Session ID
    {
      "error": "Forbidden"
    }
    bob@dylan:~$
```
### :wrench: Task setup.
```bash
```

### :heavy_check_mark: Solution
> [:point_right: api/v1/app.py](api/v1/app.py)
