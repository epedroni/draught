# Draught

[![Build Status](https://travis-ci.org/epedroni/draught.svg?branch=dev)](https://travis-ci.org/epedroni/draught)

A Python tool for creating and managing content for Jekyll websites.

Current features:
* Create new posts and drafts;
* Create new content for collections;
* Publish drafts;
* Template front matter for posts, drafts and collections.

For a built executable, look under [build](https://github.com/epedroni/draught/tree/master/build).

## Usage

### Creating Content

To create new content, use the `new` command anywhere within a Jekyll website. For instance, to create a new post:

```
~/my_blog $ draught new post "Five Foos in a Bar"
```

This creates ~/my_blog/_posts/YYYY-MM-DD-five-foos-in-a-bar.md with the current date. The following is also possible:

```
~/my_blog/_posts $ draught new draft "Around the Foo in 80 Bars"
```

This creates ~/my_blog/_drafts/around-the-foo-in-80-bars.md. For user-defined collections, content can be created using the collection name as it is defined in _config.yml. For example, given a collection called "projects":

```
~/my_blog $ draught new projects "Foobar"
```

creates ~/my_blog/_projects/foobar.md.

### Front Matter

When creating content, Draught will attempt to insert front matter for each content type. For each content type, Draught looks for a plain text file under .templates with an identical name. For example, the contents of ~/my_blog/.templates/posts are automatically added to any posts created with `draught new post`. Templates also work for collections, as long as they are appropriately named. If a template is not defined, the following default is used:

```
---
title: "Enter title"
---
```

When writing templates, `{title}` can be used as a placeholder for the content title. So running

```
~/my_blog $ draught new post "Five Foos in a Bar"
```

with a template such as ~/my_blog/.templates/posts containing

```
---
title: {title}
layout: post
---
```

will create the file ~/my_blog/_posts/YYYY-MM-DD-five-foos-in-a-bar.md with the following front matter:

```
---
title: "Five Foos in a Bar"
layout: post
---
```

### Publishing Drafts

Existing drafts can be turned into posts by running `draught publish`, which shows a numbered list of all available drafts. One or more drafts can be addressed by index, causing them to be copied to _posts with the current date. 
