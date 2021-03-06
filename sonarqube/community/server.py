#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import API_SERVER_VERSION_ENDPOINT


class SonarQubeServer(RestClient):
    """
    SonarQube server Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeServer, self).__init__(**kwargs)

    def get_server_version(self):
        """
        Version of SonarQube in plain text

        :return:
        """
        resp = self.get(API_SERVER_VERSION_ENDPOINT)
        return resp.text
