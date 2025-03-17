---
title: Blog Guideline
authors:
  - name: Myeongseok
    affiliations: KAIST
    email: myeongseok@kaist.ac.kr
license: CC-BY-4.0
date: 2024-11-13
---

This post summarizes the [MyST official documentation guidelines](https://mystmd.org/guide), highlighting the key points.

<br/><br/>

## 0. Prerequisites 

1. Ensure Python and git are installed.
2. Install TeX-related packages. (https://www.tug.org/texlive/) On Mac, install MacTeX. (This is needed when creating PDF files in academic paper format.)

<br/><br/>

## 1. Install & Initialize

```bash
pip install mystmd
myst init
```
It will ask if you want to run `myst start` right away, but since there's no need to start immediately, enter N.


<br/><br/>

## 2. Directory Structure
mystmd automatically reads md and ipynb files without special configuration. It even reads files inside folders automatically. Additionally, note that if you index folder and file names like `01-`, `02-`, it understands that order. Also, if there are both folders and files in the same directory, it reads files first, then files inside the folders. So if you place an `about-me.md` file in the root folder and manage the rest of the materials inside folders, the about-me file will be positioned at the top.

The directory structure of this blog is as follows: (README.md is the main page of the blog.)

```bash
README.md
about-me.md
01-writing/
├── 01-why-i-use-myst.md
├── 02-blog-guideline.md
02-research/
├── 01-literature-review.md
├── 02-research-2.md
```

<br/><br/>
## 3. myst.yml
The most important file automatically generated when you run `myst init` is myst.yml, which contains all the settings for the blog. As noted in the first line comment below, refer to the [official documentation](https://mystmd.org/guide/frontmatter) for detailed information. Here are some options:
- Folders listed in the exclude section are not included in the blog.
- If you write your GitHub address in the github section, a GitHub icon will be created at the top of the blog.
- In site, you can set the blog's theme, favicon, logo, etc.

```yaml
# See docs at: https://mystmd.org/guide/frontmatter
version: 1
project:
  id: 7f4425d6-d197-4904-88a4-81cd23fa671d
  # title:
  # description:
  # keywords: []
  # authors: []
  github: https://github.com/myeongseok-kwon/blog
  # To autogenerate a Table of Contents, run "myst init --write-toc"
  exclude:
    - venv/**
    - draft/**
    - data/**
    - images/**
site:
  template: book-theme
  options:
    favicon: images/favicon.ico
    logo: images/site_logo.png
```

<br/><br/>
## 4. myst start
Enter `myst start` to run the blog. Since the blog runs locally by default, you need to be connected to the internet. To exit the blog, press `Ctrl + C`. You can check the address in the terminal where you ran it, by default it runs at https://localhost:3000. You can see the blog change in real-time as you add, modify and save markdown and ipynb files.


<br/><br/>
## 5. Deployment
Refer to the [github pages deployment guidelines](https://mystmd.org/guide/deployment-github-pages) to deploy your blog. In summary:
1. Create a github repository (public), and push your working directory.
2. Select the Github Actions deployment method in github repo -> Settings -> Pages as shown in [](#github-actions).
3. Run myst init --gh-pages


:::{figure} ../images/github-actions.png
:label: github-actions
:width: 60%
:align: left
Selecting the GitHub Actions deployment method
:::```