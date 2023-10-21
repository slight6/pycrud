# Linking MongoDB with my python apps

1. First off, I know md, I just don't use it enough to bother with properly formatting it just yet.
2. I have other things on my mind.
3. I pretty much only have .md files all over the place for various notes that some day I hope to get back to and clean up a bit.
4. This is more or less a templating repo for me to have on hand as a guide to hooking up a python app to a backend database. 
5. Currently I've got it connected to MongoDB no matter how much I dislike it.
6. Squeal or NoSqueal will be next somewhere, possibly a Cassandra vector database for some ML/AI stuff.
7. I bounce around a bit, the only thing I know for sure anymore is one day I'll be dead.

## String variable for .env file

`MONGODB_URI=mongodb+srv://admin_user:admin_password@cluster0.afcldfx.mongodb.net/?retryWrites=true&w=majority`

### Security is with a key

> That key is the .env file in the root directory, added to the exclude file at /.git/info/exclude
