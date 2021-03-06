# coding=utf-8
#
# Copyright © 2015 VMware, Inc. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions
# of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from tests.config import *
from nsxramlclient.client import NsxClient

__author__ = 'yfauser'


def create_nvc(session, domain='domain-c7'):
    nwf_spec = session.extract_resource_body_schema('nwfabricConfig', 'update')

    nwf_spec['nwFabricFeatureConfig']['resourceConfig']['resourceId'] = domain

    response = session.update('nwfabricConfig', request_body_dict=nwf_spec)

    session.view_response(response)


def get_nfw_features(session):
    response = session.read('nwfabricFeatures')
    session.view_response(response)


def get_nfw_status(session, resource='domain-c7'):
    response = session.read('nwfabricStatus', query_parameters_dict={'resource': resource})
    session.view_response(response)


def delete_nfw(session, domain='domain-c7'):
    nwf_spec = session.extract_resource_body_schema('nwfabricConfig', 'delete')

    nwf_spec['nwFabricFeatureConfig']['resourceConfig']['resourceId'] = domain

    response = session.delete('nwfabricConfig', request_body_dict=nwf_spec)

    session.view_response(response)


def main():
    session = NsxClient(nsxraml_file, nsxmanager, nsx_username, nsx_password, debug=True)

    create_nvc(session)

    get_nfw_features(session)

    get_nfw_status(session)

    delete_nfw(session)


if __name__ == "__main__":
    main()

