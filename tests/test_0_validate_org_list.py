import pytest
import json
import os

def read_known_orgs_from_json():
    """ Read the json file from this repo, parse to a python list and return the list"""

    org_file = "organisations-list/organisations.json"

    with open(org_file) as f:
        orgs_dict = json.load(f)

    orgs = orgs_dict["orgs"]

    return orgs


def test_valid_orgs_list():

    orgs_list = read_known_orgs_from_json()
    assert isinstance(orgs_list, list)
    return


def test_image_format_valid():

    this_json = os.path.join("docker-images","supported_images.json")
    with open(this_json) as f:
        im_list = json.load(f)

    for image in im_list:
        keys = image.keys()
        for expected_key in ['id', 'description', 'imagename', 'poststart', 'notebook_dir', 'default_url', 'cmd', 'organisations']:
            assert expected_key  in keys


def test_no_orphan_images():

    this_json = os.path.join("docker-images","supported_images.json")
    with open(this_json) as f:
        im_list = json.load(f)

    orgs_list = read_known_orgs_from_json()

    our_orgs = set()

    for image in im_list:
        for org in image["organisations"]:
            our_orgs.add(org)

    for org in our_orgs:
        assert org in orgs_list
