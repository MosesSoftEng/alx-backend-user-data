#!/usr/bin/env python3
"""Authentication module.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if auth is required.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if path == excluded_path or excluded_path.startswith(path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method to get authorization header.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get user from request.
        """
        return None
