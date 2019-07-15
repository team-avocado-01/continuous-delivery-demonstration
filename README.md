# Continuous Delivery Demonstration

## Introduction to project

A workflow which utlises automated testing and pull requests allows developers to change, test and deploy code quickly and with confidence. Using peer reviewed code merges such as pull requests in GitHub also adds transparency to your teams work.

Typical pipelines for continuous integration / continuous delivery projects will include a repository on a VCS (Version Control System) that the team is working on and  CI/CD software that watches a project repo and builds the code from multiple branches and runs tests. After successful results from testing the code should then be deployed. This means that a developer just has to commit their changes and  the rest is automated. This will encourage regular changes and give more time to write productional code. 

This project is a full CI/CD pipeline which takes in transformed data and runs tests to validate and deploy the code following a peer-reviewed pull request.

## Repo Structure

This project includes a CI/CD workflow using CircleCI, and GitHub as the version control system.

## Included:

CircleCI config YAML file
Input/Output data that is tested and deployed
SRC folder included Python scripts
Tests folder which includes tests to be ran in the build written in Python
Contributing.md file which explains setup and guidance to using the repo
Pipfile which instructs packages to be built
  
This is an open-source project, for contribution commit your changes and submit pull requests for an administrators review