## Organisations

This is a json file that is read by the cloud service.

The list of organisations corresponds to the other folders in this repository where a filed named
`supported_images.json` is expected (and with a standard format - see examples)

This list will be read when a user authenticated (via github) to the underworld cloud. If no organisations
match, only those images in 'public-access' will be available. Note, 'public-access' is not the same as
using binder ... we still request github authentication.
