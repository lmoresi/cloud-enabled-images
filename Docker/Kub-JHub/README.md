## Kub-JHub

This is the base image for a Kubernetes / Jupyterhub deployment in the underworld
Cloud or for deployment to binder environments

  - It has the basic infrastructure for underworld codes including PETSc, MPI, numpy etc
  - It has the necessary jupyterhub and jupyterlab installation and necessary extensions
  - It does have the relevant jupyter installations
  - It does **not** have the underworld or quagmire installation
  - It does **not** have any of the access tokens required 

The Kubernetes deployment requires there to be a post-spawn python script to install
various files into the users persistent storage (when provided). The script that
is provided will install files from various standard locations. It is optional to
run a post-spawn script and the name of the script is part of the description of the image.


### Base image content
