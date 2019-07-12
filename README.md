## cloud-enabled-images

Build information and machine-readable docker image information for underworld cloud

[![Build Status](https://travis-ci.com/underworld-geodynamics-cloud/cloud-enabled-images.svg?branch=master)](https://travis-ci.com/underworld-geodynamics-cloud/cloud-enabled-images)

## Organisations

The `organisations-list` directory contains the supported GitHub organisations. If you are a public member of one of those organisations, then the images for that organisation will be available to you. This list is machine-readable json and is used by the jupyter hub deployment as each user logs in.

Currently, the following organisations have published images

  -  **public-access** - Only a GitHub login is required
  -  **underworld-community** - Users of the Underworld suite of codes
  -  **Underworld-Geodynamics-Education** - Teaching resources for Computational Geodynamics
  -  **underworldcode** - Underworld developers

## Supported docker images by organisation

For each of the supported GitHub organisations, the `supported_images.json` file is read by the hub spawner for the underworld  cloud and populates the list of images that the user can select. For example, if the user is a (public) member of the [Underworld-Geodynamics-Education](https://github.com/Underworld-Geodynamics-Education) group, then he/she will be able to run any of the images that are listed in `Underworld-Geodynamics-Education/supported_images.json`
