#!/bin/bash
docker run -it -v ${PWD}:/home/openfoam/afg_labcar --memory="4g" --cpus="6" openfoam/openfoam10-paraview56:latest bash

# To see how many CPU you have "lscpu"