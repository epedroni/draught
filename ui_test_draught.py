#!/usr/bin/env python3

import draught
import unittest
import os
import shutil
from datetime import date

# So-called UI tests, as these test Draught's "entry point".
# Draught is such a small project that the distinction between
# UI, integration and unit tests falls apart, but as an exercise
# in testing, UI tests have been written.
# The test site is created once and cleaned before each test, to
# minimise the number of filesystem operations.

# Superclass with factored-out setup
class DraughtTests(unittest.TestCase):

    def setUp(self):
        cleanDirectories()

# Happy-path content creation using the interface
class ContentCreationTests(DraughtTests):

    def test_createNewPost(self):
        draught.main(("draught", "new", "post", "Post Name"))
        expectedFileName = date.isoformat(date.today()) + "-post-name.md"
        self.assertTrue(os.path.exists(os.path.join("_posts", expectedFileName)))
        
    def test_createNewDraft(self):
        draught.main(("draught", "new", "draft", "Draft Name"))
        expectedFileName = "draft-name.md"
        self.assertTrue(os.path.exists(os.path.join("_drafts", expectedFileName)))
        
    def test_createNewCollectionContent(self):
        draught.main(("draught", "new", "coll", "Content Name"))
        expectedFileName = "content-name.md"
        self.assertTrue(os.path.exists(os.path.join("_coll", expectedFileName)))

# Happy-path content creation with templates using the interface
class ContentCreationWithTemplateTests(DraughtTests):

    def test_defaultTemplatePost(self):
        draught.main(("draught", "new", "post", "Template Test Post"))
        postFile = date.isoformat(date.today()) + "-template-test-post.md"
        with open(os.path.join("_posts", postFile)) as post:
            actualPostContent = post.read()
        with open("../resources/template.yml") as default:
            expectedPostContent = default.read().format(title="\"Template Test Post\"") 
        self.assertTrue(actualPostContent == expectedPostContent)
        
    def test_defaultTemplateDraft(self):
        draught.main(("draught", "new", "draft", "Template Test Draft"))
        draftFile = "template-test-draft.md"
        with open(os.path.join("_drafts", draftFile)) as draft:
            actualDraftContent = draft.read()
        with open("../resources/template.yml") as default:
            expectedDraftContent = default.read().format(title="\"Template Test Draft\"") 
        self.assertTrue(actualDraftContent == expectedDraftContent)
    
    def test_defaultTemplateColl(self):
        draught.main(("draught", "new", "coll", "Template Test Coll"))
        collFile = "template-test-coll.md"
        with open(os.path.join("_coll", collFile)) as coll:
            actualCollContent = coll.read()
        with open("../resources/template.yml") as default:
            expectedCollContent = default.read().format(title="\"Template Test Coll\"")        
        self.assertTrue(actualCollContent == expectedCollContent)

    def test_customTemplatePost(self):
        template = """
            ---
            title: {title}
            layout: post
            ---
            """
        with open(".templates/posts", "w") as postTemplate:
            postTemplate.write(template)
            
        draught.main(("draught", "new", "post", "Custom Template Test Post"))
        postFile = date.isoformat(date.today()) + "-custom-template-test-post.md"
        with open(os.path.join("_posts", postFile)) as post:
            actualPostContent = post.read()
        expectedPostContent = template.format(title="\"Custom Template Test Post\"") 
        self.assertTrue(actualPostContent == expectedPostContent)
        
    def test_customTemplateDraft(self):
        template = """
            ---
            title: {title}
            layout: draft
            ---
            """
        with open(".templates/drafts", "w") as draftTemplate:
            draftTemplate.write(template)
            
        draught.main(("draught", "new", "draft", "Custom Template Test Draft"))
        draftFile = "custom-template-test-draft.md"
        with open(os.path.join("_drafts", draftFile)) as draft:
            actualDraftContent = draft.read()
        expectedDraftContent = template.format(title="\"Custom Template Test Draft\"") 
        self.assertTrue(actualDraftContent == expectedDraftContent)
        
    def test_customTemplateColl(self):
        template = """
            ---
            title: {title}
            layout: coll
            ---
            """
        with open(".templates/coll", "w") as collTemplate:
            collTemplate.write(template)
            
        draught.main(("draught", "new", "coll", "Custom Template Test Coll"))
        collFile = "custom-template-test-coll.md"
        with open(os.path.join("_coll", collFile)) as coll:
            actualCollContent = coll.read()
        expectedCollContent = template.format(title="\"Custom Template Test Coll\"") 
        self.assertTrue(actualCollContent == expectedCollContent)
        
