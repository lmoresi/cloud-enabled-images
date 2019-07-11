import pytest
import json
import os

def read_known_orgs_from_json():
    """ Read the json file from this repo, parse to a python list and return the list"""

    org_file = "organisations-list/organisations.json"

    with open(org_file) as f:
        orgs_dict = json.load(f)

    orgs = orgs_dict["orgs"]

    return(orgs)


def test_valid_orgs_list():

    orgs_list = read_known_orgs_from_json()
    assert isinstance(orgs_list, list)
    return

@pytest.mark.parametrize("org", read_known_orgs_from_json())
def test_org_directories_valid(org):

    assert os.path.exists(org)
    assert os.path.exists(os.path.join(org,"supported_images.json"))

    return

## Should break if the valid directory fails
@pytest.mark.parametrize("org", read_known_orgs_from_json())
def test_org_directories_valid_json(org):

    this_json = os.path.join(org,"supported_images.json")
    with open(this_json) as f:
        im_list = json.load(f)

    assert isinstance(im_list, list)

    for image in im_list:
        assert isinstance(image, dict)

    return

## Should break if the valid image json fails
@pytest.mark.parametrize("org", read_known_orgs_from_json())
def test_image_format_valid(org):

    this_json = os.path.join(org,"supported_images.json")
    with open(this_json) as f:
        im_list = json.load(f)

    for image in im_list:
        keys = image.keys()
        for expected_key in ['id', 'description', 'imagename', 'poststart', 'notebook_dir', 'default_url', 'cmd']:
            assert expected_key  in keys
