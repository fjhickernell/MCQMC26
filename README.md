# SIAM UQ 2026 Talk

This repository contains the slides and supporting material for my talk at the

SIAM Conference on Uncertainty Quantification (UQ) 2026.

## Slides

The slides are available online:

https://fjhickernell.github.io/SIAMUQ26/slides/SIAMUQ2026.html

They are written using Quarto and RevealJS.

## Repository Structure

SIAMUQ26
│
├── index.qmd          # website landing page
├── slides/            # slide source files
├── classlib/          # HickernellClassLib submodule
├── qmcsoftware/       # QMCPy submodule
└── .github/workflows  # GitHub Actions deployment

The slides rely on two submodules:

HickernellClassLib  
Provides shared plotting helpers, slide macros, and utilities.

QMCPy  
Python library for quasi-Monte Carlo methods used in the slides.

## Clone the Repository

Clone with submodules:

git clone --recurse-submodules https://github.com/fjhickernell/SIAMUQ26

If already cloned:

git submodule update --init --recursive

## Building Slides Locally

cd slides
quarto render

Then open

slides/_site/intro.html

## Continuous Deployment

GitHub Actions automatically builds and publishes the site when changes are pushed to `main`.

The workflow

1. checks out the repository with submodules
2. installs Python dependencies
3. installs classlib and qmcpy
4. renders the Quarto slides
5. publishes the website to GitHub Pages

## Author

Fred J. Hickernell  
Department of Applied Mathematics  
Illinois Institute of Technology
