# IMR Report Generator

## Install and setup
Ask in house IT support for with the setup of the NAS!

### Setup on NAS
First run the shell script "run-server.sh".
Then share/map the folder named "output" in the app directory with users who needs access.
Provide these users with an link http://nas-address:5001, where "nas-address"
is the address of the NAS server.

### NAS Requirements
Docker and docker-compose
Open port 5001/tcp on firewall for the user interface

## Usage
Start by opening link provided by IT support in a browser.
The address should look something like this: "http://nas-server:5001".
First uploaded an Excel file either by drag and drop or by clicking the drag and drop area.
Then press the submit button and wait for the start button to show and click it to start the download process.
The generated and downloaded files will appear in the shared folder on the NAS also provided by IT support.

The metadata will be generated in the Excel file metadata.xlsx.
