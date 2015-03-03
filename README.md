# Draught

A Python tool for creating and managing content for Jekyll websites.

Current features:
* Create new posts and drafts;
* Create new content for collections;
* Publish drafts;
* Template front matter for posts, drafts and collections.

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

When creating content, Draught will attempt to insert specific front matter for each content type. Draught looks for templates as plain-text files in .templates, under the website root. 