# Irregular cases
class InvalidContentCreation(DraughtTests):

    def test_exitIfPostExists(self):
        draught.main(("draught", "new", "post", "Post Name"))
        
        with self.assertRaises(SystemExit):
            draught.main(("draught", "new", "post", "Post Name"))
            
    def test_exitIfDraftExists(self):
        draught.main(("draught", "new", "draft", "Draft Name"))
        
        with self.assertRaises(SystemExit):
            draught.main(("draught", "new", "draft", "Draft Name"))
            
    def test_exitIfCollExists(self):
        draught.main(("draught", "new", "coll", "Coll Name"))
        
        with self.assertRaises(SystemExit):
            draught.main(("draught", "new", "coll", "Coll Name"))
            
    def test_existingPostNotOverwritten(self):
        draught.main(("draught", "new", "post", "Post Name"))
        fileName = date.isoformat(date.today()) + "-post-name.md"
        with open(os.path.join("_posts", fileName), "a") as post:
            post.write("This content should still be there")
        
        try:
            draught.main(("draught", "new", "post", "Post Name"))
        except:
            pass
        
        with open(os.path.join("_posts", fileName)) as post:
            self.assertTrue(post.read().find("This content should still be there"))
            
    def test_existingDraftNotOverwritten(self):
        draught.main(("draught", "new", "draft", "Draft Name"))
        fileName = "draft-name.md"
        with open(os.path.join("_drafts", fileName), "a") as draft:
            draft.write("This content should still be there")
        
        try:
            draught.main(("draught", "new", "draft", "Draft Name"))
        except:
            pass
        
        with open(os.path.join("_drafts", fileName)) as draft:
            self.assertTrue(draft.read().find("This content should still be there"))
    
    def test_existingCollNotOverwritten(self):
        draught.main(("draught", "new", "coll", "Coll Name"))
        fileName = "coll-name.md"
        with open(os.path.join("_coll", fileName), "a") as coll:
            coll.write("This content should still be there")
        
        try:
            draught.main(("draught", "new", "coll", "Coll Name"))
        except:
            pass
        
        with open(os.path.join("_coll", fileName)) as coll:
            self.assertTrue(coll.read().find("This content should still be there"))
            

# Supporting functions
def createTestWebsite():
    os.mkdir("test_site")
    os.chdir("test_site")
    
    with open("_config.yml", "w") as config:
        config.write("""
        name: Test Site
        description: A fake site for testing Draught.

        # baseurl will often be '', but for a project page on gh-pages, it needs to
        # be the project name.
        # *** IMPORTANT: If your local "jekyll serve" throws errors change this to '' or
        #     run it like so: jekyll serve --baseurl=''
        baseurl: '--'
        
        collections:
            coll:
                output: true
        """)
    
    os.mkdir("_posts")
    os.mkdir("_drafts")
    os.mkdir("_coll")
    os.mkdir(".templates")

def cleanDirectories():
    directories = ("_posts", "_drafts", "_coll", ".templates")
    for directory in directories:
        for fileName in os.listdir(directory):
            filePath = os.path.join(directory, fileName)
            try:
                os.remove(filePath)
            except Exception as e:
                print(e)

def cleanUp():
    os.chdir("..")
    shutil.rmtree("test_site")

if __name__ == "__main__":
    createTestWebsite()
    unittest.main(exit=False)
    cleanUp()
