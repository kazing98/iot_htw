The repository for this project is empty
You can get started by cloning the repository or start adding files to it with one of the following options.

Command line instructions
You can also upload existing files from your computer using the instructions below.

Git global setup
git config --global user.name "Rohan Panda"
git config --global user.email "rohan.panda@student.htw-berlin.de"
Create a new repository
git clone git@gitlab.rz.htw-berlin.de:s0595920/m_iot_ws2425_s0595920.git
cd m_iot_ws2425_s0595920
git switch --create main
touch README.md
git add README.md
git commit -m "add README"
git push --set-upstream origin main
Push an existing folder
cd existing_folder
git init --initial-branch=main
git remote add origin git@gitlab.rz.htw-berlin.de:s0595920/m_iot_ws2425_s0595920.git
git add .
git commit -m "Initial commit"
git push --set-upstream origin main
Push an existing Git repository
cd existing_repo
git remote rename origin old-origin
git remote add origin git@gitlab.rz.htw-berlin.de:s0595920/m_iot_ws2425_s0595920.git
git push --set-upstream origin --all
git push --set-upstream origin --tags