# Python modules + main script example

This repository provides an example folder structure for a project containing modules and an executable script.  
Bottom line is :

- Files within a module `lib` should import other files from `lib` with relative paths, because they don't know if `lib` represents an actual module or a submodule for the current project.
- Files importing `lib` can reference it as an actual module, without relative paths. Those are exclusive to the current project anyway.

For a repository that only contains a module and no executable scripts, the module files can sit in the root directory.