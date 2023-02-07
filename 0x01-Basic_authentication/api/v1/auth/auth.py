#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if auth is required.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to get authorization header.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get user from request.
        """
        return None
