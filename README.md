# Contributing to the project

1. Clone the project and create a new branch using the naming convention '<your-name>/<feature-description>'. An example branch name is 'robertp/create_initial_server'.

2. Make your changes and commit them with a meaningful commit message.

3. Push your branch to the remote using ``git push origin <branch_name>``

4. Create a merge request, get an approval and merge it.


# Docker Instructions

1. While docker running, build the docker image using 
     > docker build -t wardrobe_diffusion .
2. Run the docker container with the command
     > docker run -d --name wd_container -p 80:80 wardrobe_diffusion
3. Veryify the container is running and test the api by going to localhost/docs.
    
    *Note: replace local hoset with hosting url if running on webserver*