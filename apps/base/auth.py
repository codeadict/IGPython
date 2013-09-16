# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
import logging

from django.contrib.auth.models import User

log = logging.getLogger(__name__)

class OWUserBackend(object):
    """
    Backend to authenticate with Username or email
    """
    supports_anonymous_user = False
    supports_object_permissions = True

    def authenticate(self, username=None, password=None):
        log.debug("Attempting to authenticate user %s" % (username,))
        try:
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            log.debug("User does not exist: %s" % (username,))
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None